'''
Author: your name
Date: 2022-04-16 15:24:36
LastEditTime: 2022-04-30 12:38:00
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pyqt5\EX1GuessNum\function\func_guess_num.py
'''
from logging import debug
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, showbase
from PyQt5.QtWidgets import QDialog, QFileDialog, QMainWindow, QMessageBox
from random import randint

sys.path.append('.')

from vrf.ui.Ui_vrf_decode import Ui_MainWindow
from vrf.vrf_cmd_print import *

class FunVrfUi(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None) -> None:
        super(FunVrfUi, self).__init__()
        self.setupUi(self)

        self.messageBox = QMessageBox()

    def closeEvent(self, event):
        reply = self.messageBox.question(self, 'MAKE', 'EXIT?', QMessageBox.Yes,QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    @pyqtSlot()
    def on_decodeButton_clicked(self):
        result = ''
        try:
            datas = self.inputText.toPlainText().split('\n')
            logging.debug('datas: ' + str(datas))
            for s in datas:
                logging.debug('-'+s+'-')
                result += s + '\r\n'
                dec_cmd = RD505CMD(s)
                dec_cmd.cmd_check()
                # decode_str = myprint_cmd0x4c_request(dec_cmd.data_decode_dict)
                decode_str = eval(dec_cmd.data_decode_dict.get(MYPRINT_FUNCTION))(dec_cmd.data_decode_dict)
                for s in decode_str:
                    result += s + '\r\n'
                result += '----------------------------\r\n'
        except Exception as e:
            # self.outputText.setPlainText('len, fcc ok, may be data is fake cmd or data.' + str(e))
            result += 'len, fcc ok, may be data is fake cmd or data.' + str(e)
            logging.debug(e)
            
            
        # print('haha')
        # self.outputText.setPlainText(self.inputText.toPlainText())
        self.outputText.setPlainText(result)
        # logging.debug(result)

    # @pyqtSlot()
    def on_ExitButton_clicked(self):
        print("haha")