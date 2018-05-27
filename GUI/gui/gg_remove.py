# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/GG_remove.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_remove_ww(object):
    def setupUi(self, remove_ww):
        remove_ww.setObjectName("remove_ww")
        remove_ww.resize(391, 216)
        self.chem_elem_cb = QtWidgets.QComboBox(remove_ww)
        self.chem_elem_cb.setGeometry(QtCore.QRect(230, 20, 141, 30))
        self.chem_elem_cb.setObjectName("chem_elem_cb")
        self.che_elem_label = QtWidgets.QLabel(remove_ww)
        self.che_elem_label.setGeometry(QtCore.QRect(20, 20, 191, 22))
        self.che_elem_label.setObjectName("che_elem_label")
        self.remove_bb = QtWidgets.QDialogButtonBox(remove_ww)
        self.remove_bb.setGeometry(QtCore.QRect(190, 180, 183, 30))
        self.remove_bb.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.remove_bb.setObjectName("remove_bb")

        self.retranslateUi(remove_ww)
        QtCore.QMetaObject.connectSlotsByName(remove_ww)

    def retranslateUi(self, remove_ww):
        _translate = QtCore.QCoreApplication.translate
        remove_ww.setWindowTitle(_translate("remove_ww", "Remove - GG"))
        self.che_elem_label.setText(_translate("remove_ww", "Chemical element:"))

