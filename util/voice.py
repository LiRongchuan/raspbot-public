import os
import threading
import dashscope
from config import *
from tts import LocalTTS
from http import HTTPStatus
from dotenv import load_dotenv
from dashscope import Generation
from util.handler import Handler
from util.asr_callback import ASRCallback
from util.tts_callback import TTSCallback
from dashscope.audio.tts_v2 import SpeechSynthesizer
from dashscope.audio.asr import TranslationRecognizerRealtime

# DashScope API Key
load_dotenv('key.env')
dashscope.api_key = os.environ['ali_key']

# Global State
user_input_ready = threading.Event()

# Process input, respond with LLM
messages = []
handler = Handler()
def process_input(user_input):
    global messages
    print(f"\n处理用户输入: {user_input}")
    messages.append({"role": "user", "content": PROMPT + user_input})
    responses = Generation.call(
        model="qwen-turbo",
        messages=messages,
        result_format="message",
        stream=True,
        incremental_output=True
    )
    tts_callback = TTSCallback()
    synthesizer = LocalTTS() if LOCAL_TTS else SpeechSynthesizer(
        model="cosyvoice-v2",
        voice="longxiaochun_v2",
        format=TTS_FORMAT,
        callback=tts_callback
    )
    reply = ""
    for response in responses:
        if response.status_code == HTTPStatus.OK:
            content = response.output.choices[0]["message"]["content"]
            reply += content
            print(content,end="",flush=True)
            if not LOCAL_TTS:
                synthesizer.streaming_call(content)  # 不需要 start()
        else:
            print(f"\n生成回复失败: {response.message}")
    # 加入指令处理
    code, reply = reply.split('#', 2)
    handler.handle(code)
    messages.append({"role": "assistant", "content": reply})
    synthesizer.speak(reply) if LOCAL_TTS else synthesizer.streaming_complete()  # 仍需调用
    print("\n回复播放完成，重新进入监听状态")
    
# Main Loop
def run_assistant():
    user_input_ready.clear()
    asr_callback = None
    recognizer = None
    while True:
        print("\n等待用户输入...")
        if asr_callback:
            asr_callback = None
        if recognizer:
            recognizer = None
        asr_callback = ASRCallback(user_input_ready)
        recognizer = TranslationRecognizerRealtime(
            model="gummy-realtime-v1",
            format=ASR_FORMAT,
            sample_rate=ASR_SAMPLE_RATE,
            transcription_enabled=True,
            translation_enabled=False,
            callback=asr_callback
        )
        recognizer.start()
        asr_callback.is_listening = True
        while asr_callback.is_listening and asr_callback.stream:
            try:
                data = asr_callback.stream.read(3200, exception_on_overflow=False)
                recognizer.send_audio_frame(data)
            except Exception as e:
                print(f"\n退出录音: {e}")
                break
        recognizer.stop()
        user_input_text = asr_callback.get_text()
        if user_input_ready.is_set():
            process_input(user_input_text)
            user_input_ready.clear()

if __name__ == "__main__":
    try:
        run_assistant()
    except Exception as e:
        print(f"\n程序退出: {e}")
