import sys
from PyQt5.QtWidgets import (QDialog,
                             QApplication,
                             QPushButton,
                             QVBoxLayout,
                             QPushButton,
                             QGroupBox,
                             QComboBox)
from matplotlib import colors
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import random
from utilGui import Names


class Hist(QDialog):
    def __init__(self, parent=None):
        super(Hist, self).__init__(parent)

        self.parent = parent

        # a figure instance to plot on
        self.figure = plt.figure(figsize=(20, 30))

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        self.group_gb = QGroupBox("Select the chemical element:")

        self.item_cb = QComboBox()
        for i in range(len(Names.Chemical_Elemnts)):
            self.item_cb.addItem(Names.Chemical_Elemnts[i])
        self.item_cb.activated.connect(self.item_cb_activated)

        vbox = QVBoxLayout()
        vbox.addWidget(self.item_cb)
        vbox.addStretch(1)
        self.group_gb.setLayout(vbox)

        # set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.addWidget(self.group_gb)
        self.setLayout(layout)
        self.item_cb_activated(0)

        self.show()

    def item_cb_activated(self, value):
        print(Names.Chemical_Elemnts[value])
        # random data
        # data = [random.random() for i in range(10)]
        parent = self.parent
        colnames, rownames, matrix = parent.table_to_matrix(
            parent.result_tb, True)
        # instead of ax.hold(False)
        self.figure.clear()

        # create an axis
        ax = self.figure.add_subplot(1, 1, 1)

        ax.hist(matrix[value], bins=5, density=True)
        # ax.yaxis.set_major_formatter(PercentFormatter(xmax=1))

        # refresh canvas
        self.canvas.draw()
