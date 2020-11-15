from collections import OrderedDict

import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')


class Plotter:

    def __init__(self):
        plt.figure()

    def add_polygon(self, xs, ys):
        plt.fill(xs, ys, 'lightgray', label='Polygon')

    def add_point(self, x, y, kind=None):
        print("KIND", kind)
        for i in range(len(kind)):
            if kind[i] == "outside":
                plt.plot(x[i], y[i], "ro", label='Outside')
            elif kind[i] == "boundary":
                plt.plot(x[i], y[i], "bo", label='Boundary')
            elif kind[i] == "inside":
                plt.plot(x[i], y[i], "go", label='Inside')
            else:
                plt.plot(x[i], y[i], "ko", label='Unclassified')

    def show(self):
        handles, labels = plt.gca().get_legend_handles_labels()
        by_label = OrderedDict(zip(labels, handles))
        plt.legend(by_label.values(), by_label.keys())
        plt.xlabel("x coordinate")
        plt.ylabel("y coordinate")
        plt.show()

