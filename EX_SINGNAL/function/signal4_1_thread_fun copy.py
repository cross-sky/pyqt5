'''
Author: your name
Date: 2022-05-15 11:29:18
LastEditTime: 2022-05-15 21:04:58
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pyqt5\EX_SINGNAL\function\signal2_1_clicked_fun.py
'''
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, pyqtSlot, showbase, QThread,  QDateTime
from PyQt5.QtWidgets import QDialog, QFileDialog, QMainWindow, QMessageBox,QApplication
import time
sys.path.append('..')


from ui.Ui_signal4_1_thread import Ui_MainWindow

class MyThread(QThread):
    #自定义信号为str参数类型
    sinOut = pyqtSignal(str)
    sinDate = pyqtSignal(str)

    def __init__(self, parent=None) -> None:
        super(MyThread, self).__init__(parent=parent)
        self.identify = None
        self.times = 0

    def setIndentify(self, text):
        self.identify = text

    def setValue(self, value):
        self.times = value

    def run(self):
        while True:
            if self.times > 0 and self.identify :
                self.sinOut.emit(str(self.times))
                self.times -= 1
                # print('val ', self.times)
            
            #获得当前系统时间
            #设置时间显示格式
            data = QDateTime.currentDateTime()
            curTime = data.toString('yyyy-MM-dd hh:mm:ss dddd')
            #发射信号
            self.sinDate.emit(str(curTime))
            time.sleep(1)
            
class SignalClickedWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None) -> None:
        super(SignalClickedWindow, self).__init__()
        self.setupUi(self)

        # # 单击按钮时触发内置的信号clicked，绑定窗口内置的槽函数
        # self.pushButton.clicked.connect(self.close)
        self.bdThread = MyThread()
        self.bdThread.setIndentify('time')
        
        self.pbSetValue.clicked.connect(self.setButtonClicked)

        # #信号连接到界面显示槽函数
        self.bdThread.sinOut.connect(self.valueDispSlot)
        self.bdThread.sinDate.connect(self.dateDispSlot)

        # thread start
        self.bdThread.start()

    # send 槽函数
    def setButtonClicked(self):
        #发射信号
        self.bdThread.setValue(10000)

    # rec 槽函数
    def valueDispSlot(self, value):
        self.valueDisp.setText(value)

    def dateDispSlot(self, value):
        self.dateDisplay.setText(value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = SignalClickedWindow()
    ui.show()
    sys.exit(app.exec_())