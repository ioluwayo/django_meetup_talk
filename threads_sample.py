from threading import Thread
import os


def task_1(n):
    # do some cpu intensive work here
    print('I am thread {}. My process I.D is {}. I am executing task 1'.format(n, os.getpid()))


def task_2(n):
    # do some cpu intensive work here
    print('I am thread {}. My process I.D is {}. I am executing task 2'.format(n, os.getpid()))


if __name__ == '__main__':
    thread1 = Thread(target=task_1, args=(1,))
    thread2 = Thread(target=task_1, args=(2,))
    thread3 = Thread(target=task_2, args=(3,))
    # start the threads
    thread1.start()
    thread2.start()
    thread3.start()
    # wait for the threads to finish working
    thread1.join()
    thread2.join()
    thread3.join()
