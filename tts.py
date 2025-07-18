import pyttsx3

class LocalTTS:
    def __init__(self, voice_id='zh', rate=200, volume=1):
        self.engine = pyttsx3.init('espeak')
        self.engine.setProperty('voice', voice_id)
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
        
if __name__ == "__main__":
    tts = LocalTTS()
    text_to_speak = "你好，欢迎使用本地语音合成服务。"
    print(f"正在合成语音: {text_to_speak}")
    tts.speak(text_to_speak)
    print("语音合成完成。")