#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui import Ui_main_window


class App(QMainWindow, Ui_main_window):
    def __init__(self):
        super(QMainWindow, self).__init__()

        # Set up the user interface from designer
        self.setupUi(self)

        # Make some local modification ...


        # Connect up the buttons
        self.add_btn.clicked.connect(self.add_btn_clicked)
        self.edit_btn.clicked.connect(self.edit_btn_clicked)
        self.remove_btn.clicked.connect(self.remove_btn_clicked)
        self.run_btn.clicked.connect(self.run_btn_clicked)
        self.show()

    def add_btn_clicked(self):
        """TODO: Docstring for add_btn_clicled.
        :returns: TODO

        """
        print("add")

    def edit_btn_clicked(self):
        """TODO: Docstring for edit_btn_clicled.
        :returns: TODO

        """
        print("edit")

    def remove_btn_clicked(self):
        """TODO: Docstring for remove_btn_clicked.
        :returns: TODO

        """
        print("remove")

    def run_btn_clicked(self):
        """TODO: Docstring for run_btn_clicked.
        :returns: TODO

        """
        print("run")
