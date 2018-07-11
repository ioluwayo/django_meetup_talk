# Created by ioluwayo on 2018-07-08.
import time
import wikipedia
from visualize import profile_series

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
    profile_series(starts, stops)
