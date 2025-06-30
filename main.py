import threading
from util.wechat import detectTask
from util.voice import run_assistant

if __name__ == "__main__":
    detect_thread = threading.Thread(target=detectTask)
    detect_thread.daemon = True
    detect_thread.start()
    try:
        run_assistant()
    except KeyboardInterrupt:
        print("\n程序正在退出...")
        detect_thread.join(timeout=2.0)
        print("\n程序已退出。")