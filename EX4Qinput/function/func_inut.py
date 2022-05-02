'''
Author: your name
Date: 2022-04-29 23:50:58
LastEditTime: 2022-04-30 10:31:06
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pyqt5\EX4Qinput\function\func_inut.py
'''
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, showbase
from PyQt5.QtWidgets import QDialog, QFileDialog, QInputDialog, QMainWindow, QMessageBox
from random import randint

sys.path.append('../')

from ui.Ui_ui_input import Ui_MainWindow

class InputEvent(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None) -> None:
        super(InputEvent, self).__init__()
        self.setupUi(self)

        self.pushButtonName.clicked.connect(self.showDialog)
        self.pushButtonAge.clicked.connect(self.showDialog)
        self.pushButtonSex.clicked.connect(self.showDialog)
        self.pushButtonHeight.clicked.connect(self.showDialog)
        self.pushButtonInfo.clicked.connect(self.showDialog)


    def showDialog(self):
        sender = self.sender() 
        sex = ['man', 'woman']

        if sender == self.pushButtonName:
            text, ok = QInputDialog.getText(self, 'Edit name', 'Please input name:')
            if ok:
                self.labe_name_2.setText(text)

        elif sender == self.pushButtonAge:
            text, ok = QInputDialog.getInt(self, 'Edit age', 'Please input age:', min=1)
            if ok:
                self.label_age_2.setText(str(text))   # int to str
        
        elif sender == self.pushButtonSex:
            text, ok = QInputDialog.getItem(self, 'Edit sex','Please select sex:', sex)
            if ok:
                self.label_sex_2.setText(text)

        elif sender == self.pushButtonHeight:
            text, ok = QInputDialog.getDouble(self, 'Edit age', 'Please input age:', min=1.0)
            if ok:
                self.label_height_2.setText(str(text))   # int to str

        elif sender == self.pushButtonInfo:
            text, ok = QInputDialog.getMultiLineText(self, 'Edit info', 'Please input information:')
            if ok:
                self.textInformation.setText(text)

    
                