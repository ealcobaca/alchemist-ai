# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/GG_edit.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_edit_ww(object):
    def setupUi(self, edit_ww):
        edit_ww.setObjectName("edit_ww")
        edit_ww.resize(393, 216)
        self.max_dsb = QtWidgets.QDoubleSpinBox(edit_ww)
        self.max_dsb.setGeometry(QtCore.QRect(230, 120, 141, 31))
        self.max_dsb.setDecimals(6)
        self.max_dsb.setSingleStep(0.01)
        self.max_dsb.setObjectName("max_dsb")
        self.chem_elem_cb = QtWidgets.QComboBox(edit_ww)
        self.chem_elem_cb.setGeometry(QtCore.QRect(230, 20, 141, 30))
        self.chem_elem_cb.setObjectName("chem_elem_cb")
        self.min_dsb = QtWidgets.QDoubleSpinBox(edit_ww)
        self.min_dsb.setGeometry(QtCore.QRect(230, 70, 141, 31))
        self.min_dsb.setDecimals(6)
        self.min_dsb.setSingleStep(0.01)
        self.min_dsb.setObjectName("min_dsb")
        self.che_elem_label_4 = QtWidgets.QLabel(edit_ww)
        self.che_elem_label_4.setGeometry(QtCore.QRect(20, 20, 191, 22))
        self.che_elem_label_4.setObjectName("che_elem_label_4")
        self.edit_bb = QtWidgets.QDialogButtonBox(edit_ww)
        self.edit_bb.setGeometry(QtCore.QRect(190, 180, 183, 30))
        self.edit_bb.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.edit_bb.setObjectName("edit_bb")
        self.che_elem_label_5 = QtWidgets.QLabel(edit_ww)
        self.che_elem_label_5.setGeometry(QtCore.QRect(20, 70, 191, 22))
        self.che_elem_label_5.setObjectName("che_elem_label_5")
        self.che_elem_label_6 = QtWidgets.QLabel(edit_ww)
        self.che_elem_label_6.setGeometry(QtCore.QRect(20, 120, 191, 22))
        self.che_elem_label_6.setObjectName("che_elem_label_6")

        self.retranslateUi(edit_ww)
        QtCore.QMetaObject.connectSlotsByName(edit_ww)
        edit_ww.setTabOrder(self.chem_elem_cb, self.min_dsb)
        edit_ww.setTabOrder(self.min_dsb, self.max_dsb)

    def retranslateUi(self, edit_ww):
        _translate = QtCore.QCoreApplication.translate
        edit_ww.setWindowTitle(_translate("edit_ww", "Edit - GG"))
        self.che_elem_label_4.setText(_translate("edit_ww", "Chemical element:"))
        self.che_elem_label_5.setText(_translate("edit_ww", "Min:"))
        self.che_elem_label_6.setText(_translate("edit_ww", "Max:"))

