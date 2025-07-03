from util.voice import run_assistant

if __name__ == "__main__":
    try:
        run_assistant()
    except KeyboardInterrupt:
        print("\n程序已退出。")