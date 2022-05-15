'''
Author: your name
Date: 2022-05-15 11:29:18
LastEditTime: 2022-05-15 14:32:36
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pyqt5\EX_SINGNAL\function\signal2_1_clicked_fun.py
'''
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, pyqtSlot, showbase
from PyQt5.QtWidgets import QDialog, QFileDialog, QMainWindow, QMessageBox,QApplication

sys.path.append('..')


from ui.Ui_signal3_1_signal_emit import Ui_MainWindow

class SignalClickedWindow(QMainWindow, Ui_MainWindow):
    # 1.自定义信号，不带参数
    signal_no_param = pyqtSignal()
    signal_int = pyqtSignal(int)
    signal_int_str = pyqtSignal(int, str)
    signal_list = pyqtSignal(list)
    signal_dict = pyqtSignal(dict)
    signal_int_str_or_str = pyqtSignal([int, str], [str])

    def __init__(self, parent=None) -> None:
        super(SignalClickedWindow, self).__init__()
        self.setupUi(self)

        # 4.连接按键和信号发射
        self.pushButton_noParam.clicked.connect(self.signal_no_param_btn_clicked)
        self.pushButton_int.clicked.connect(self.signal_int_btn_clicked)
        self.pushButton_str.clicked.connect(self.signal_int_str_btn_clicked)
        self.pushButton_list.clicked.connect(self.signal_list_btn_clicked)
        self.pushButton_dict.clicked.connect(self.signal_dict_btn_clicked)
        self.pushButton_intNotStr.clicked.connect(self.signal_int_not_str_btn_clicked)
        self.pushButton_strNotInt.clicked.connect(self.signal_str_not_int_btn_clicked)

        # 3.连接 信号和槽
        self.signal_no_param.connect(self.sig_no_parm_clicked)
        self.signal_int.connect(self.sig_int_clicked)
        self.signal_int_str.connect(self.sig_int_str_clicked)
        self.signal_list.connect(self.sig_list_clicked)
        self.signal_dict.connect(self.sig_dict_clicked)
        self.signal_int_str_or_str[int, str].connect(self.sig_int_not_str_clicked)
        self.signal_int_str_or_str[str].connect(self.sig_str_not_int_clicked)

        # 6.自定义参数的传递给槽函数
        self.pushButton_1.clicked.connect(lambda: self.show_clicked(1))
        self.pushButton_2.clicked.connect(lambda: self.show_clicked(2))

    # 7.自定义参数的槽函数
    def show_clicked(self, name):
        print("button {}".format(name))
        QMessageBox.information(self, 'info', 'Button {}'.format(name))

        

    # 5.发送自定义信号
    def signal_no_param_btn_clicked(self):
        self.signal_no_param.emit()

    def signal_int_btn_clicked(self):
        self.signal_int.emit(1)
    
    def signal_int_str_btn_clicked(self):
        self.signal_int_str.emit(1, 'aaa')
    
    def signal_list_btn_clicked(self):
        self.signal_list.emit([1, 2, 3, 4])
    
    def signal_dict_btn_clicked(self):
        self.signal_dict.emit({'name':'jia', 'age':'21'})
    
    def signal_int_not_str_btn_clicked(self):
        self.signal_int_str_or_str[int, str].emit(1, 'six')
    
    def signal_str_not_int_btn_clicked(self):
        self.signal_int_str_or_str[str].emit('seven')

    # 2.自定义槽函数
    def sig_no_parm_clicked(self):
        print('sig no param emit')
        
    def sig_int_clicked(self, val):
        print('sig emit, val: ', val)

    def sig_int_str_clicked(self, val, text):
        print('sig emit, val:  ', val, text)

    def sig_list_clicked(self, val):
        print('sig emit, val: ', val)

    def sig_dict_clicked(self, val):
        print('sig emit, val: ', val)

    def sig_int_not_str_clicked(self, val, text):
        print('sig emit, val: ', val, text)
    
    def sig_str_not_int_clicked(self, val):
        print('sig emit, val: ', val)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = SignalClickedWindow()
    ui.show()
    sys.exit(app.exec_())