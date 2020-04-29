# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QDialog
from Sql.Sql import MySql
from ui.add import Ui_Dialog as addPassUI


class AddPass(addPassUI, QDialog):
    def __init__(self):
        super(AddPass, self).__init__()
        self.setupUi(self)
        self.ensureBtn.clicked.connect(self.ensureClick)
        self.cancelBtn.clicked.connect(self.closeClick)

    def ensureClick(self):
        condition = self.condition.text()
        username = self.username.text()
        password = self.password.text()
        MySql.addDef(condition, username, password)
        self.main_handle.flushTable()
        self.close()

    def closeClick(self):
        self.close()
