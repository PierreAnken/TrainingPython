import threading
import time


def thread_function():
    while True:
        time.sleep(1)
        print(f'Loop : {threading.current_thread().name}')


if __name__ == "__main__":
    print('debut\n')
    x = threading.Thread(target=thread_function, name="T1")
    x.start()
    y = threading.Thread(target=thread_function, name="T2")
    y.start()
