'''
Author: your name
Date: 2022-04-16 15:24:36
LastEditTime: 2022-04-17 12:29:45
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
        # self.num = randint(1, 100)
        # print(self.num)
        # self.numShow.selectAll()
        # self.numShow.setFocus()
        # self.guessButton.clicked.connect(self.close)    
        # QMessageBox.about(self, 'see', 'yyy')  

    # def showMessageBox(self):
    #     guessNumber = int(self.numShow.text())
    #     print(guessNumber)
    #     self.numShow.selectAll()
    #     self.numShow.setFocus()

    #     if (guessNumber > self.num ):
    #         self.messageBox.about(self, 'SEE', 'TOO Big!')
    #         # self.numShow.setFocus()
            
    #     elif (guessNumber < self.num):
    #         self.messageBox.about(self, 'SEE', 'TOO Little')
    #         # self.numShow.setFocus()
    #     else:
    #         self.messageBox.about(self, 'SEE', 'Correct')
    #         self.num = randint(1, 100)
    #         self.numShow.clear()
    #         # self.numShow.setFocus()
    #         print(self.num)

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
            datas = self.inputText.toPlainText().split('/n')
            for s in datas:
                result += s + '\r\n'
                dec_cmd = RD505CMD(s)
                dec_cmd.cmd_check()
                decode_str = myprint_cmd4c(dec_cmd.data_decode_dict)
                for s in decode_str:
                    result += s + '\r\n'
                result += '----------------------------'
        except Exception as e:
            self.outputText.setPlainText(e)
            logging.debug(e)
            
            
        # print('haha')
        # self.outputText.setPlainText(self.inputText.toPlainText())
        self.outputText.setPlainText(result)
        # logging.debug(result)

    # @pyqtSlot()
    def on_ExitButton_clicked(self):
        print("haha")