# the GIL does not protect object shared by threads from data races.
import os
from threading import Thread, Lock

pid_list = []


class CoolCounter:
    def __init__(self):
        self.count = 0
        self.lock = Lock()

    def increment(self, n):
        # with self.lock:
        self.count += n


def increment(counter):
    for i in range(100000):
        counter.increment(1)  # non atomic operation. in bytcode this is more than one instruction


def do_thread(counter, n):
    threads = []
    for i in range(n):
        thread = Thread(target=increment, args=(counter,))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()  # block until finished


if __name__ == '__main__':
    cool_counter = CoolCounter()
    do_thread(cool_counter, 3)
    print('The counter should be {}*{} = {}'.format(3, 100000, 3 * 100000))
    print('Its actual value is {}'.format(cool_counter.count))
