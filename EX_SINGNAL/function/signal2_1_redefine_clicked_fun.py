'''
Author: your name
Date: 2022-05-15 11:29:18
LastEditTime: 2022-05-15 11:37:09
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pyqt5\EX_SINGNAL\function\signal2_1_clicked_fun.py
'''
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, showbase
from PyQt5.QtWidgets import QDialog, QFileDialog, QMainWindow, QMessageBox,QApplication

sys.path.append('..')


from ui.Ui_signal2_1_clicked import Ui_MainWindow

class SignalClickedWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None) -> None:
        super(SignalClickedWindow, self).__init__()
        self.setupUi(self)

        # 单击按钮时触发按钮内置的信号，绑定自定义的槽函数
        self.pushButton.clicked.connect(self.btn_close)

    def btn_close(self):
        print('redifine close signal')
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = SignalClickedWindow()
    ui.show()
    sys.exit(app.exec_())