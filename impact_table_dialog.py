# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'impact_table.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dlgImpact(object):
    def setupUi(self, dlgImpact):
        dlgImpact.setObjectName("dlgImpact")
        dlgImpact.resize(640, 480)
        self.tblImpacts = QtWidgets.QTableWidget(dlgImpact)
        self.tblImpacts.setGeometry(QtCore.QRect(10, 10, 621, 461))
        self.tblImpacts.setAlternatingRowColors(True)
        self.tblImpacts.setObjectName("tblImpacts")
        self.tblImpacts.setColumnCount(3)
        self.tblImpacts.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblImpacts.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblImpacts.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblImpacts.setHorizontalHeaderItem(2, item)

        self.retranslateUi(dlgImpact)
        QtCore.QMetaObject.connectSlotsByName(dlgImpact)

    def retranslateUi(self, dlgImpact):
        _translate = QtCore.QCoreApplication.translate
        dlgImpact.setWindowTitle(_translate("dlgImpact", "Impacts Table"))
        item = self.tblImpacts.horizontalHeaderItem(0)
        item.setText(_translate("dlgImpact", "Project"))
        item = self.tblImpacts.horizontalHeaderItem(1)
        item.setText(_translate("dlgImpact", "Type"))
        item = self.tblImpacts.horizontalHeaderItem(2)
        item.setText(_translate("dlgImpact", "Distance"))
