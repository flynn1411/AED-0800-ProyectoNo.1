# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddFolder.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(371, 48)
        self.FolderName = QtWidgets.QTextEdit(Dialog)
        self.FolderName.setGeometry(QtCore.QRect(10, 10, 301, 31))
        self.FolderName.setObjectName("FolderName")
        self.ConfirmFolder = QtWidgets.QPushButton(Dialog)
        self.ConfirmFolder.setGeometry(QtCore.QRect(320, 9, 41, 31))
        self.ConfirmFolder.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../LunaDeMielWIP/Nucleo/Iconos/accept.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ConfirmFolder.setIcon(icon)
        self.ConfirmFolder.setIconSize(QtCore.QSize(39, 25))
        self.ConfirmFolder.setObjectName("ConfirmFolder")

        self.retranslateUi(Dialog)
        self.ConfirmFolder.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
