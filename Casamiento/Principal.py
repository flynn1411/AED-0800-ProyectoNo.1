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
        Dialog.setStyleSheet("")
        self.o = QtWidgets.QPushButton(Dialog)
        self.o.setGeometry(QtCore.QRect(10, 0, 21, 28))
        self.o.setObjectName("o")
        self.Lista = QtWidgets.QListWidget(Dialog)
        self.Lista.setGeometry(QtCore.QRect(9, 29, 311, 391))
        self.Lista.setObjectName("Lista")
        self.carpeta = QtWidgets.QPushButton(Dialog)
        self.carpeta.setGeometry(QtCore.QRect(10, 430, 80, 68))
        self.carpeta.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Iconos/folder.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.carpeta.setIcon(icon)
        self.carpeta.setIconSize(QtCore.QSize(60, 60))
        self.carpeta.setObjectName("carpeta")
        self.archivo = QtWidgets.QPushButton(Dialog)
        self.archivo.setGeometry(QtCore.QRect(100, 430, 80, 68))
        self.archivo.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Iconos/file.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.archivo.setIcon(icon1)
        self.archivo.setIconSize(QtCore.QSize(60, 60))
        self.archivo.setObjectName("archivo")

        self.retranslateUi(Dialog)
        self.o.clicked.connect(self.Lista.clear)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.o.setText(_translate("Dialog", "o"))
