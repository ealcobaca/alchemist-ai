#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File.....: optimizer.py
Author...: Bruno Pimentel, Edesio Alcobaça
Email....: bappimentel@gmail.com, e.alcobaca@gmail.com
Github...: https://github.com/bapimentel, https://github.com/ealcobaca
Description:
"""

import re
import numpy as np
from keras.models import load_model
import tensorflow as tf

from sklearn.ensemble import RandomForestRegressor
from util import Reader


class Optimizer(object):
    """
    TODO:
    """
    '''
    AVAILABLECOMPOUNDS = ['Ag2O', 'Al2O3', 'As2O3', 'As2O5', 'B2O3', 'BaO',
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
    '''

    AVAILABLECOMPOUNDS = ['Ag2O', 'Al2O3', 'As2O3', 'As2O5', 'B2O3', 'BaO',
                          'Bi2O3', 'CaO', 'CdO', 'Ce2O3', 'CeO2', 'Cl', 'Cs2O',
                          'Cu2O', 'CuO', 'Er2O3', 'F', 'Fe2O3', 'Fe3O4', 'FeO',
                          'Ga2O3', 'Gd2O3', 'GeO2', 'I', 'K2O', 'La2O3',
                          'Li2O', 'MgO', 'Mn2O3', 'Mn2O7', 'Mn3O4', 'MnO',
                          'MnO2', 'Mo2O3', 'Mo2O5', 'MoO', 'MoO2', 'MoO3', 'N',
                          'N2O5', 'NO2', 'Na2O', 'Nb2O3', 'Nb2O5', 'P2O3',
                          'P2O5', 'Pb3O4', 'PbO', 'PbO2', 'SO2', 'SO3',
                          'Sb2O3', 'Sb2O5', 'SbO2', 'SiO2', 'Sn2O3',
                          'SnO', 'SnO2', 'SrO', 'Ta2O3', 'Ta2O5',
                          'TeO3', 'Ti2O3', 'TiO', 'TiO2', 'V2O3', 'V2O5',
                          'VO2', 'VO6', 'WO3', 'Y2O3', 'Yb2O3', 'ZnO', 'ZrO2']

    # Chemical_Elemnts = ["Cd", "Yb", "Cs", "N", "Mn", "S", "Ce", "Er", "I",
    #                     "Mo", "Cl", "As", "Ga", "Cu", "Sn", "Ag", "Ta", "Y",
    #                     "Gd", "Ge", "V", "Fe", "W", "F", "Sb", "Sr", "Te",
    #                     "Nb", "Bi", "La", "Pb", "Zr", "Ti", "Mg", "Ba", "K",
    #                     "Ca", "Zn", "Li", "P", "Al", "Na", "B", "Si", "O"]
    #
    Chemical_Elemnts = ["Yb", "Pb", "Ca", "Ti", "Mo", "Sn", "Cd", "Ag", "La",
                        "Cs", "W", "Sb", "Ta", "V", "Fe", "Bi", "Ce", "Nb",
                        "Cu", "I", "B", "Te", "Al", "Zr", "Gd", "Na", "Ga",
                        "Cl", "S", "Si", "O", "F", "Mn", "Ba", "K", "Zn",
                        "N", "Li", "Ge", "Y", "Sr", "P", "Mg", "Er", "As"]


    def __init__(self, tg, min_max_dic, seed=None, path='models/ANN.h5', clf_rf=None, limiar_rf=1200):
        custom_objects = {'huber_loss': tf.losses.huber_loss}
        self.model = load_model(path, custom_objects=custom_objects)
        self.model_rf = clf_rf
        self.limiar_rf = limiar_rf

        self.tg = tg
        self.min_max_dic = min_max_dic

        if seed is not None:
            np.random.seed(seed)

        #self.init_clf()
        #if clf is not None:
        #    self.model = clf

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
        clf = RandomForestRegressor(n_estimators= 10, min_samples_leaf=1, max_depth=1000, random_state=0)
        print('Treinando RF...')
        self.model_rf = clf.fit(data_train, data_target)
        #predictions = clf.predict(X_test)

    def predict(self, example, target):
        """TODO: Docstring for fit.
        :returns: TODO
        """
        #print(example)

        example = np.asarray([self.dict_to_matrix(example)])
        if self.model_rf is None:
            #print('model_rf = None')
            # ANN ####################################################
            pred = self.model.predict(example)
        else:
            #print(self.limiar_rf)
            target = target*1452.0
            if target > self.limiar_rf:# 1200.0:
                # ANN ####################################################        
                pred = self.model.predict(example)
            else:
                # RF ####################################################
                pred = self.model_rf.predict(example)
                #print('RF')

        return pred[0]


    @classmethod
    def matrix_to_dic(cls, min_max):
        dic_min_max = {}
        for i in range(len(min_max)):
            if min_max[i][1] >= min_max[i][0] and min_max[i][1] != 0:
                dic_min_max[cls.AVAILABLECOMPOUNDS[i]] = min_max[i].copy()
        return dic_min_max


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
        compostoDic = self.compounddic2atomsfraction(compostoDic)
        matriz = [0.0]*len(self.Chemical_Elemnts)
        for composto in compostoDic:
            indice = self.Chemical_Elemnts.index(composto)
            # print(compostoDic[composto])
            matriz[indice] = compostoDic[composto]
        return matriz

    @classmethod
    def vector_to_dic(cls, values, keys):
        dic = {}
        for value, key in zip(values, keys):
            dic[key] = value
        return dic

    @classmethod
    def dic_to_vector(cls, dic):
        vector = [0]*len(cls.Chemical_Elemnts)
        for key in dic.keys():
            idx = cls.Chemical_Elemnts.index(key)
            vector[idx] = dic[key]
        return vector

    @classmethod
    def dic_to_vector_compound(cls, dic):
        vector = [0]*len(cls.AVAILABLECOMPOUNDS)
        for key in dic.keys():
            idx = cls.AVAILABLECOMPOUNDS.index(key)
            vector[idx] = dic[key]
        return vector


    def run(self):
        """TODO: Docstring for run.
        :returns: TODO

        """
        return []


