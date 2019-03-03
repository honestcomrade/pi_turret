#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 17:49:03 2019
joystick
@author: jf
"""
from smbus2 import SMBus
import time

class nunchuck(object):
    
    def __init__(self):
        self.address = 0x52
        self.i2c_bus = 1 #0, 1 ?
        self.setup()

    def setup(self):
        print("Initialise I2C")
        self.bus = SMBus(self.i2c_bus)
        #init nunchuck
        self.bus.write_byte_data(self.address, 0x40, 0x00)
      
    def readNck(self):
        time.sleep(0.004)
        try:
            self.bus.write_byte(self.address, 0)
        except:
            print("Bus restart")
            time.sleep(0.1)
            self.setup()
            self.bus.write_byte(self.address, 0)
        else:
            time.sleep(0.002) #delay for Nunchuck to respond
            #Joystick position (x and y)
            #Orientation (x, y and z)
            #Two button states (called c and z)
            nCk = [((self.bus.read_byte(self.address ) ^ 0x17) +0x17) for i in range(0,6)]   
          #  nCk = [(self.bus.read_byte(self.address)) for i in range(0,6)]   
            
#            joyX = nCk [0]
#            joyY = nCk [1]
#            accelX = (nCk [2] << 2) | ((nCk [5] & 0xc0) >> 6)
#            accelY = (nCk [3] << 2) | ((nCk [5] & 0x30) >> 4)
#            accelZ = (nCk [4] << 2) | ((nCk [5] & 0x0c) >> 2)
#            c = (nCk [5] & 0x02) >> 1
#            z = nCk [5] & 0x01;
            return nCk
    
    
if __name__ =="__main__":
    mynunchuck = nunchuck()
    joylast=[-1]*4
    try:
        while True:
            bank = mynunchuck.readNck()
            print(bank)
#         if bank[0] > 190:
#            joyNow[x] = 1 # move right
#         if bank[0] < 60:
#            joyNow[x] = 0 # move left
#         if bank[1] > 190:
#            joyNow[y] = 2 # move up
#         if bank[1] < 60:
#            joyNow[y] = 3 # move down
#         if joyNow[x] != joyLast[x] and joyNow[x] > -1:
#            movePlayer(nun,joyNow[x]) # move left or right
#         if joyNow[y] != joyLast[y] and joyNow[y] > 1:
#            movePlayer(nun,joyNow[y]) # move up or down
#         joyLast[x] = joyNow[x]          
#         joyLast[y] = joyNow[y]
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass    
