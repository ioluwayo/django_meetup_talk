# Created by ioluwayo on 2018-07-08.
import time
import wikipedia
from matplotlib import pyplot as plt


def profile(starts, stops):
    elapsed = [s2-s1 for s1, s2 in zip(starts, stops)]
    lefts = [0]

    for i in range(1,len(elapsed)):
        lefts.append(elapsed[i-1]+lefts[i-1])

    plt.barh(range(len(starts)), elapsed, left=lefts)
    plt.xlim(0,sum(elapsed))
    plt.grid(axis="both")
    plt.ylabel("Tasks")
    plt.xlabel("Seconds")
    print('Total duration: ', stops[-1]-starts[0])
    plt.show()



if __name__ == '__main__':
    cities = ['Lagos', 'London', 'Manchester', 'Paris', 'Shanghai','Ife', 'Toronto', 'Boston', 'Munich','Monaco',
              'Seattle', 'Athens', 'Dundee', 'Lisbon', 'Tokyo']
    summaries = []
    starts = []
    stops = []
    s = time.time()
    for city in cities:
        starts.append(time.time())
        summaries.append(wikipedia.summary(city))
        stops.append(time.time())

    for summary in summaries:
        print(summary)
    print('emm:',time.time()-s)
    profile(starts, stops)