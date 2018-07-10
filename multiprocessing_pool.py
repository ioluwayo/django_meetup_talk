from time import time
from threading import Thread
from multiprocessing import Pool
from Display import profile

POOL_SIZE = 4


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True


def get_prime_factors(num):
    """
    Takes a number and returns a list of its factors tha are prime
    :param num:
    :return:
    """
    factors = []
    for factor in range(2, num + 1):
        if num % factor == 0:
            if is_prime(factor):
                factors.append(factor)
    return factors


class CustomThread(Thread):
    def __init__(self, *args, **kwargs):
        Thread.__init__(self, *args, **kwargs)
        self.result = None

    def run(self):
        self.result = self._target(*self._args, **self._kwargs)


def series(numbers_list):
    start = time()

    series_results = []
    for num in numbers_list:
        series_results.append(get_prime_factors(num))

    stop = time()
    return series_results, (start, stop)


def multithread(numbers_list):
    start = time()

    threads_results = []
    threads = []
    for n in numbers_list:
        thread = CustomThread(target=get_prime_factors, args=(n,))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
        threads_results.append(thread.result)

    stop = time()
    return threads_results, (start, stop)


def multiprocess_pool(numbers_list):
    start = time()

    pool = Pool(processes=POOL_SIZE)  # initial cost of process creation is pretty high
    pool_results = pool.map(get_prime_factors, numbers_list)
    pool.close()
    pool.join()  # context manager can also help here

    stop = time()
    return pool_results, (start, stop)


def multiprocess_pool_with_context_manager(numbers_list):
    start = time()

    pool_results = []
    with Pool(processes=POOL_SIZE) as pool:
        pool_results = pool.map(get_prime_factors, numbers_list)

    stop = time()
    return pool_results, (start, stop)


if __name__ == '__main__':
    numbers = [i for i in range(1000, 1300)]
    series_result, series_duration = series(numbers)
    thread_results, multithread_duration = multithread(numbers)
    multiprocessing_results, multiprocess_duration = multiprocess_pool_with_context_manager(numbers)

    print("Series: ", series_duration)
    print("Threads: ", multithread_duration)
    print("Multiprocessing: ", multiprocessing_results)
    profile([series_duration, multithread_duration, multiprocess_duration])
