'''
Author: your name
Date: 2022-05-15 11:29:18
LastEditTime: 2022-05-15 22:16:49
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pyqt5\EX_SINGNAL\function\signal2_1_clicked_fun.py
'''
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, showbase
from PyQt5.QtWidgets import QDialog, QFileDialog, QMainWindow, QMessageBox,QApplication
from signal5_1_mulwindow_childdialog_fun import MultWindChildDialogWindow

sys.path.append('..')


from ui.Ui_signal5_mulwindow_main import Ui_MainWindow

class SignalClickedWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None) -> None:
        super(SignalClickedWindow, self).__init__()
        self.setupUi(self)

        self.pushButton_new.clicked.connect(self.onButtonNewClicked)
        self.pushButton_attr.clicked.connect(self.onButtonAttrClicked)
        self.pushButton_signal.clicked.connect(self.openDialog)
        
    def onButtonNewClicked(self):
        dialog = MultWindChildDialogWindow(self)
        result = dialog.exec_()
        date = dialog.dateTime()
        if result:
            self.textDisplay.setText(date.date().toString())
        print('1result = ', result)
    
    def onButtonAttrClicked(self):
        date, time, result = MultWindChildDialogWindow.getDateTime()
        if result:
            self.textDisplay.setText(date.toString())
        print('2result = ', result)

    # open dialog and recv signal
    def openDialog(self):
        dialog = MultWindChildDialogWindow(self)
        dialog.sigOn.connect(self.deal_emit_slot)
        dialog.exec_()

    def deal_emit_slot(self, datestr):
        self.textDisplay.setText(datestr)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = SignalClickedWindow()
    ui.show()
    sys.exit(app.exec_())