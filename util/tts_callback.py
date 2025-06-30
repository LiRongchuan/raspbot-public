import pyaudio
from config import TTS_RATE
from dashscope.audio.tts_v2 import ResultCallback

class TTSCallback(ResultCallback):
    
    def __init__(self):
        super().__init__()
        self.audio = None
        self.stream = None

    def on_open(self):
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=TTS_RATE,
            output=True
        )
        print("TTS: 语音合成已启动。")

    def on_close(self):
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
            self.stream=None
        if self.audio:
            self.audio.terminate()
            self.audio=None
        print("TTS: 语音合成已关闭。")

    def on_data(self, data: bytes):
        if self.stream:
            self.stream.write(data)