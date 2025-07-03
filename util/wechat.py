import os
import time
import requests
import threading
from dotenv import load_dotenv
from util.mpu6050 import mpu6050

load_dotenv('key.env')
WECHAT_SCKEY = os.environ['wechat_key']
WECHAT_PUSH_URL = f"https://sctapi.ftqq.com/{WECHAT_SCKEY}.send"
THRESHOLD = 50
MAX_CNT = 5

def wechatPushTask(message="检测到佩戴者跌倒！"):
    """通过Server酱发送微信推送通知"""
    try:
        data = {
            "title": "跌倒警报",
            "desp": message
        }
        response = requests.post(WECHAT_PUSH_URL, data=data)
        result = response.json()
        if result.get("code") == 0:
            print("\n微信推送成功")
        else:
            print(f"\n微信推送失败: {result.get('message')}")
    except Exception as e:
        print(f"\n微信推送异常: {str(e)}")

detect_stop = threading.Event()
mpu = mpu6050(0x68)

def detectTask():
    cnt = 0
    while not detect_stop.is_set():
        if cnt > MAX_CNT:
            print("\n检测到跌倒")
            wechatPushTask()
            cnt = 0
        try:
            gyro_data = mpu.get_gyro_data()
            if (abs(gyro_data['x']) > THRESHOLD or abs(gyro_data['y']) > THRESHOLD or abs(gyro_data['z']) > THRESHOLD):
                cnt += 1
            else:
                cnt = 0
        except Exception:
            break
        time.sleep(0.05)
    print("停止跌倒检测")
        
if __name__ == '__main__':
    detectTask()