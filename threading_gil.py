from time import time
from threading import Thread
from multiprocessing import Pool
from visualize import profile

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


def run_series(numbers_list):
    start = time()

    series_results = []
    for num in numbers_list:
        series_results.append(get_prime_factors(num))

    stop = time()
    return series_results, (start, stop)


def run_threads(numbers_list):
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


if __name__ == '__main__':
    numbers = [i for i in range(1000, 1006)]

    series_result, series_duration = run_series(numbers)

    thread_results, thread_durations = run_threads(numbers)  # this should be faster right?

    print("Series: ", series_result)
    print("Threads: ", thread_results)
    profile([series_duration, thread_durations], labels=['Series', 'Thread'], colors=['r', 'y'])
