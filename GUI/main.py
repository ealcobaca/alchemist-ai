#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication
from src import App


def main():
    APP = QApplication(sys.argv)
    ex = App()
    sys.exit(APP.exec_())


if __name__ == "__main__":
    main()
