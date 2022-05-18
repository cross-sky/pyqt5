'''
Author: your name
Date: 2022-05-18 22:35:24
LastEditTime: 2022-05-18 22:59:59
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pyqt5\\vrf\ui_fun\SerialObject.py
'''


import serial
from serial.serialutil import EIGHTBITS, PARITY_EVEN, STOPBITS_ONE
import serial.tools.list_ports

import logging
logging.basicConfig(level=logging.DEBUG)

class SerialPort:
    def __init__(self, port='com10', baudrate=9600):
        self.serial = serial.Serial()
        self.serial.port = port
        self.serial.baudrate = baudrate
        self.serial.timeout = 2
        self.serial.parity = PARITY_EVEN
        self.serial.stopbits = STOPBITS_ONE
        self.serial.bytesize = EIGHTBITS

    def list_ports(self):
        com_list = list(serial.tools.list_ports.comports())
        for i in com_list:
            logging.debug(i)
        return com_list

    def bind_port(self):
        # bind two ports
        # port = self.selec_coms('master')
        # if port is not '':
        #     self.serial_spy_master.serial.port = port
        # print('your select {} com is {}'.format('master', self.serial_spy_master.serial.port))
