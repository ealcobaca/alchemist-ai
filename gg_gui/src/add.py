#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gui import Ui_add_ww
from PyQt5.QtWidgets import (QMainWindow,
                             QDialogButtonBox,
                             QTableWidgetItem)
from PyQt5 import QtCore


class Add(QMainWindow, Ui_add_ww):
    def __init__(self, parent):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.parent = parent

        self.add_bb.accepted.connect(self.add_bb_accepted)
        self.add_bb.rejected.connect(self.add_bb_rejected)

    def add_bb_accepted(self):
        print("Ok")
        elem = self.chem_elem_cb.currentText()
        min_elem = self.min_dsb.value()
        max_elem = self.max_dsb.value()
        new_item = QTableWidgetItem()
        row_count = 0
        self.parent.min_max_table.setItem(
            row_count, 0, QTableWidgetItem(elem))
        self.parent.min_max_table.setItem(
            row_count, 1, QTableWidgetItem(min_elem))
        self.parent.min_max_table.setItem(
            row_count, 2, QTableWidgetItem(max_elem))
        print("{0:s}, {1:6f}, {2:6f}".format(elem, min_elem, max_elem))
        self.close()

    def add_bb_rejected(self):
        print("Cancel")
        self.close()
