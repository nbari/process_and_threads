import time
from multiprocessing import Process

class MyProcess(Process):
    def __init__(self):
        super(MyProcess, self).__init__()

    def run(self):
        a, b = 0 , 1
        for i in range(100000):
            a, b = b, a + b


if __name__ == '__main__':
    start_time = time.time()
    p = MyProcess()
    p.start()
    print p.pid
    p.join()
    print p.exitcode
    print time.time() - start_time
