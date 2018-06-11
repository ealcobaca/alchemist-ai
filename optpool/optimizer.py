#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File.....: optimizer.py
Author...: Bruno Pimentel, Edesio Alcobaça
Email....: bappimentel@gmail.com, e.alcobaca@gmail.com
Github...: https://github.com/bapimentel, https://github.com/ealcobaca
Description:
"""

import numpy as np
from keras.models import load_model
import tensorflow as tf


class Optimizer(object):
    """
    TODO:
    """
    AvailableCompounds = ['Ag2O', 'Al2O3', 'As2O3', 'As2O5', 'B2O3', 'BaO',
                          'Bi2O3', 'CaO', 'CdO', 'Ce2O3', 'CeO2', 'Cl', 'Cs2O',
                          'Cu2O', 'CuO', 'Er2O3', 'F', 'Fe2O3', 'Fe3O4', 'FeO',
                          'Ga2O3', 'Gd2O3', 'GeO', 'GeO2', 'I', 'K2O', 'La2O3',
                          'Li2O', 'MgO', 'Mn2O3', 'Mn2O7', 'Mn3O4', 'MnO',
                          'MnO2', 'Mo2O3', 'Mo2O5', 'MoO', 'MoO2', 'MoO3', 'N',
                          'N2O5', 'NO2', 'Na2O', 'Nb2O3', 'Nb2O5', 'P2O3',
                          'P2O5', 'Pb3O4', 'PbO', 'PbO2', 'SO2', 'SO3',
                          'Sb2O3', 'Sb2O5', 'SbO2', 'SiO', 'SiO2', 'Sn2O3',
                          'SnO', 'SnO2', 'SrO', 'Ta2O3', 'Ta2O5', 'TeO2',
                          'TeO3', 'Ti2O3', 'TiO', 'TiO2', 'V2O3', 'V2O5',
                          'VO2', 'VO6', 'WO3', 'Y2O3', 'Yb2O3', 'ZnO', 'ZrO2']

    Chemical_Elemnts = ["Cd", "Yb", "Cs", "N", "Mn", "S", "Ce", "Er", "I",
                        "Mo", "Cl", "As", "Ga", "Cu", "Sn", "Ag", "Ta", "Y",
                        "Gd", "Ge", "V", "Fe", "W", "F", "Sb", "Sr", "Te",
                        "Nb", "Bi", "La", "Pb", "Zr", "Ti", "Mg", "Ba", "K",
                        "Ca", "Zn", "Li", "P", "Al", "Na", "B", "Si", "O"]

    def __init__(self, path='models/ANN.h5'):
        custom_objects = {'huber_loss': tf.losses.huber_loss}
        self.model = load_model(path, custom_objects=custom_objects)

    def predict(self, example):
        """TODO: Docstring for fit.
        :returns: TODO

        """
        example = self.dict2Matrix(example):
        pred = self.model.predict(np.array([example]))
        return pred[0]

    def compounddic2atomsfraction(self, compounds):

        def createNewDic(dic, multiplyby):
            values = list(dic.values())
            keys = dic.keys()
            newValues = np.array(values)*multiplyby
            newDic = dict(zip(keys, newValues))
            return newDic

        def composition2atoms(cstr):
            lst = re.findall(r'([A-Z][a-z]?)(\d*\.?\d*)', cstr)
            dic = {}
            for i in lst:
                if len(i[1]) > 0:
                    try:
                        dic[i[0]] = int(i[1])
                    except ValueError:
                        dic[i[0]] = float(i[1])
                else:
                    dic[i[0]] = 1
            return dic

        dic = {}

        for key in compounds.keys():
            baseValue = compounds[key]
            atoms = composition2atoms(key)
            for a in atoms.keys():
                dic[a] = dic.get(a, 0) + atoms[a]*baseValue

        multiplyby = 1.0/np.sum(list(dic.values()))
        atomsF = createNewDic(dic, multiplyby)

        return atomsF

    def dict_to_matrix(self, compostoDic):
        matriz = [0.0]*len(self.Chemical_Elemnts)
        for composto in compostoDic:
            indice = self.Chemical_Elemnts.index(composto)
            print(compostoDic[composto])
            matriz[indice] = compostoDic[composto]
        return matriz

    def matrix_to_dic(self, min_max):
        dic_min_max = {}
        for i in range(len(min_max)):
            if min_max[i][0] >= min_max[i][1] and min_max
            dic_min_max[self.AvailableCompounds[i]] = min_max[i].copy()

    def vector_to_dic(self, values, keys):
        dic = {}
        for value, key in zip(values, keys):
            dic[key] = value

        return dic

    def run(self):
        """TODO: Docstring for run.
        :returns: TODO

        """
        return []
