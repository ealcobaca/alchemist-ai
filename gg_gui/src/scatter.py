import sys
from PyQt5.QtWidgets import (QDialog,
                             QApplication,
                             QPushButton,
                             QVBoxLayout,
                             QPushButton,
                             QGroupBox,
                             QComboBox,
                             QLabel)
from matplotlib import colors
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import random
from utilGui import Names


class ScatterPlot(QDialog):
    def __init__(self, parent=None):
        super(ScatterPlot, self).__init__(parent)

        self.parent = parent

        # a figure instance to plot on
        # self.figure = plt.figure()
        self.figure = plt.figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)
        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        self.group_gb = QGroupBox("Options")

        # first chemical elemnt
        self.item1_lb = QLabel("Select the first chemical elemnt:", self)
        self.item1_cb = QComboBox()
        for i in range(len(Names.Chemical_Elemnts)):
            self.item1_cb.addItem(Names.Chemical_Elemnts[i])
        self.item1_cb.activated.connect(self.item_cb_activated)

        # second chemical element
        self.item2_lb = QLabel("Select the second chemical elemnt:", self)
        self.item2_cb = QComboBox()
        for i in range(len(Names.Chemical_Elemnts)):
            self.item2_cb.addItem(Names.Chemical_Elemnts[i])
        self.item2_cb.activated.connect(self.item_cb_activated)

        vbox = QVBoxLayout()
        vbox.addWidget(self.item1_lb)
        vbox.addWidget(self.item1_cb)
        vbox.addWidget(self.item2_lb)
        vbox.addWidget(self.item2_cb)
        vbox.addStretch(1)
        self.group_gb.setLayout(vbox)

        # set the layout
        layout = QVBoxLayout()
        # layout.setStretch(1, 10)
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.addWidget(self.group_gb)
        self.setLayout(layout)
        self.item_cb_activated(0)

        self.show()

    def item_cb_activated(self, value):
        print(Names.Chemical_Elemnts[self.item1_cb.currentIndex()])
        print(Names.Chemical_Elemnts[self.item2_cb.currentIndex()])

        # random data
        # data = [random.random() for i in range(10)]
        parent = self.parent
        colnames, rownames, matrix = parent.table_to_matrix(
            parent.result_tb, True)
        # instead of ax.hold(False)
        self.figure.clear()

        # create an axis
        ax = self.figure.add_subplot(1, 1, 1)

        value_1 = matrix[self.item1_cb.currentIndex()]
        value_2 = matrix[self.item2_cb.currentIndex()]
        name_1 = Names.Chemical_Elemnts[self.item1_cb.currentIndex()]
        name_2 = Names.Chemical_Elemnts[self.item2_cb.currentIndex()]

        x_real = value_1
        y_real = value_2
        ax.scatter(x_real, y_real, c='r', s=15,
                   marker='s', alpha=0.5, label='Real')
        ax.set_title('Scatter Plot', fontsize=12)
        plt.xlabel(name_1, fontsize=12)
        plt.ylabel(name_2, fontsize=12)
        ax.legend()

        # plt.legend()
        # refresh canvas
        self.canvas.draw()
