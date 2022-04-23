'''
Author: your name
Date: 2022-04-16 15:24:36
LastEditTime: 2022-04-18 23:13:18
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pyqt5\EX1GuessNum\function\func_guess_num.py
'''
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, showbase
from PyQt5.QtWidgets import QDialog, QFileDialog, QMainWindow, QMessageBox
from random import randint

sys.path.append('../')
from ui.Ui_guess_num_mainwindow import Ui_MainWindow


class FunGuessNum(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None) -> None:
        super(FunGuessNum, self).__init__()
        self.setupUi(self)

        self.messageBox = QMessageBox()
        self.num = randint(1, 100)
        print(self.num)
        self.numShow.selectAll()
        self.numShow.setFocus()
        # self.guessButton.clicked.connect(self.close)    

    def showMessageBox(self):
        guessNumber = int(self.numShow.text())
        print(guessNumber)
        self.numShow.selectAll()
        self.numShow.setFocus()

        if (guessNumber > self.num ):
            self.messageBox.about(self, 'SEE', 'TOO Big!')
            # self.numShow.setFocus()
            
        elif (guessNumber < self.num):
            self.messageBox.about(self, 'SEE', 'TOO Little')
            # self.numShow.setFocus()
        else:
            self.messageBox.about(self, 'SEE', 'Correct')
            self.num = randint(1, 100)
            self.numShow.clear()
            # self.numShow.setFocus()
            print(self.num)

    def closeEvent(self, event):
        reply = self.messageBox.question(self, 'MAKE', 'EXIT?', QMessageBox.Yes,QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    @pyqtSlot()
    def on_guessButton_clicked(self):
        print('haha')
        self.showMessageBox()

    # @pyqtSlot()
    def on_ExitButton_clicked(self):
        print("haha")
            