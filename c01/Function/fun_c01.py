import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, showbase
from PyQt5.QtWidgets import QFileDialog, QMainWindow

sys.path.append('../')

from UI.Ui_c01 import Ui_MainWindow

class fun_main(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None) -> None:
        super(fun_main, self).__init__()
        self.setupUi(self)

        self.buttonClose.clicked.connect(self.close)
        #file close
        self.fileClose.triggered.connect(self.close)

        #file open 
        self.fileOpen.triggered.connect(self.openMsg)


        #self.ButtonCalc.clicked.connect(self.on_ButtonCalc_clicked())

        
    @pyqtSlot()
    def on_ButtonCalc_clicked(self):
        print("haha")

    def openMsg(self):
        file, ok = QFileDialog.getOpenFileName(self, 'open', "c:/", "ALL Files (*)")
        #self.statusBar.showMessage(file)



        