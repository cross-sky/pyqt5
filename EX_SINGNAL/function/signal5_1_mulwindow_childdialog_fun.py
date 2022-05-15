'''
Author: your name
Date: 2022-05-15 11:29:18
LastEditTime: 2022-05-15 22:10:19
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pyqt5\EX_SINGNAL\function\signal2_1_clicked_fun.py
'''
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, pyqtSlot, showbase
from PyQt5.QtWidgets import QDialog, QFileDialog, QMainWindow, QMessageBox,QApplication

sys.path.append('..')


from ui.Ui_signal5_mulwindow_childdialog import Ui_Dialog

class MultWindChildDialogWindow(QDialog, Ui_Dialog):
    sigOn = pyqtSignal(str)
    
    def __init__(self, parent=None) -> None:
        super(MultWindChildDialogWindow, self).__init__()
        self.setupUi(self)

        # bind emit signal
        self.dateTimeEdit.dateChanged.connect(self.emit_signal)
    
    # emit function
    def emit_signal(self):
        date_str = self.dateTimeEdit.dateTime().toString()
        self.sigOn.emit(date_str)

    # redefine accept
    def accept(self) -> None:
        print('haha')
        return super().accept()

    def dateTime(self):
        return self.dateTimeEdit.dateTime()

    @staticmethod
    def getDateTime(parent=None):
        dialog = MultWindChildDialogWindow(parent)
        result = dialog.exec_()
        date = dialog.dateTime()
        return (date.date(), date.time(), result==QDialog.Accepted)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MultWindChildDialogWindow()
    ui.show()
    sys.exit(app.exec_())