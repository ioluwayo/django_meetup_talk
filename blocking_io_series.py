# Created by ioluwayo on 2018-07-08.
import time
import wikipedia
from matplotlib import pyplot


def profile(start_times, stop_times, title="Blocking IO in series)"):
    elapsed = [s2 - s1 for s1, s2 in zip(start_times, stop_times)]

    lefts = [0]
    for i in range(1, len(elapsed)):
        lefts.append(elapsed[i - 1] + lefts[i - 1])

    pyplot.barh(range(1, len(start_times) + 1), elapsed, left=lefts)
    pyplot.xlim(0, sum(elapsed))
    pyplot.grid(axis="both")
    pyplot.ylabel("Threads")
    pyplot.xlabel("Seconds")
    pyplot.title(title)
    print("Individual durations:", elapsed)
    print("Fastest response: ", min(elapsed))
    print("Slowest response: ", max(elapsed))
    print('Total duration: ', stop_times[-1] - start_times[0])
    pyplot.show()


if __name__ == '__main__':
    cities = ['Lagos', 'London', 'Manchester', 'Paris', 'Shanghai', 'Ife', 'Toronto', 'Boston', 'Munich', 'Monaco',
              'Seattle', 'Athens', 'Dundee', 'Lisbon', 'Tokyo']

    summaries = []
    starts = []
    stops = []

    for city in cities:
        starts.append(time.time())
        summaries.append(wikipedia.summary(city))
        stops.append(time.time())

    for summary in summaries:
        print(summary)
    profile(starts, stops)
