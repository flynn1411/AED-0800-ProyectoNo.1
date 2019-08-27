# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddFile.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(369, 49)
        self.FileName = QtWidgets.QTextEdit(Dialog)
        self.FileName.setGeometry(QtCore.QRect(10, 10, 301, 31))
        self.FileName.setObjectName("FileName")
        self.ConfirmFile = QtWidgets.QPushButton(Dialog)
        self.ConfirmFile.setGeometry(QtCore.QRect(320, 10, 41, 31))
        self.ConfirmFile.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../LunaDeMielWIP/Nucleo/Iconos/accept.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ConfirmFile.setIcon(icon)
        self.ConfirmFile.setIconSize(QtCore.QSize(39, 25))
        self.ConfirmFile.setObjectName("ConfirmFile")

        self.retranslateUi(Dialog)
        self.ConfirmFile.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
