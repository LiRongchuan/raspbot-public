import re
import time
import json
import threading
from tts import LocalTTS
from util.wechat import detectTask, detect_stop

class Handler:
    detect_thread = None
    tts = LocalTTS()
    
    def handle(self, code):
        """ Call the appropriate handler method based on code """
        if code == 0:
            pass
        elif code == 1:
            self.fall_detc_start()
        elif code == -1:
            self.fall_detc_end()

    def fall_detc_start(self):
        if self.detect_thread is None:
            detect_stop.clear()
            self.detect_thread = threading.Thread(target=detectTask)
            self.detect_thread.daemon = True
            self.detect_thread.start()
    
    def fall_detc_end(self):
        if self.detect_thread is not None:
            detect_stop.set()
            self.detect_thread.join()
            self.detect_thread = None
            
    def set_reminder(self, json_str):
        clean_json = re.sub(r'```(json)?', '', json_str).strip()
        try:
            data = json.loads(clean_json)
            minutes = data['minutesLater']
            name = data['scheduleName']
            if not isinstance(minutes, (int, float)) or minutes <= 0:
                return None
            reminder_thread = threading.Thread(
                target=self._reminder_worker,
                args=(minutes, name),
                name=f"Reminder-{name}"
            )
            reminder_thread.start()
            return reminder_thread
        except Exception:
            return None
    
    def _reminder_worker(self, minutes, name):
        seconds = minutes * 60
        time.sleep(seconds)  # 线程阻塞直到计时结束
        self.tts.speak(f"提醒：{name}")
        print(f"[提醒触发] {minutes}分钟后{name}")
        
if __name__ == "__main__":
    handler = Handler()
    json_str = """
    ```
    json
    {
    "minutesLater": 0.5,
    "scheduleName": "线上会议签到"
    }  
    ```
    """
    handler.set_reminder()