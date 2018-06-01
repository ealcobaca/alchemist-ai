#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui import Ui_main_window
sys.path.append("../")  # Adds higher directory to python modules path.
from optpool import AnnealingGlass


class App(QMainWindow, Ui_main_window):
    def __init__(self):
        # super(QMainWindow, self).__init__()
        QMainWindow.__init__(self)
        # Set up the user interface from designer
        self.setupUi(self)

        # Make some local modification ...
        self.tb_item = None

        # Connect up the buttons
        self.run_btn.clicked.connect(self.run_btn_clicked)
        self.min_max_table.itemChanged.connect(self.min_max_table_itemChanged)
        self.min_max_table.itemDoubleClicked.connect(
            self.min_max_table_itemDoubleClicked)
        self.show()

    def min_max_table_itemChanged(self, item):
        col = item.column()
        print("[ItemChanged] item={0:s}, col={1:d}".format(
            item.text(), col))
        if re.match("^\d+?\.\d+?$", item.text()) is None:
            print("Not float")
            item.setText(self.tb_item.text())

    def min_max_table_itemDoubleClicked(self, item):
        col = item.column()
        print("[ItemDoubleClicked] item={0:s}, col={1:d}".format(
            item.text(), col))
        self.tb_item = item.clone()

    @staticmethod
    def table_to_matrix(tb):
        matrix = []
        for i in range(tb.rowCount()):
            mlin = []
            for j in range(tb.columnCount()):
                item = tb.item(i, j)
                mlin.append(float(item.text()))
            matrix.append(mlin)

        colnames = [tb.horizontalHeaderItem(i).text()
                    for i in range(tb.columnCount())]
        rownames = [tb.verticalHeaderItem(i).text()
                    for i in range(tb.rowCount())]

        return colnames, rownames, matrix

    def run_btn_clicked(self):
        """TODO: Docstring for run_btn_clicked.
        :returns: TODO

        """
        print("run\n")
        colnames, rownames, matrix = self.table_to_matrix(self.min_max_table)
        print(colnames)
        print(rownames)
        print(matrix)

        opt = self.opt_cb.currentText()
        amount = self.amount_sp.value()
        tg = self.tg_dsb.value()
        print("Optimizer: {0:s}".format(opt))
        print("Amount: {0:d}".format(amount))
        print("Tg: {0:6f}".format(tg))

        # chamada para a API
        restriction = [[0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0],
                       [0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0],
                       [0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0],
                       [0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0],
                       [0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0],
                       [0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0],
                       [0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0],
                       [0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0],
                       [0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0]]
        tsp = AnnealingGlass(tg=0.85, steps=5000, restriction=restriction,
                             save_preds=True, save_states=True, path="../models/ANN.h5")
        result = tsp.run()
        print()
        print(result.get_result()[0])
        print(len(result.get_result()[3]))
        print(len(result.get_result()[4]))



