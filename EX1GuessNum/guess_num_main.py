'''
Author: your name
Date: 2022-04-16 16:04:07
LastEditTime: 2022-04-16 17:04:43
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pyqt5\EX1GuessNum\guess_num_main.py
'''
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, showbase
from PyQt5.QtWidgets import QFileDialog, QMainWindow
from function.func_guess_num import FunGuessNum
from PyQt5.QtCore import pyqtSlot

import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = FunGuessNum()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())