#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
Simple gravity ODE test.
MIT License

Created on Sun Mar 17 18:51:26 2019
@author: dfbowden
"""

import numpy as np

def gravity(state,time):
    ''' Simple gravity ODE
    
    state[0] is position
    state[1] is velocity
    '''
    state_dot = np.zeros(2)
    state_dot[0] = state[1]
    state_dot[1] = -9.8
    
    return(state_dot)
