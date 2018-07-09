# threads tasks that release the GIL. blocking io like api calls
import wikipedia
import time
from matplotlib import pyplot
import numpy as np
# def profile(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         return func(*args, **kwargs), time.time() - start
#
#     return wrapper

def profile(starts, stops):
    elapsed = [s2-s1 for s1, s2 in zip(starts, stops)]
    lefts=[]

    for i in range(len(elapsed)):
        lefts.append(starts[i]-min(starts))
    pyplot.barh(range(len(starts)), elapsed, left=lefts)
    # pyplot.xlim(0,1.5*(max(stops)-min(starts)))
    pyplot.grid(axis="both")
    pyplot.ylabel("Tasks")
    pyplot.xlabel("Seconds")
    print('Individual durations: ', elapsed)
    print('Total duration (max): ', max(elapsed))

    pyplot.show()

def get_city_summary(city, result, durations, index):
    start = time.time()
    result[index] = wikipedia.summary(city)
    stop = time.time()
    durations[index] = (start,stop)

def with_threads(cities):
    import threading
    threads = []
    results = [0 for i in range(len(cities))]
    durations = [0 for i in range(len(cities))]
    i = 0
    for city in cities:
        th = threading.Thread(target=get_city_summary, args=(city, results, durations, i))
        th.start()
        threads.append(th)
        i+=1

    for t in threads:
        t.join()
    return results, durations


if __name__ == '__main__':
    cities = ['Lagos', 'London', 'Manchester', 'Paris', 'Shanghai','Ife', 'Toronto', 'Boston', 'Munich','Monaco',
              'Seattle', 'Athens', 'Dundee', 'Lisbon', 'Tokyo']
    cities = cities
    summaries, start_stop = with_threads(cities[:7])

    for summary in summaries:
        print(summary)

    starts = [d[0] for d in start_stop]
    stops = [d[1] for d in start_stop]
    profile(starts, stops)
