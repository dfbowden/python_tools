#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
{Description}
MIT License

Created on Sun Apr 21 11:32:38 2019
@author: dfbowden
"""

# How should this be structured?
import Sensors
import Navigation
import Guidance
import Autopilot
import Controls
import Actuators
import Physics

class Vehicle:
    def __init__(self):
        self.sens = Sensors.IMU
        self.nav = Navigation()
        self.guid = Guidance()
        self.ap = Autopilot()
        self.con = Controls()
        self.act = Actuators()
        self.phys = Physics()
        
    def exec(self):
        self.sens.exec()
        self.nav.exec()
        self.guid.exec()
        self.ap.exec()
        self.con.exec()
        self.act.exec()
        self.phys.exec()
        
        