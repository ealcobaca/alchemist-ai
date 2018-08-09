#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, traceback, re, csv
import numpy as np
from PyQt5.QtWidgets import (QApplication,
                             QMainWindow,
                             QTableWidgetItem,
                             QProgressBar,
                             QFileDialog,
                             QAction,
                             QMenu)
from PyQt5.QtGui import QFont, QColor, QIcon
from gui import Ui_main_window
sys.path.append("../")  # Adds higher directory to python modules path.
from optpool import AnnealingGlass
from optpool import PSO
from optpool import RandomOpt
from optpool import Optimizer
from PyQt5.QtCore import Qt
from utilGui import Names
from .hist import Hist
from .scatter import ScatterPlot

from sklearn.ensemble import RandomForestRegressor
from util import Reader


class App(QMainWindow, Ui_main_window):
    def __init__(self):
        # super(QMainWindow, self).__init__()
        QMainWindow.__init__(self)
        # Set up the user interface from designer
        self.setupUi(self)

        #Train RF
        self.usa_RF = False
        self.model_rf = None
        if self.usa_RF:
            self.init_clf()

        # Make some local modification ...
        self.tb_item = None
        self.progress = QProgressBar(self)
        self.progress.setGeometry(20, 800, 640, 20)
        self.progress.setHidden(True)

        self.menu_glass = self.menubar.addMenu('Glass G.')
        menu_open_result = QAction(QIcon(), '&Open Result', self)
        menu_open_result.setShortcut('Ctrl+R')
        menu_open_result.setStatusTip(
            'Open a csv result file')
        menu_open_result.triggered.connect(self.menu_open_result)
        self.menu_glass.addAction(menu_open_result)
        # Visualization menubar

        # Create vis action
        self.menu_vis = QMenu("Visualization", self)
        self.menubar.addMenu(self.menu_vis)
        menu_vis_hist = QAction(QIcon(), '&Hist', self)
        menu_vis_hist.setShortcut('Ctrl+H')
        menu_vis_hist.setStatusTip(
            'Apply histogram in each results column')
        menu_vis_hist.triggered.connect(self.menu_vis_hist)
        self.menu_vis.addAction(menu_vis_hist)

        menu_vis_scatter = QAction(QIcon(), '&Scatter Plot', self)
        menu_vis_scatter.setShortcut('Ctrl+M')
        menu_vis_scatter.setStatusTip(
            'Apply scatter plot in each column')
        menu_vis_scatter.triggered.connect(self.menu_vis_scatter)
        self.menu_vis.addAction(menu_vis_scatter)

        self.menu_help = self.menubar.addMenu('Options')
        self.menu_help = self.menubar.addMenu('Help')
        self.menu_exit = self.menubar.addMenu('Exit')

        # Connect up the buttons
        self.run_btn.clicked.connect(self.run_btn_clicked)
        self.min_max_table.itemChanged.connect(self.min_max_table_itemChanged)
        self.min_max_table.itemDoubleClicked.connect(
            self.min_max_table_itemDoubleClicked)
        self.discard_btn.clicked.connect(self.discard_btn_clicked)
        self.clean_all_btn.clicked.connect(self.clean_all_btn_clicked)
        self.save_btn.clicked.connect(self.save_btn_clicked)
        self.clean_all_btn_clicked()
        self.show()

    def menu_open_result(self):
        print("Menu open result")
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(
            self,
            "QFileDialog.getOpenFileName()",
            "",
            "csv Files (*.csv);;All Files (*)",
            options=options)
        if fileName:
            print(fileName)
            with open(fileName, "r") as file:
                reader = csv.reader(file, delimiter=",")
                x = list(reader)
                self.discard_btn_clicked()
                for i in range(1, len(x)):
                    self.add_result_tb(x[i])

    def menu_vis_scatter(self):
        print("Scatter plot")
        ScatterPlot(parent=self)

    def menu_vis_hist(self):
        print("Hist")
        Hist(parent=self)

    def save_btn_clicked(self):
        print("Saving")
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(
            self,
            "QFileDialog.getSaveFileName()",
            "",
            "All Files (*);;csv Files (*.csv)", options=options)
        if fileName:
            with open(fileName, 'w') as file:
                file.write(self.results_to_csv())
            print(fileName)

    def clean_all_btn_clicked(self):
        self.discard_btn_clicked()
        #self.tg_dsb.setValue(700)
        self.tg_dsb.setValue(1100)
        #self.amount_sp.setValue(1)
        self.amount_sp.setValue(3)
        self.opt_cb.setCurrentIndex(1)
        for i in range(len(Names.Chemical_Compounds)):
            for j in range(2):
                self.min_max_table.setItem(
                    i, j, QTableWidgetItem("0.0"))
        self.min_max_table.setItem(
                    1, 1, QTableWidgetItem("1.0"))
        self.min_max_table.setItem(
                    55, 1, QTableWidgetItem("1.0"))
        self.min_max_table.setItem(
                    56, 1, QTableWidgetItem("1.0"))

    def discard_btn_clicked(self):
        print("Discard")
        self.result_tb.clear()
        #self.result_tb.setColumnCount(46)
        self.result_tb.setColumnCount(len(Names.Chemical_Compounds)+1)
        self.result_tb.setRowCount(0)

        #for i in range(len(Names.Chemical_Elemnts)):
        #    item = QTableWidgetItem(Names.Chemical_Elemnts[i])
        for i in range(len(Names.Chemical_Compounds)):
            item = QTableWidgetItem(Names.Chemical_Compounds[i])
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
        self.progress.setValue(0)

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
    def table_to_matrix(tb, flag=False):
        matrix = []
        if flag:
            for i in range(tb.columnCount()):
                mcol = []
                for j in range(tb.rowCount()):
                    item = tb.item(j, i)
                    mcol.append(float(item.text()))
                matrix.append(mcol)
        else:
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

    def results_to_csv(self):
        csv = ""
        for j in range(self.result_tb.columnCount()):
            item = self.result_tb.horizontalHeaderItem(j)
            if j == (self.result_tb.columnCount()-1):
                csv = csv + item.text() + "\n"
            else:
                csv = csv + item.text() + ","

        for i in range(self.result_tb.rowCount()):
            for j in range(self.result_tb.columnCount()):
                item = self.result_tb.item(i, j)
                if j == (self.result_tb.columnCount()-1):
                    csv = csv + item.text() + "\n"
                else:
                    csv = csv + item.text() + ","
        return csv

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

    def sort_result_tb(self, matrix):
        n_col = len(matrix[0])
        matrix_sorted = sorted(matrix,key=lambda x: x[n_col-1])
        #print([m[n_col-1] for m in matrix_sorted])
        #print(matrix)
        matrix_reduced = []
        self.discard_btn_clicked()
        for m in matrix_sorted:
            m_reduced = m[0:n_col-1]
            matrix_reduced.append(m_reduced)
            #print(m_reduced)
            self.add_result_tb(m_reduced)        


    def random(self):
        print("Running Random")
        amount = self.amount_sp.value()
        tg = self.to_normalized_tg(self.tg_dsb.value())
        results = []
        _, _, matrix = self.table_to_matrix(self.min_max_table)
        matrix = Optimizer.matrix_to_dic(matrix)
        completed = 0
        perc = 100/amount
        self.progress.setValue(completed)
        self.progress.setHidden(False)
        for i in range(amount):
            tsp = RandomOpt(tg=tg, min_max_dic=matrix, path="../models/ANN.h5")
            result = tsp.run()
            print()
            pred = result.get_result()[0]
            print(result.get_result()[0])
            vector = result.get_result()[2].copy()
            vector = Optimizer.dic_to_vector(vector)
            print(vector)
            print(sum(vector))
            erro = result.get_result()[1]
            print(erro)
            vector.append(self.to_real_tg(pred))
            self.add_result_tb(vector)
            results.append(result)

            completed += perc
            self.progress.setValue(completed)
        self.progress.setHidden(True)

    def annealing(self):
        print("Running Annealing")
        amount = self.amount_sp.value()
        tg = self.to_normalized_tg(self.tg_dsb.value())
        results = []
        _, _, matrix = self.table_to_matrix(self.min_max_table)
        matrix = Optimizer.matrix_to_dic(matrix)
        completed = 0
        perc = 100/amount
        self.progress.setValue(completed)
        self.progress.setHidden(False)
        matrix_results = []
        for i in range(amount):
            tsp = AnnealingGlass(tg=tg, min_max_dic=matrix,
                                 save_preds=True, save_states=True,
                                 path="../models/ANN.h5")
            result = tsp.run()
            print()
            pred = result.get_result()[0]
            print(result.get_result()[0])
            vector = result.get_result()[2].copy()
            #vector = Optimizer.dic_to_vector(vector)
            vector = Optimizer.dic_to_vector_compound(vector)
            print(vector)
            print(sum(vector))
            erro = result.get_result()[1]
            print(erro)
            vector.append(self.to_real_tg(pred))
            self.add_result_tb(vector)
            results.append(result)

            vector2 = vector
            vector2.append(erro)
            matrix_results.append(vector2)

            completed += perc
            self.progress.setValue(completed)
        self.sort_result_tb(matrix_results)
        self.progress.setHidden(True)

    def pso(self):
        print("Running PSO")
        amount = self.amount_sp.value()
        tg = self.to_normalized_tg(self.tg_dsb.value())
        _, _, mM = self.table_to_matrix(self.min_max_table)
        mM = Optimizer.matrix_to_dic(mM)
        print(mM)
        completed = 0
        perc = 100/amount

        self.progress.setHidden(False)
        self.progress.setValue(completed)

        matrix = []

        for i in range(amount):
            completed += perc
            self.progress.setValue(completed)

            initialVectors = [np.random.rand(len(mM)).tolist()]
            pso = PSO(
                sizeVector=len(mM),
                max_min_comp=mM,
                target=tg,
                path="../models/ANN.h5",
                clf=self.model_rf)
            result = pso.run()
            results = result.get_result()
            solucoes = results[0]
            valores = results[1]
            erros = results[2]

            vector = solucoes[0]
            vector.append(self.to_real_tg(valores[0]))            
            self.add_result_tb(vector)
            vector2 = vector
            vector2.append(erros[0])
            matrix.append(vector2)

            #print(solucoes)
            #print(erros)
            #print(self.to_real_tg(valores[0]))
        self.sort_result_tb(matrix)
        self.progress.setHidden(True)

    def to_normalized_tg(self, tg):
        return tg/1452.0

    def to_real_tg(self, tg):
        return tg * 1452.0

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
            tg = self.to_normalized_tg(self.tg_dsb.value())
            print("Optimizer: {0:s}".format(opt))
            print("Amount: {0:d}".format(amount))
            print("Tg: {0:6f}".format(tg))

            # chamada para a API
            print()
            if opt == "Annealing":
                self.annealing()
            elif opt == "PSO":
                self.pso()
            elif opt == "Random":
                print("calling")
                self.random()

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

    def init_clf(self):
        r = Reader()
        #file_name = "C:/Users/Bruno Pimentel/Downloads/Glass/data/traindata.csv"
        file_name = "/home/bruno/Projetos/Glass-Generator/data/traindata.csv"
        data = r.get_data(file_name)
        data_train = []
        data_target = []
        for d in data:
            data_train.append(d[0:(len(data[0])-4)])
            data_target.append(d[len(data[0])-3])
        clf = RandomForestRegressor(n_estimators= 100, min_samples_leaf=1, max_depth=1000, random_state=0)
        print('Treinando RF...')
        self.model_rf = clf.fit(data_train, data_target)
        #predictions = clf.predict(X_test)

