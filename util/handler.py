import threading
from util.wechat import detectTask, detect_stop

class Handler:
    detect_thread = None
    
    def handle(self, code):
        """ Call the appropriate handler method based on code """
        try:
            code = int(code)
        except Exception:
            pass
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