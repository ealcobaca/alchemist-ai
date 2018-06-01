#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: test_annealing_glass.py
Author: E. Alcobaça
Email: e.alcobaca@gmail.com
Github: https://github.com/ealcobaca
Description: A simples test to the AnnealingGlass class
"""
from optpool import AnnealingGlass
from optpool import OptPool
import numpy as np


def main():
    """TODO: Docstring for main.
    :returns: TODO

    """
    # np.random.seed(123)
    # with restriction
    print("\n>>> Simple, with one state <<<")
    restriction = [[0.0, 0.3], [0.0, 0.9], [0.0, 0.6], [0.0, 0.0], [0.0, 0.0],
                   [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0],
                   [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0],
                   [0.0, 0.9], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0],
                   [0.0, 0.9], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0],
                   [0.0, 0.9], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0],
                   [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0],
                   [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0],
                   [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.9], [0.0, 0.5]]
    tsp = AnnealingGlass(tg=0.85, steps=5000, restriction=restriction)
    result = tsp.run()
    print()
    print(result.get_result()[0])

    restriction = [[0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0],
                   [0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0],
                   [0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0],
                   [0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0],
                   [0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0],
                   [0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0],
                   [0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0],
                   [0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0],
                   [0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0]]
    tsp = AnnealingGlass(tg=0.85, steps=5000, restriction=restriction,
                         save_preds=True, save_states=True)
    result = tsp.run()
    print()
    print(result.get_result()[0])
    print(len(result.get_result()[3]))
    print(len(result.get_result()[4]))
    return


if __name__ == "__main__":
    main()


