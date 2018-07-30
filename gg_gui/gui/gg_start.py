# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/GG_start.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from utilGui import Names

class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(684, 828)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")

        # run_btn
        self.run_btn = QtWidgets.QPushButton(self.centralwidget)
        self.run_btn.setText("Run")
        self.run_btn.setGeometry(QtCore.QRect(510, 20, 121, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.run_btn.setFont(font)
        self.run_btn.setStyleSheet("border-color: rgb(114, 159, 207);\n"
"background-color: rgb(78, 154, 6);")
        self.run_btn.setObjectName("run_btn")

        # min_max table
        self.min_max_table = QtWidgets.QTableWidget(self.centralwidget)
        self.min_max_table.setGeometry(QtCore.QRect(20, 100, 421, 192))
        self.min_max_table.setObjectName("min_max_table")
        self.min_max_table.setColumnCount(2)
        self.min_max_table.setRowCount(len(Names.Chemical_Compounds))

        for i in range(len(Names.Chemical_Compounds)):
            item = QtWidgets.QTableWidgetItem(Names.Chemical_Compounds[i])
            self.min_max_table.setVerticalHeaderItem(i, item)

        item = QtWidgets.QTableWidgetItem("min")
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        item.setFont(font)
        item.setBackground(QtGui.QColor(114, 159, 207))
        self.min_max_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem("max")
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        item.setFont(font)
        item.setBackground(QtGui.QColor(114, 159, 207))
        self.min_max_table.setHorizontalHeaderItem(1, item)

        for i in range(len(Names.Chemical_Compounds)):
            self.min_max_table.setItem(
                i, 0, QtWidgets.QTableWidgetItem("0.0"))
            self.min_max_table.setItem(
                i, 1, QtWidgets.QTableWidgetItem("1.0"))
        self.min_max_label = QtWidgets.QLabel(self.centralwidget)
        self.min_max_label.setGeometry(QtCore.QRect(20, 70, 421, 22))
        self.min_max_label.setObjectName("min_max_label")
        self.min_max_label.setText("Search space limitation:")

        # opt_label
        self.opt_label = QtWidgets.QLabel(self.centralwidget)
        self.opt_label.setGeometry(QtCore.QRect(460, 100, 201, 22))
        self.opt_label.setObjectName("opt_label")
        self.opt_label.setText("Optimizer")

        # amount
        self.amount_sp = QtWidgets.QSpinBox(self.centralwidget)
        self.amount_sp.setGeometry(QtCore.QRect(460, 270, 201, 31))
        self.amount_sp.setMinimum(1)
        self.amount_sp.setMaximum(10000)
        self.amount_sp.setValue(1)
        self.amount_sp.setObjectName("amount_sp")
        self.amount_label = QtWidgets.QLabel(self.centralwidget)
        self.amount_label.setGeometry(QtCore.QRect(460, 240, 201, 22))
        self.amount_label.setObjectName("amount_label")
        self.amount_label.setText("Amount:")

        # tg
        self.tg_dsb = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.tg_dsb.setGeometry(QtCore.QRect(460, 200, 201, 31))
        self.tg_dsb.setMaximum(50000)
        self.tg_dsb.setMinimum(0)
        self.tg_dsb.setDecimals(0)
        self.tg_dsb.setSingleStep(5)
        self.tg_dsb.setObjectName("tg_dsb")
        self.tg_dsb.setValue(700)
        self.tg_label = QtWidgets.QLabel(self.centralwidget)
        self.tg_label.setGeometry(QtCore.QRect(460, 170, 201, 22))
        self.tg_label.setObjectName("tg_label")
        self.tg_label.setText("TG:")

        # opt_cb
        self.opt_cb = QtWidgets.QComboBox(self.centralwidget)
        self.opt_cb.setGeometry(QtCore.QRect(460, 130, 201, 30))
        self.opt_cb.setObjectName("opt_cb")
        self.opt_cb.addItem("Annealing")
        self.opt_cb.addItem("PSO")
        self.opt_cb.addItem("Random")

        # result_tb
        self.result_label = QtWidgets.QLabel(self.centralwidget)
        self.result_label.setGeometry(QtCore.QRect(20, 350, 641, 22))
        self.result_label.setObjectName("result_label")
        self.result_label.setText("Results:")
        self.result_tb = QtWidgets.QTableWidget(self.centralwidget)
        self.result_tb.setGeometry(QtCore.QRect(20, 380, 641, 341))
        self.result_tb.setObjectName("result_table")
        self.result_tb.setColumnCount(46)
        # self.result_tb.setRowCount(1)

        for i in range(len(Names.Chemical_Elemnts)):
            item = QtWidgets.QTableWidgetItem(Names.Chemical_Elemnts[i])
            self.result_tb.setHorizontalHeaderItem(i, item)
            font = QtGui.QFont()
            font.setItalic(True)
            item.setFont(font)
            item.setBackground(QtGui.QColor(114, 159, 207))

        item = QtWidgets.QTableWidgetItem("TG")
        self.result_tb.setHorizontalHeaderItem(i+1, item)
        font = QtGui.QFont()
        font.setItalic(True)
        item.setFont(font)
        item.setBackground(QtGui.QColor(114, 159, 207))

        # discard_btn
        self.discard_btn = QtWidgets.QPushButton(self.centralwidget)
        self.discard_btn.setText("Discard")
        self.discard_btn.setGeometry(QtCore.QRect(540, 730, 122, 30))
        self.discard_btn.setObjectName("discard_btn")

        # save_btn
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setText("Save")
        self.save_btn.setGeometry(QtCore.QRect(400, 730, 122, 30))
        self.save_btn.setToolTip("")
        self.save_btn.setObjectName("save_btn")

        # clean_all_btn
        self.clean_all_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clean_all_btn.setGeometry(QtCore.QRect(20, 730, 122, 30))
        self.clean_all_btn.setObjectName("clean_all_btn")
        self.clean_all_btn.setText("Clan All")

        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 684, 27))
        self.menubar.setObjectName("menubar")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)
