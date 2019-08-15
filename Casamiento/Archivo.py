# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Archivo.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(373, 118)
        self.archivostring = QtWidgets.QPlainTextEdit(Dialog)
        self.archivostring.setGeometry(QtCore.QRect(10, 10, 301, 31))
        self.archivostring.setObjectName("archivostring")
        self.CArchivo = QtWidgets.QPushButton(Dialog)
        self.CArchivo.setGeometry(QtCore.QRect(330, 10, 41, 31))
        self.CArchivo.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Iconos/accept.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CArchivo.setIcon(icon)
        self.CArchivo.setObjectName("CArchivo")
        self.guardadoarchivo = QtWidgets.QTextEdit(Dialog)
        self.guardadoarchivo.setGeometry(QtCore.QRect(10, 80, 301, 31))
        self.guardadoarchivo.setObjectName("guardadoarchivo")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
