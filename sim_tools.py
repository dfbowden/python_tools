#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
Variety of tools useful for simulations
MIT License

Created on Sun Mar 17 11:23:44 2019
@author: dfbowden
"""

import numpy as np

def RK4_step(state,time,dt,ODE,**kwargs):
    """ 1 step of the 4th Order Runge Kutta Method
    
    @param ODE:      The system to be integrated. 
    @type ODE:       Function that works as below:
                     derivatives = ODE(state,time)
    @param state:    The initial states to be used.
    @type state:     Numpy array.
    @param time:     The initial time to be used.
    @type time:      Float
    @param dt:       Time step
    @type dt:        Float
    @param **kwargs: Any additional arguments to calculate ODE.
    """
    
    if not callable(ODE):
        raise Exception("ODE argument must be a function!")
    if type(state) != np.ndarray:
        raise Exception("state argument must be a numpy array!")
    if type(time) != float:
        raise Exception("time argument must be a float!")
    if type(dt) != float:
        raise Exception("dt argument must be a float!")
    
    k1 = ODE(state,time,**kwargs)
    k2 = ODE(state + k1*dt/2,time+dt/2,**kwargs)
    k3 = ODE(state + k2*dt/2,time+dt/2,**kwargs)
    k4 = ODE(state + k3*dt,  time+dt,**kwargs)
    a = np.array([1.0/6.0, 1.0/3.0, 1.0/3.0, 1.0/6.0])
    next_state = state + dt*(a[0]*k1 + a[1]*k2 + a[2]*k3 + a[3]*k4)
    next_time = time + dt
    return(next_state,next_time)
    
def RK4(state,ti,tf,dt,ODE,**kwargs):
    """ 4th Order Runge Kutta Method
    
    @param ODE:      The system to be integrated. 
    @type ODE:       Function that works as below:
                     derivatives = ODE(state,time)
    @param state:    The initial states to be used.
    @type state:     Numpy array.
    @param ti:       The initial time to start integration.
    @type ti:        Float
    @param tf:       The final time to stop integration.
    @type tf:        Float
    @param dt:       Time step
    @type dt:        Float
    @param **kwargs: Any additional arguments to calculate ODE.
    """
    
    if type(ti) != float:
        raise Exception("ti argument must be a float!")
    if type(tf) != float:
        raise Exception("tf argument must be a float!")
        
    steps = int(np.ceil((tf-ti)/dt)+1)
    time_array = [0]*steps
    state_array = [0]*steps
    time = ti
    time_array[0] = time
    state_array[0] = state
    for step in range(steps-1):
        state,time = RK4_step(ODE,state,time,dt,**kwargs)
        state_array[step+1] = state
        time_array[step+1] = time
    return(state_array,time_array)
        
        