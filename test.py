# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 16:58:23 2022

@author: mlols
"""
from ReduceMonomsRBC import monom_reduction

monom_reduction('auto', monom_deg=6, hier_num=4,
                monom_dir='Monoms', fQ_dir='Monoms/fQ')
