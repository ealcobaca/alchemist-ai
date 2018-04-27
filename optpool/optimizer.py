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
    def __init__(self, path='models/ANN.h5'):
        custom_objects = {'huber_loss': tf.losses.huber_loss}
        self.model = load_model(path, custom_objects=custom_objects)

    def predict(self, example):
        """TODO: Docstring for fit.
        :returns: TODO

        """
        pred = self.model.predict(np.array([example]))
        return pred[0]

    def run(self):
        """TODO: Docstring for run.
        :returns: TODO

        """
        return []
