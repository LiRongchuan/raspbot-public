import pyaudio
import threading
from config import ASR_SAMPLE_RATE
from dashscope.audio.asr import TranslationRecognizerCallback, TranscriptionResult, TranslationResult

class ASRCallback(TranslationRecognizerCallback):
    
    def __init__(self, user_input_ready, user_input_text):
        super().__init__()
        self.user_input_ready = user_input_ready
        self.user_input_text = user_input_text
        self.transcription_buffer = ""
        self.timer = None
        self.is_listening = True
        self.mic=None
        self.stream=None

    def on_open(self):
        self.mic = pyaudio.PyAudio()
        self.stream = self.mic.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=ASR_SAMPLE_RATE,
            input=True
        )
        print("ASR: 语音识别已启动，请开始说话...")

    def on_close(self):
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
            self.stream=None
        if self.mic:
            self.mic.terminate()
            self.mic=None
        print("ASR: 语音识别已关闭。")

    def on_event(self, request_id, transcription_result: TranscriptionResult, translation_result: TranslationResult, usage):
        if transcription_result:
            current_text = transcription_result.text.strip()
            if current_text:
                self.update_buffer(current_text)

    def update_buffer(self, text):
        self.transcription_buffer = text
        self.reset_timer()

    def reset_timer(self):
        if self.timer:
            self.timer.cancel()
        self.timer = threading.Timer(1, self.on_timeout)
        self.timer.start()

    def on_timeout(self):
        self.user_input_text = self.transcription_buffer.strip()
        if self.user_input_text:
            print(f"检测到停顿，用户输入完成：{self.user_input_text}")
            self.is_listening = False
            self.user_input_ready.set()