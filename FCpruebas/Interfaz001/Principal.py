# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Principal.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(710, 515)
        self.carpeta = QtWidgets.QPushButton(Dialog)
        self.carpeta.setGeometry(QtCore.QRect(40, 420, 81, 51))
        self.carpeta.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Iconos/folder.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.carpeta.setIcon(icon)
        self.carpeta.setIconSize(QtCore.QSize(60, 60))
        self.carpeta.setObjectName("carpeta")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
