'''
Author: your name
Date: 2022-05-15 11:29:18
LastEditTime: 2022-05-15 11:43:09
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pyqt5\EX_SINGNAL\function\signal2_1_clicked_fun.py
'''
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, pyqtSlot, showbase
from PyQt5.QtWidgets import QDialog, QFileDialog, QMainWindow, QMessageBox,QApplication

sys.path.append('..')


from ui.Ui_signal2_1_clicked import Ui_MainWindow

class SignalClickedWindow(QMainWindow, Ui_MainWindow):
    # 自定义信号，不带参数
    button_clicked_signal = pyqtSignal()

    def __init__(self, parent=None) -> None:
        super(SignalClickedWindow, self).__init__()
        self.setupUi(self)

        # 连接 信号和槽
        self.pushButton.clicked.connect(self.btn_clicked)

        # 接收信号，连接到槽
        self.button_clicked_signal.connect(self.close)
        
    # 发送自定义信号，无参数
    def btn_clicked(self):
        print('redifine signal clicked')
        self.button_clicked_signal.emit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = SignalClickedWindow()
    ui.show()
    sys.exit(app.exec_())