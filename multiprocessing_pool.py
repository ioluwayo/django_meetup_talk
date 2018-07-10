from time import time


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


if __name__ == '__main__':
    numbers = [i for i in range(1000, 1500)]
    total_duration = 0
    start = time()
    for i in numbers:
        result = get_prime_factors(i)
    stop = time()
    print('Total duration in series: ', stop - start)

    from threading import Thread

    threads = []
    start = time()
    for n in numbers:
        thread = Thread(target=get_prime_factors, args=(n,))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    stop = time()
    print('Total duration with threads: ', stop - start)

    from multiprocessing import Pool

    start = time()
    pool = Pool(processes=3)
    factors = pool.map(get_prime_factors, numbers)
    pool.close()
    pool.join()
    stop = time()
    print(factors)
    print("Total duration with multiprocessing: ", stop - start)
