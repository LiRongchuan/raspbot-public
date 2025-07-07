from dashscope.audio.tts_v2 import AudioFormat

# Audio Parameter
ASR_FORMAT = "pcm"
ASR_SAMPLE_RATE = 16000
TTS_FORMAT = AudioFormat.PCM_22050HZ_MONO_16BIT
TTS_RATE = 22050

INST = {"无指令": 0, "开启跌倒检测": 1, "关闭跌倒检测": -1}

PROMPT = [
"用简洁热情的语言回复，用户输入：",
"""根据用户描述内容提取目标信息 
如果未提供则设置为 无 
minutesLater可以为浮点数 若为提供则设置无
禁止添加未提供的信息 
按照要求的json格式回复，都为必填项，且为合法json格式 
```json 
{
    "minutesLater": 30,
    "scheduleName": "线上会议签到"
}
```
""",
]

# Use Local TTS Model
LOCAL_TTS = True

if __name__ == "__main__":
    print(PROMPT)