import sys
from PyQt5.QtWidgets import (QDialog,
                             QApplication,
                             QPushButton,
                             QGridLayout,
                             QVBoxLayout,
                             QPushButton,
                             QGroupBox,
                             QComboBox,
                             QLabel,
                             QDoubleSpinBox,
                             QSpinBox)
from matplotlib import colors
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import random
from utilGui import Names
from util import Reader


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

        # delta
        self.sd_lb = QLabel("Standard Deviation:", self)
        self.sd_dsb = QDoubleSpinBox(self)
        self.sd_dsb.setDecimals(2)
        self.sd_dsb.setMaximum(1000)
        self.sd_dsb.setMinimum(0)
        self.sd_dsb.setSingleStep(5)
        self.sd_dsb.setValue(100)

        # number of samples
        self.sample_lb = QLabel("Sample amount:", self)
        self.sample_sb = QSpinBox(self)
        self.sample_sb.setMaximum(50000)
        self.sample_sb.setMinimum(0)
        self.sample_sb.setSingleStep(10)
        self.sample_sb.setValue(30000)

        layout = QGridLayout()
        # layout.setColumnStretch(1, 4)
        # layout.setColumnStretch(2, 4)
        layout.addWidget(self.item1_lb, 0, 0)
        layout.addWidget(self.item1_cb, 0, 1)
        layout.addWidget(self.item2_lb, 1, 0)
        layout.addWidget(self.item2_cb, 1, 1)
        layout.addWidget(self.sd_lb, 2, 0)
        layout.addWidget(self.sd_dsb, 2, 1)
        layout.addWidget(self.sample_lb, 3, 0)
        layout.addWidget(self.sample_sb, 3, 1)
        self.group_gb.setLayout(layout)

        # set the layout
        layout = QVBoxLayout()
        # layout.setStretch(1, 10)
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.addWidget(self.group_gb)
        self.setLayout(layout)

        self.matrix_real = self.get_from_real_data()
        self.item_cb_activated(0)

        self.show()

    def get_from_real_data(self):

        size_vector = 45
        index_target = 45
        index_predicted_target = 47

        r = Reader()
        data = r.get_data('../data/traindata.csv')

        sd = self.sd_dsb.value()
        TG = self.parent.tg_dsb.value()
        data2 = []

        for i in range(len(data)):
            row = []
            for j in range(size_vector):
                row.append(data[i][j])
                data2.append(row)
                vectors = []

        for i in range(len(data)):
            TG_data = data[i][index_target]
            if TG - sd <= TG_data <= TG + sd:
                vectors.append(data2[i])
            if len(vectors) == self.sample_sb.value():
                break
        print(len(vectors))
        return vectors

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

        x_opt = value_1
        y_opt = value_2
        x_real = [row[self.item1_cb.currentIndex()]
                  for row in self.matrix_real]
        y_real = [row[self.item2_cb.currentIndex()]
                  for row in self.matrix_real]
        print(len(x_real))
        print(len(y_real))
        ax.scatter(x_real, y_real, c='r', s=15,
                   marker='s', alpha=0.5, label='Real')
        ax.scatter(x_opt, y_opt, c='b', s=15,
                   marker='o', alpha=0.5, label='Opt')
        ax.set_title('Scatter Plot', fontsize=12)
        plt.xlabel(name_1, fontsize=12)
        plt.ylabel(name_2, fontsize=12)
        ax.legend()
        # plt.legend()
        # refresh canvas
        self.canvas.draw()
