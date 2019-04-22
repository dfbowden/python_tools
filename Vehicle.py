#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
{Description}
MIT License

Created on Sun Apr 21 11:32:38 2019
@author: dfbowden
"""
import Sensors
import Navigation
import Guidance
import Autopilot
import Controls
import Actuators
import Physics

class Vehicle:
    def __init__(self):
        sens = Sensors()
        nav = Navigation()
        guid = Guidance()
        ap = Autopilot()
        con = Controls()
        act = Actuators()
        phys = Physics()
        
    def exec(self):
        sens.exec()
        nav.exec()
        guid.exec()
        ap.exec()
        con.exec()
        act.exec()
        phys.exec()
        
        