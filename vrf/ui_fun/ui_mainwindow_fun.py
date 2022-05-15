'''
Author: your name
Date: 2022-05-14 22:52:12
LastEditTime: 2022-05-15 10:27:35
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \\pyqt5\\vrf\\ui_fun\\ui_mainwindow_fun.py
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

from ui.Ui_main_window import Ui_MainWindow
from .ui_bounderate_fun import BoundRateVrfUi

# from vrf.vrf_cmd_print import *

class MainWindowUi(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None) -> None:
        super(MainWindowUi, self).__init__()
        self.setupUi(self)

        self.boundrateWindow = BoundRateVrfUi()
        self.serial = None
        
        self.serialList = ['com0', 'com1']
        


        # set object paramaters
        self.lineEdit_boundrate = self.boundrateWindow.comboBox_boundrate
        

    @pyqtSlot()
    def on_pushButton_set_boundrate_clicked(self):
        # if self.boundrateWindow is None:
        #     self.boundrateWindow = BoundRateVrfUi()
        self.boundrateWindow.comboBox_serialList.addItems(self.serialList)
        self.boundrateWindow.raise_()
        self.boundrateWindow.show()
    
    @pyqtSlot()
    def on_pushButton_on_clicked(self):
        if (self.serial is None):
            QMessageBox.about(self, '串口', '未设置串口参数')

    @pyqtSlot()
    def on_pushButton_set_mainmachine_clicked(self):
        self.close()
    
    # 

            # self.boundrateWindow.exec_()
        # self.comboBox_boundrate.addItems(["2400", "9600", "57600", "115200"])
        # self.comboBox_bits.addItems(["8", "9" , '10'])
        # self.comboBox_cc.addItems(['None', 'odd', 'even'])
        # self.comboBox_flow.addItems(['no', 'yes'])


    # @pyqtSlot()
    # def on_decodeButton_clicked(self):
    #     result = ''
    #     try:
    #         datas = self.inputText.toPlainText().split('\n')
    #         logging.debug('datas: ' + str(datas))
    #         for s in datas:
    #             logging.debug('-'+s+'-')
    #             result += s + '\r\n'
    #             dec_cmd = RD505CMD(s)
    #             dec_cmd.cmd_check()
    #             # decode_str = myprint_cmd0x4c_request(dec_cmd.data_decode_dict)
    #             decode_str = eval(dec_cmd.data_decode_dict.get(MYPRINT_FUNCTION))(dec_cmd.data_decode_dict)
    #             for s in decode_str:
    #                 result += s + '\r\n'
    #             result += '----------------------------\r\n'
    #     except Exception as e:
    #         # self.outputText.setPlainText('len, fcc ok, may be data is fake cmd or data.' + str(e))
    #         result += 'len, fcc ok, may be data is fake cmd or data.' + str(e)
    #         logging.debug(e)
            
            
    #     # print('haha')
    #     # self.outputText.setPlainText(self.inputText.toPlainText())
    #     self.outputText.setPlainText(result)
    #     # logging.debug(result)

    # # @pyqtSlot()
    # def on_ExitButton_clicked(self):
    #     print("haha")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainWindowUi()
    ui.show()
    sys.exit(app.exec_())