# Created by ioluwayo on 2018-07-08.
from matplotlib import pyplot
import numpy as np

def profile2(results):
    start,stop = np.array(results).T
    start.astype(float)
    stop.astype(float)
    pyplot.barh(range(len(start)), stop-start, left=start)
    pyplot.grid(axis='x')
    pyplot.ylabel("Tasks")
    pyplot.xlabel("Seconds")
    print(stop[-1]-start[0])
    pyplot.show()

def profile(starts, stops):
    elapsed = [s2-s1 for s1, s2 in zip(starts, stops)]
    lefts = [0]

    for i in range(1,len(elapsed)):
        lefts.append(starts[i]-min(starts))
    print(starts)
    print(stops)

    # lefts = elapsed.copy()
    # lefts.pop()
    # lefts.insert(0,0)
    print(elapsed)
    print(lefts)
    pyplot.barh(range(len(starts)), elapsed)
    # pyplot.xlim(0,max(elapsed))
    pyplot.grid(axis="both")
    pyplot.ylabel("Tasks")
    pyplot.xlabel("Seconds")
    # print('Total duration: ', stops[-1]-starts[0])
    pyplot.show()