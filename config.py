from dashscope.audio.tts_v2 import AudioFormat

# Audio Parameter
ASR_FORMAT = "pcm"
ASR_SAMPLE_RATE = 16000
TTS_FORMAT = AudioFormat.PCM_22050HZ_MONO_16BIT
TTS_RATE = 22050

# LLM Prompt
PROMPT = "你来扮演老年人用户的孙子小毛，用简洁温暖的语言回复，用户输入为："

# Use Local TTS Model
LOCAL_TTS = True