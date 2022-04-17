import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import sip
from PyQt5.QtWidgets import QApplication

from Function.fun_c01 import fun_main

if __name__ == "__main__":
    # app = QtWidgets.QApplication(sys.argv)
    # uiMainWindow = QtWidgets.QMainWindow()
    # ui = fun_main()
    # ui.setupUi(uiMainWindow)
    # uiMainWindow.show()
    # sys.exit(app.exec_())

    app = QApplication(sys.argv)
    ui = fun_main()
    ui.show()
    sys.exit(app.exec_())
    



