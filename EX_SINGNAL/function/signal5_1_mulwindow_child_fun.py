'''
Author: your name
Date: 2022-05-15 11:29:18
LastEditTime: 2022-05-15 21:32:54
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pyqt5\EX_SINGNAL\function\signal2_1_clicked_fun.py
'''
from _typeshed import Self
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, showbase
from PyQt5.QtWidgets import QDialog, QFileDialog, QMainWindow, QMessageBox,QApplication

sys.path.append('..')


from ui.Ui_signal5_mulwindow_child import Ui_MainWindow

class MultWindChildWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None) -> None:
        super(MultWindChildWindow, self).__init__()
        self.setupUi(self)
        self.result = False

        self.buttonBox_check.accepted.connect(self.btn_ok)
        self.buttonBox_check.rejected.connect(self.btn_cancel)
    
    def btn_ok(self):
        print('ok')
        self.result = True
        self.close()
        
        # return True

    def btn_cancel(self):
        print('cancel')
        self.result = False
        self.close()
        # return False
    
    def dateTime(self):
        return self.dateTimeEdit.dateTime()

    def getDateTime(parent=None):
        dialog = MultWindChildWindow(parent)
        result = dialog.show()
        date = dialog.dateTime()
        return (date.date(), date.time(), result)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MultWindChildWindow()
    ui.show()
    sys.exit(app.exec_())