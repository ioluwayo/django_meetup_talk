from matplotlib import pyplot


def profile(starts_stops, title='', labels=[], colors=[]):
    """
    :param labels:
    :param colors:
    :param List starts_stops: List of tuples of form (start , stop) times
    :param str title: Title for plot
    :return:
    """
    if len(colors) < len(starts_stops):
        colors = None
    if len(labels) < len(starts_stops):
        labels = None

    start_times = [start_stop[0] for start_stop in starts_stops]
    stop_times = [start_stop[1] for start_stop in starts_stops]
    elapsed = [stop - start for start, stop in zip(start_times, stop_times)]

    lefts = []
    for j in range(len(elapsed)):
        lefts.append(start_times[j] - min(start_times))

    pyplot.barh(range(len(start_times)), elapsed, left=lefts, color=colors, tick_label=labels)

    pyplot.grid(axis="both")
    pyplot.ylabel("Task(s)")
    pyplot.xlabel("Seconds")
    pyplot.title(title)

    print('Individual durations: ', elapsed)
    print("Fastest: ", min(elapsed))
    print("Slowest: ", max(elapsed))

    pyplot.show()


def profile_series(start_times, stop_times, title="Blocking IO in series)"):
    elapsed = [s2 - s1 for s1, s2 in zip(start_times, stop_times)]

    lefts = [0]
    for i in range(1, len(elapsed)):
        lefts.append(elapsed[i - 1] + lefts[i - 1])

    pyplot.barh(range(1, len(start_times) + 1), elapsed, left=lefts)
    pyplot.xlim(0, sum(elapsed))
    pyplot.grid(axis="both")
    pyplot.ylabel("Tasks")
    pyplot.xlabel("Seconds")
    pyplot.title(title)
    print("Individual durations:", elapsed)
    print("Fastest: ", min(elapsed))
    print("Slowest: ", max(elapsed))
    print('Total duration: ', stop_times[-1] - start_times[0])
    pyplot.show()
