import sys
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

import random

class Hist(QDialog):
    def __init__(self, parent=None):
        super(Hist, self).__init__(parent)

        self.parent = parent

        # a figure instance to plot on
        self.figure = plt.figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        self.plot()

        # set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        self.show()

    def plot(self):
        ''' plot some random stuff '''
        # random data
        data = [random.random() for i in range(10)]
        parent = self.parent
        colnames, rownames, matrix = parent.table_to_matrix(
            parent.result_tb, True)
        print(colnames)
        print(rownames)
        print(matrix)
        # instead of ax.hold(False)
        self.figure.clear()

        # create an axis
        fig, axs = plt.subplots(1, 45, sharey=True, tight_layout=True)
        # discards the old graph
        # ax.hold(False) # deprecated, see above

        # plot data
        # ax.plot(data, '*-')
        for i in range(len(axs)):
            axs[i].hist(matrix[i], bins=5)


        # refresh canvas
        self.canvas.draw()

