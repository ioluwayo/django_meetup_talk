import threading
import wikipedia
from queue import Queue, Empty
from time import time
from visualize import profile

THREAD_POOL_SIZE = 10  # threads will continue to pick up work from the que until its empty.
job_que = Queue()
result_que = Queue()
durations_que = Queue()


def worker():
    start = time()  # we are timing each thread. Not each job
    stop = time()
    while not job_que.empty():  # if the que is not empty. pick up the next job
        try:  # still need to catch Empty Exception...another thread could take over control before retrieving item
            job = job_que.get()
        except Empty:
            break  # no more jobs to process since que is empty
        else:
            result_que.put(wikipedia.summary(job))  # GIL is released while waiting.
            job_que.task_done()
            stop = time()  # stop time is when the last job was processed by this thread

    durations_que.put((start, stop))


if __name__ == '__main__':
    cities = ['Lagos', 'London', 'Manchester', 'Paris', 'Shanghai', 'Ife', 'Toronto', 'Boston', 'Munich', 'Monaco',
              'Seattle', 'Athens', 'Dundee', 'Lisbon', 'Tokyo']
    # cities.extend(cities)
    # cities.extend(cities)
    # cities.extend(cities)

    threads = []
    for city in cities:
        job_que.put(city)

    for i in range(THREAD_POOL_SIZE):
        thread = threading.Thread(target=worker)
        thread.start()
        threads.append(thread)

    job_que.join()  # wait until all cities have been removed from the que.

    for thread in threads:
        thread.join()  # wait for thread to finish processing job

    while not result_que.empty():
        print()
        print(result_que.get())

    durations = []
    while not durations_que.empty():
        durations.append(durations_que.get())  # earlier threads are most likely to pick up extra jobs

    profile(starts_stops=durations, title='Blocking IO with Thread pools')
