from Queue import Empty
from multiprocessing import Process, Queue
import math
import time

def isprime(n):
    """ Returns True if n is prime and False otherwise """
    if not isinstance(n, int):
        raise TypeError("argument passed to is_prime is not of 'int' type")
    if n < 2:
        return False
    if n == 2:
        return True
    max = int(math.ceil(math.sqrt(n)))
    i = 2
    while i <=max:
        if n % i == 0:
            return False
        i += 1
    return True

def sum_primes(n):
    """ Calculates sum of all primes below given integer n """
    return sum([x for x in xrange(2, n) if isprime(x)])

def do_work(q):
    while True:
        try:
            x = q.get(block=False)
            print sum_primes(x)
        except Empty:
            break

def do_work(q):
    while True:
        try:
            x = q.get(block=False)
            print sum_primes(x)
        except Empty:
            break


if __name__ == '__main__':
    start_time = time.time()
    work_queue = Queue()
    for i in xrange(100000, 5000000, 100000):
        work_queue.put(i)

    processes = [Process(target=do_work, args=(work_queue,)) for i in range(2)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()

    print time.time() - start_time
