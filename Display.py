from matplotlib import pyplot


def profile(starts_stops, title=''):
    """

    :param List starts_stops: List of tuples of form (start , stop) times
    :param str title: Title for plot
    :return:
    """
    start_times = [start_stop[0] for start_stop in starts_stops]
    stop_times = [start_stop[1] for start_stop in starts_stops]
    elapsed = [stop - start for start, stop in zip(start_times, stop_times)]

    lefts = []
    for j in range(len(elapsed)):
        lefts.append(start_times[j] - min(start_times))

    pyplot.barh(range(len(start_times)), elapsed, left=lefts)
    pyplot.grid(axis="both")
    pyplot.ylabel("Threads")
    pyplot.xlabel("Seconds")
    pyplot.title(title)

    print('Individual durations: ', elapsed)
    print("Fastest thread: ", min(elapsed))
    print("Slowest thread: ", max(elapsed))
    print('Total duration: ', max(elapsed))

    pyplot.show()
