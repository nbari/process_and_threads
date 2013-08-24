from multiprocessing import Pool


def myfunc(i):
    print "sleeping 5 sec from process %d" % i
    time.sleep(3)
    print "finised sleeping from process %d" % i

if __name__ == '__main__':
    p = Pool()
    for i in range(10):
        p.apply_async(myfunc, i)
    p.join()
