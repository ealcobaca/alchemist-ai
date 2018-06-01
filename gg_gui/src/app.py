#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, traceback
import re
from PyQt5.QtWidgets import (QApplication,
                             QMainWindow,
                             QTableWidgetItem)
from PyQt5.QtGui import QFont, QColor
from gui import Ui_main_window
sys.path.append("../")  # Adds higher directory to python modules path.
from optpool import AnnealingGlass
from PyQt5.QtCore import Qt
from utilGui import Names


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
        self.discard_btn.clicked.connect(self.discard_btn_clicked)
        self.clean_all_btn.clicked.connect(self.clean_all_btn_clicked)
        self.show()

    def clean_all_btn_clicked(self):
        self.discard_btn_clicked()
        self.tg_dsb.setValue(0.5)
        self.amount_sp.setValue(1)
        for i in range(len(Names.Chemical_Elemnts)):
            for j in range(2):
                self.min_max_table.setItem(
                    i, j, QTableWidgetItem("0.0"))
        self.opt_cb.setCurrentIndex(0)


    def discard_btn_clicked(self):
        print("Discard")
        self.result_tb.clear()
        self.result_tb.setColumnCount(46)
        self.result_tb.setRowCount(0)

        for i in range(len(Names.Chemical_Elemnts)):
            item = QTableWidgetItem(Names.Chemical_Elemnts[i])
            self.result_tb.setHorizontalHeaderItem(i, item)
            font = QFont()
            font.setItalic(True)
            item.setFont(font)
            item.setBackground(QColor(114, 159, 207))

        item = QTableWidgetItem("TG")
        self.result_tb.setHorizontalHeaderItem(i + 1, item)
        font = QFont()
        font.setItalic(True)
        item.setFont(font)
        item.setBackground(QColor(114, 159, 207))

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

    def add_result_tb(self, vector):
        print("Added")
        row = self.result_tb.rowCount()
        self.result_tb.insertRow(row)
        self.result_tb.setVerticalHeaderItem(
            row, QTableWidgetItem(str(row + 1)))
        for i in range(len(vector)):
            item = QTableWidgetItem()
            item.setText(str(vector[i]))
            item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.result_tb.setItem(
                row, i, item)

    def annealing(self):
        print("Running Annealing")
        amount = self.amount_sp.value()
        tg = self.tg_dsb.value()
        results = []
        _, _, matrix = self.table_to_matrix(self.min_max_table)
        for i in range(amount):
            tsp = AnnealingGlass(tg=tg, steps=1000, restriction=matrix,
                                 save_preds=True, save_states=True,
                                 path="../models/ANN.h5")
            result = tsp.run()
            print()
            pred = result.get_result()[0]
            print(result.get_result()[0])
            vector = result.get_result()[2].copy()
            vector.append(pred)
            self.add_result_tb(vector)
            results.append(result)

    def pso(self):
        print("Running SPO")

    def run_btn_clicked(self):
        """TODO: Docstring for run_btn_clicked.
        :returns: TODO

        """
        try:
            print("run\n")
            colnames, rownames, matrix = self.table_to_matrix(
                self.min_max_table)
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
            print()
            if opt == "Annealing":
                self.annealing()
            elif opt == "PSO":
                self.pso()

        except Exception as inst:
            print("\n#################### Error ####################")
            print(type(inst))    # the exception instance
            print(inst.args)     # arguments stored in .args
            print(inst)          # __str__ allows args to be printed directly,
            print("Exception in user code:")
            print("-"*60)
            traceback.print_exc(file=sys.stdout)
            print("-"*60)
            print("\n##############################################")

