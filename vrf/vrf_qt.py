'''
Author: your name
Date: 2022-04-16 16:04:07
LastEditTime: 2022-04-23 21:44:52
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pyqt5\EX1GuessNum\guess_num_main.py
'''


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, showbase
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QApplication

from PyQt5.QtCore import pyqtSlot


import sys, os

sys.path.append("..")

print('cur path: ', os.getcwd())
print('sys path:', sys.path[0])


from vrf.ui_fun.fun_ui import FunVrfUi

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = FunVrfUi()
    ui.show()
    sys.exit(app.exec_())
