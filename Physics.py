#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
Simple gravity ODE test.
MIT License

Created on Sun Mar 17 18:51:26 2019
@author: dfbowden
"""

import numpy as np

class Physics:
    def __init__(self,initialState):
        
    def forces():
        aero()
        gravity()
        thrust()
        
    def moments():
        aero()
        gravity()
        thrust()
        
        

def gravity(state,time):
    ''' Simple gravity ODE
    
    state[0,0] is position
    state[1,0] is velocity
    '''
    state_dot = np.zeros((2,1))
    state_dot[0,0] = state[1,0]
    state_dot[1,0] = -9.8
    
    return(state_dot)

def spring_mass(state,time,input):
    return(0)