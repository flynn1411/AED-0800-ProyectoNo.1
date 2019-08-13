# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Carpeta.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(377, 53)
        self.carpetastring = QtWidgets.QPlainTextEdit(Dialog)
        self.carpetastring.setGeometry(QtCore.QRect(10, 10, 301, 31))
        self.carpetastring.setObjectName("carpetastring")
        self.CCarpeta = QtWidgets.QPushButton(Dialog)
        self.CCarpeta.setGeometry(QtCore.QRect(332, 17, 41, 21))
        self.CCarpeta.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Iconos/accept.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CCarpeta.setIcon(icon)
        self.CCarpeta.setObjectName("CCarpeta")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
