#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: resultopt.py
Author: Edesio Alcobaça
Email: e.alcobaca@gmail.com
Github: https://github.com/ealcobaca
Description: TODO
"""


class ResultOpt(object):
    """ TODO """

    def __init__(self, type_opt, result):
        self.type_opt = type_opt
        self.result = result

    def get_result(self):
        """TODO: Docstring for getResult.
        :returns: TODO

        """
        return self.result

    def get_type(self):
        """TODO: Docstring for getType.

        :returns: TODO

        """
        return self.type_opt
