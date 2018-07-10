from multiprocessing import Pool


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
   pass