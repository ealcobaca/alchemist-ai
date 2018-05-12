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
    # simple, with one state
    print("\n>>> Simple, with one state <<<")
    tsp = AnnealingGlass(
        state=np.random.rand(45).tolist(),
        qtd_distutb=20, tg=0.85, perc_disturb=1)
    result = tsp.run()
    print()
    print(result.get_result()[0])

    print("\n>>> With multiple state <<<")
    # with more one states
    states = [np.random.rand(45).tolist() for i in range(3)]
    tsp_mult = AnnealingGlass(
        state=states,
        qtd_distutb=20, tg=0.85, perc_disturb=1)
    result = tsp_mult.run()
    print()
    print(result.get_result()[0])

    # with any states in optpool
    print("\n>>> With multiple state <<<")

    tps1 = AnnealingGlass(state=np.random.rand(45).tolist(),
                          qtd_distutb=20, tg=0.85, perc_disturb=1)
    tps2 = AnnealingGlass(state=np.random.rand(45).tolist(),
                          qtd_distutb=20, tg=0.85, perc_disturb=1)
    tps3 = AnnealingGlass(state=np.random.rand(45).tolist(),
                          qtd_distutb=20, tg=0.85, perc_disturb=1)
    optpool = OptPool([tps1, tps2, tps3, tsp_mult])
    ret = optpool.run()
    print()
    print(ret)

    return


if __name__ == "__main__":
    main()


