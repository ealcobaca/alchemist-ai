# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/GG_add.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_add_ww(object):
    def setupUi(self, add_ww):
        add_ww.setObjectName("add_ww")
        add_ww.resize(393, 218)
        self.che_elem_label = QtWidgets.QLabel(add_ww)
        self.che_elem_label.setGeometry(QtCore.QRect(20, 20, 191, 22))
        self.che_elem_label.setObjectName("che_elem_label")
        self.chem_elem_cb = QtWidgets.QComboBox(add_ww)
        self.chem_elem_cb.setGeometry(QtCore.QRect(230, 20, 141, 30))
        self.chem_elem_cb.setObjectName("chem_elem_cb")
        self.che_elem_label_2 = QtWidgets.QLabel(add_ww)
        self.che_elem_label_2.setGeometry(QtCore.QRect(20, 70, 191, 22))
        self.che_elem_label_2.setObjectName("che_elem_label_2")
        self.che_elem_label_3 = QtWidgets.QLabel(add_ww)
        self.che_elem_label_3.setGeometry(QtCore.QRect(20, 120, 191, 22))
        self.che_elem_label_3.setObjectName("che_elem_label_3")
        self.min_dsb = QtWidgets.QDoubleSpinBox(add_ww)
        self.min_dsb.setGeometry(QtCore.QRect(230, 70, 141, 31))
        self.min_dsb.setDecimals(6)
        self.min_dsb.setSingleStep(0.01)
        self.min_dsb.setObjectName("min_dsb")
        self.max_dsb = QtWidgets.QDoubleSpinBox(add_ww)
        self.max_dsb.setGeometry(QtCore.QRect(230, 120, 141, 31))
        self.max_dsb.setDecimals(6)
        self.max_dsb.setSingleStep(0.01)
        self.max_dsb.setObjectName("max_dsb")
        self.add_bb = QtWidgets.QDialogButtonBox(add_ww)
        self.add_bb.setGeometry(QtCore.QRect(190, 180, 183, 30))
        self.add_bb.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.add_bb.setObjectName("add_bb")

        self.retranslateUi(add_ww)
        QtCore.QMetaObject.connectSlotsByName(add_ww)

    def retranslateUi(self, add_ww):
        _translate = QtCore.QCoreApplication.translate
        add_ww.setWindowTitle(_translate("add_ww", "Add - GG"))
        self.che_elem_label.setText(_translate("add_ww", "Chemical element:"))
        self.che_elem_label_2.setText(_translate("add_ww", "Min:"))
        self.che_elem_label_3.setText(_translate("add_ww", "Max:"))

