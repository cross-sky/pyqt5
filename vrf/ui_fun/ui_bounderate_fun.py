'''
Author: your name
Date: 2022-05-11 23:37:08
LastEditTime: 2022-05-11 23:55:18
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: r"\\pyqt5\\vrf\\ui_fun\\ui_bounderate_fun.py"
'''




import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, showbase
from PyQt5.QtWidgets import QDialog, QFileDialog, QMainWindow, QMessageBox,QApplication
from random import randint

sys.path.append('..')

from ui.Ui_ui_boundrate import Ui_MainWindow
# from vrf.vrf_cmd_print import *

class BoundRateVrfUi(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None) -> None:
        super(BoundRateVrfUi, self).__init__()
        self.setupUi(self)

        self.comboBox_boundrate.addItems(["2400", "9600", "57600", "115200"])
        self.comboBox_bits.addItems(["8", "9" , '10'])
        self.comboBox_cc.addItems(['None', 'odd', 'even'])
        self.comboBox_flow.addItems(['no', 'yes'])


    # @pyqtSlot()
    # def on_decodeButton_clicked(self):
    #     result = ''
    #     try:
    #         datas = self.inputText.toPlainText().split('\n')
    #         logging.debug('datas: ' + str(datas))
    #         for s in datas:
    #             logging.debug('-'+s+'-')
    #             result += s + '\r\n'
    #             dec_cmd = RD505CMD(s)
    #             dec_cmd.cmd_check()
    #             # decode_str = myprint_cmd0x4c_request(dec_cmd.data_decode_dict)
    #             decode_str = eval(dec_cmd.data_decode_dict.get(MYPRINT_FUNCTION))(dec_cmd.data_decode_dict)
    #             for s in decode_str:
    #                 result += s + '\r\n'
    #             result += '----------------------------\r\n'
    #     except Exception as e:
    #         # self.outputText.setPlainText('len, fcc ok, may be data is fake cmd or data.' + str(e))
    #         result += 'len, fcc ok, may be data is fake cmd or data.' + str(e)
    #         logging.debug(e)
            
            
    #     # print('haha')
    #     # self.outputText.setPlainText(self.inputText.toPlainText())
    #     self.outputText.setPlainText(result)
    #     # logging.debug(result)

    # # @pyqtSlot()
    # def on_ExitButton_clicked(self):
    #     print("haha")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = BoundRateVrfUi()
    ui.show()
    sys.exit(app.exec_())
