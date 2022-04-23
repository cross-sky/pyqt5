'''
Author: your name
Date: 2022-04-16 15:24:36
LastEditTime: 2022-04-18 23:31:54
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pyqt5\EX1GuessNum\function\func_guess_num.py
'''
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, showbase
from PyQt5.QtWidgets import QDialog, QFileDialog, QMainWindow, QMessageBox
from random import randint

# sys.path.append('../')
from ui.Ui_event import Ui_MainWindow


class FunEvent(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None) -> None:
        super(FunEvent, self).__init__()
        self.setupUi(self)

        self.messageBox = QMessageBox()
        # self.guessButton.clicked.connect(self.close)    

    def buttonClicked(self):
        computer = randint(1, 3)
        player = 0
        sender = self.sender()

        if sender.text() == 'scissors':
            player = 1
        elif sender.text() == 'rock':
            player = 2
        else:
            player = 3  # 'paper'

        if player == computer:
            self.messageBox.about(self, '结果', '平手')
        elif player == 1 and computer == 2:
            self.messageBox.about(self, '结果', '电脑：石头，电脑赢了')
        elif player == 1 and computer == 3:
            self.messageBox.about(self, '结果', '电脑：布，玩家赢了')
        elif player == 2 and computer == 1:
            self.messageBox.about(self, '结果', '电脑：剪刀，玩家赢了')
        elif player == 2 and computer == 3:
            self.messageBox.about(self, '结果', '电脑：布，电脑赢了')
        elif player == 3 and computer == 1:
            self.messageBox.about(self, '结果', '电脑：剪刀，电脑赢了')
        elif player == 3 and computer == 2:
            self.messageBox.about(self, '结果', '电脑：石头，玩家赢了')
        

    def closeEvent(self, event):
        reply = self.messageBox.question(self, 'MAKE', 'EXIT?', QMessageBox.Yes,QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    @pyqtSlot()
    def on_rockButton_clicked(self):
        self.buttonClicked()
    
    @pyqtSlot()
    def on_paperButton_clicked(self):
        self.buttonClicked()

    @pyqtSlot()
    def on_scissorsButton_clicked(self):
        self.buttonClicked()


            