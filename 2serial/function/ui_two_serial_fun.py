'''
Author: your name
Date: 2022-05-18 23:35:10
LastEditTime: 2022-05-18 23:39:13
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \\pyqt5\\2serial\\function\\ui_two_serial_fun.py
'''

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, showbase
from PyQt5.QtWidgets import QDialog, QFileDialog, QMainWindow, QMessageBox,QApplication
from random import randint

import serial
from serial.serialutil import EIGHTBITS, PARITY_EVEN, STOPBITS_ONE
import serial.tools.list_ports
import threading
from queue import Queue
import time
import os

sys.path.append('..')
sys.path.append('.')


from ui.Ui_two_serial import Ui_MainWindow
from .ui_bounderate_dialog_fun import BoundRateVrfUi, SerDiaEnum

# from vrf.vrf_cmd_print import *

class MainWindowUi(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None) -> None:
        super(MainWindowUi, self).__init__()
        self.setupUi(self)

        # self.pushButton_set_boundrate.clicked.connect

