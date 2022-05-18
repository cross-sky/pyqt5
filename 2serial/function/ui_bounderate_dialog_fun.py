'''
Author: your name
Date: 2022-05-11 23:37:08
LastEditTime: 2022-05-17 00:00:46
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: r"\\pyqt5\\vrf\\ui_fun\\ui_bounderate_fun.py"
'''


import logging
logging.basicConfig(level=logging.DEBUG)

from enum import Enum, unique
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, pyqtSlot, showbase
from PyQt5.QtWidgets import QDialog, QFileDialog, QMainWindow, QMessageBox,QApplication
from random import randint
# from myutil import _const
sys.path.append('..')
sys.path.append('.')
from ui.Ui_ui_boundrate_dialog import Ui_Dialog
# from vrf.vrf_cmd_print import *


class SerDiaEnum(Enum):
    COMS = 1
    COMS_INDEX = 2
    BOUNDRATE = 3
    BOUNDRATE_INDEX = 4
    COM_CC = 5
    COM_CC_INDEX = 6
    COM_BITS = 7
    COM_BITS_INDEX = 8

class BoundRateVrfUi(QDialog, Ui_Dialog):
    # signal when button is ok then emit to mainwindow
    signal_serial = pyqtSignal(dict)
    
    def __init__(self, parent=None) -> None:
        super(BoundRateVrfUi, self).__init__()
        self.setupUi(self)

        self.comboBox_boundrate.addItems(["2400", "9600", "57600", "115200"])
        self.comboBox_bits.addItems(["8", "9" , '10'])
        self.comboBox_cc.addItems(['None', 'odd', 'even'])
        self.comboBox_flow.addItems(['no', 'yes'])

        self.ser_dict = {}

    def getSerialData(self):
        # if self.ser_dict.get(COMS) is None:

        self.ser_dict[SerDiaEnum.COMS.value] = self.comboBox_serialList.currentText()
        self.ser_dict[SerDiaEnum.COMS_INDEX.value] = self.comboBox_serialList.currentIndex()
        self.ser_dict[SerDiaEnum.BOUNDRATE.value] = self.comboBox_boundrate.currentText() #self.comboBox_boundrate.itemData(self.comboBox_boundrate.currentIndex())
        self.ser_dict[SerDiaEnum.BOUNDRATE_INDEX.value] = self.comboBox_boundrate.currentIndex()
        self.ser_dict[SerDiaEnum.COM_CC.value] = self.comboBox_cc.currentText() #self.comboBox_cc.itemData(self.comboBox_cc.currentIndex())
        self.ser_dict[SerDiaEnum.COM_CC_INDEX.value] = self.comboBox_cc.currentIndex()
        self.ser_dict[SerDiaEnum.COM_BITS.value] = self.comboBox_bits.currentText()
        self.ser_dict[SerDiaEnum.COM_BITS_INDEX.value] = self.comboBox_bits.currentIndex()


    def accept(self) -> None:
        self.getSerialData()
        self.signal_serial.emit(self.ser_dict)
        logging.debug(str(self.ser_dict))
        return super().accept()
    
    def setSeriaData(self, dicts:dict):
        # update data
        if dicts[SerDiaEnum.COMS.value] != '':
            self.comboBox_serialList.setCurrentIndex(dicts[SerDiaEnum.COMS_INDEX.value])
        self.comboBox_boundrate.setCurrentIndex(dicts[SerDiaEnum.BOUNDRATE_INDEX.value])
        self.comboBox_cc.setCurrentIndex(dicts[SerDiaEnum.COM_CC_INDEX.value])
        self.comboBox_bits.setCurrentIndex(dicts[SerDiaEnum.COM_BITS_INDEX.value])
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = BoundRateVrfUi()
    ui.show()
    sys.exit(app.exec_())
