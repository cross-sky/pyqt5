'''
Author: your name
Date: 2022-04-30 00:00:19
LastEditTime: 2022-04-30 00:00:19
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pyqt5\EX4Qinput\main_qt.py
'''
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, showbase
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QApplication
from function.func_inut import InputEvent
from PyQt5.QtCore import pyqtSlot

import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = InputEvent()
    ui.show()
    sys.exit(app.exec_())