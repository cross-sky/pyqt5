'''
Author: your name
Date: 2022-04-16 13:09:25
LastEditTime: 2022-04-16 13:09:27
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pyqt5\hello\hellolcd.py
'''

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, showbase
from PyQt5.QtWidgets import QFileDialog, QMainWindow
from ui.Ui_hello import Ui_Dialog

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
