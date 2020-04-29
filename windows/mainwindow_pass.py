# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow, QAbstractItemView, QTableWidgetItem
from Sql.Sql import MySql
from ui.mainwindow import Ui_MainWindow as mainWindowUI
from windows.add_pass import AddPass


class MainWindow(mainWindowUI, QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        MySql.createTable()
        self.tableWidget.setColumnHidden(0, True)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.flushTable()
        self.addBtn.clicked.connect(self.addDef)
        self.delBtn.clicked.connect(self.delDef)
        self.quitBtn.clicked.connect(self.quitDef)

    def flushTable(self):
        data_list = MySql.getData()
        self.tableWidget.setRowCount(len(data_list))
        for index in range(len(data_list)):
            self.tableWidget.setItem(index, 0, QTableWidgetItem(str(data_list[index][0])))
            self.tableWidget.setItem(index, 1, QTableWidgetItem(data_list[index][1]))
            self.tableWidget.setItem(index, 2, QTableWidgetItem(data_list[index][2]))
            self.tableWidget.setItem(index, 3, QTableWidgetItem(data_list[index][3]))

    def addDef(self):
        add_from = AddPass()
        add_from.main_handle = self
        add_from.exec_()

    def delDef(self):
        selected_row = self.tableWidget.selectedItems()
        del_row = self.tableWidget.row(selected_row[0])
        num = self.tableWidget.item(del_row, 0).text()
        MySql.delDef(num)
        self.flushTable()

    def quitDef(self):
        self.close()
