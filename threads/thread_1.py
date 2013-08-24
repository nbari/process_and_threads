import time
from threading import Thread


def myfunc(i):
    print "sleeping 5 sec from thread %d" % i
    time.sleep(3)
    print "finished sleeping from thread %d" % i

for i in range(10):
    start_time = time.time()
    t = Thread(target=myfunc, args=(i,))
    t.start()
    #t.join()
    #print '\n' + 'Elapsed time: ' + str(time.time() - start_time)
