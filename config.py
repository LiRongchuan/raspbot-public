from dashscope.audio.tts_v2 import AudioFormat

# Audio Parameter
ASR_FORMAT = "pcm"
ASR_SAMPLE_RATE = 16000
TTS_FORMAT = AudioFormat.PCM_22050HZ_MONO_16BIT
TTS_RATE = 22050

INST = {"无指令": 0, "开启跌倒检测": 1, "关闭跌倒检测": -1}

# LLM Prompt
PROMPT = f" 你是一个可以识别指令的语音助手，具备精准匹配用户输入与指令类型的能力。指令类型与返回代码的对应关系为： \
{INST} \
当用户的输入与上述某种指令类型相关时，你需要返回对应的代码，若与所有指令类型均不相关，则返回代码 0。 \
输出格式统一为 “指令代码#你的回答”（例如输入“开启跌倒检测”，你应输出“1#ans，其中ans代表你的初始回答”）。 \
用户输入为："

# Use Local TTS Model
LOCAL_TTS = True

if __name__ == "__main__":
    print(PROMPT)