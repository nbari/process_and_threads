import time
from threading import Thread

class MyThread(Thread):
    def __init__(self):
        super(MyThread, self).__init__()

    def run(self):
        a, b = 0 , 1
        for i in range(100000):
            a, b = b, a + b


if __name__ == '__main__':
    start_time = time.time()
    t = MyThread()
    t.start()
    t.join()
    print time.time() - start_time
