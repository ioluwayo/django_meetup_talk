# spin up processes
from multiprocessing import Process
import os


def task(*args):
    print("Process PID {} , arguments {}".format(os.getpid(), args))


if __name__ == '__main__':
    processes = []
    for i in range(1, 5):
        process = Process(target=task, args=(i, i*i,))
        process.start()
        processes.append(process)
    for process in processes:
        process.join()
