# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from windows.login_pass import LoginPass

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = LoginPass()
    main.show()
    sys.exit(app.exec_())
