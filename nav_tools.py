#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
Variety of tools useful for navigation.
MIT License

Created on Sun Mar 17 21:51:08 2019
@author: dfbowden
"""

import numpy as np
from numpy.linalg import inv

# Cholesky decomposition would probably be more stable than the direct inverse
# The stability of this algorithm could be improved by using a square root kalman filter
def kf(F,B,H,Q,R,x_prev,P_prev,u,z):
    # Check dimensions...
    if F.ndim != 2 or B.ndim != 2 or H.ndim != 2 or Q.ndim != 2 or R.ndim != 2 or x_prev.ndim != 2 or P_prev.ndim != 2 or u.ndim != 2 or z.ndim != 2:
        raise Exception('All arguments must be a 2D matrix')
    m = x_prev.shape[0]
    n = u.shape[0]
    o = z.shape[0]
    if F.shape[0] != m or F.shape[1] != m:
        raise Exception('F must be a ' + str(m) + ' by ' + str(m) + ' matrix')
    elif B.shape[0] != m or B.shape[1] != n:
        raise Exception('B must be a ' + str(m) + ' by ' + str(n) + ' matrix')
    elif H.shape[0] != o or H.shape[1] != m:
        raise Exception('H must be a ' + str(o) + ' by ' + str(m) + ' matrix')
    elif Q.shape[0] != m or Q.shape[1] != m:
        raise Exception('Q must be a ' + str(m) + ' by ' + str(m) + ' matrix')
    elif R.shape[0] != o or R.shape[1] != o:
        raise Exception('R must be a ' + str(o) + ' by ' + str(o) + ' matrix')
    elif x_prev.shape[0] != m or x_prev.shape[1] != 1:
        raise Exception('x_prev must be a ' + str(m) + ' by ' + str(1) + ' matrix')
    elif P_prev.shape[0] != m or P_prev.shape[1] != m:
        raise Exception('P_prev must be a ' + str(m) + ' by ' + str(m) + ' matrix')
    elif u.shape[0] != n or u.shape[1] != 1:
        raise Exception('u must be a ' + str(n) + ' by ' + str(1) + ' matrix')
    elif z.shape[0] != o or z.shape[1] != 1:
        raise Exception('z must be a ' + str(o) + ' by ' + str(1) + ' matrix')
    
    x_est = F @ x_prev + B @ u
    P_est = F @ P_prev @ F.T + Q
    y_est = z - H @ x_est
    S = R + H @ P_est @ H.T
    K = P_est @ H.T @ inv(S)
    x_est = x_est + K @ y_est
    P_est = (np.identity(m) - K @ H) @ P_est @ (np.identity(m) - K @ H).T + K @ R @ K.T
    y_est = z - H @ x_est
    return(x_est,y_est,P_est)

def ekf():
    return(0)

def ukf():
    return(0)

