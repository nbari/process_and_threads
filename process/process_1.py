import time
from multiprocessing import Pool


def myfunc(i):
    print "sleeping 5 sec from process %d" % i
    time.sleep(3)
    return i

def log_result(rs):
    print "finised sleeping from process %d" % i

if __name__ == '__main__':
    start_time = time.time()
    p = Pool()
    for i in range(10):
        p.apply_async(myfunc, args=(i,), callback=log_result)
    p.close()
    p.join()

    print '\n' + 'Elapsed time: ' + str(time.time() - start_time)
