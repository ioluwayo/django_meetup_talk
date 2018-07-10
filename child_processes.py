# Created by ioluwayo on 2018-07-07.
import subprocess
from time import time


def run_serial_processes(n):
    start = time()
    for _ in range(n):
        proc_1 = subprocess.Popen(['sleep', '0.1'])
        proc_1.communicate()
    print("{} processes in series took {} seconds".format(n, time() - start))


def run_parallel_processes(n):
    start = time()
    processes = []
    for _ in range(n):  # start all three processes upfront
        processes.append(subprocess.Popen(['sleep', '0.1']))
    for process in processes:  # wait for them to finish their io
        process.communicate()
    print("{} processes in series took {} seconds".format(n, time() - start))


if __name__ == '__main__':
    run_serial_processes(10)
    print()
    run_parallel_processes(10)
