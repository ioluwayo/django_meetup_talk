# threads tasks that release the GIL. blocking io like api calls
import wikipedia
import time
import threading
from Display import profile


def get_city_summary(query_city, results_list, durations_list, index):
    start = time.time()
    results_list[index] = wikipedia.summary(query_city)
    stop = time.time()
    durations_list[index] = (start, stop)


if __name__ == '__main__':
    cities = ['Lagos', 'London', 'Manchester', 'Paris', 'Shanghai', 'Ife', 'Toronto', 'Boston', 'Munich', 'Monaco',
              'Seattle', 'Athens', 'Dundee', 'Lisbon', 'Tokyo']
    # cities.extend(cities)
    # cities.extend(cities)
    # cities.extend(cities)

    threads = []
    summaries = [0 for _ in range(len(cities))]  # shared memory space between threads
    durations = [0 for _ in range(len(cities))]

    for i in range(len(cities)):  # unbounded number of threads.
        thread = threading.Thread(target=get_city_summary, args=(cities[i], summaries, durations, i))
        thread.start()
        threads.append(thread)

    for t in threads:
        t.join()  # wait for each thread to finish

    for summary in summaries:
        print(summary)

    profile(starts_stops=durations, title="Blocking IO with Threads (Parallel)")
