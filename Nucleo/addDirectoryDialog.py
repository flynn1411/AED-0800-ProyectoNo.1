# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addDirectoryDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddDirectoryDialog(object):
    def setupUi(self, AddDirectoryDialog):
        AddDirectoryDialog.setObjectName("AddDirectoryDialog")
        AddDirectoryDialog.resize(394, 62)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/svgs/svg/file.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AddDirectoryDialog.setWindowIcon(icon)
        AddDirectoryDialog.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.addName = QtWidgets.QPushButton(AddDirectoryDialog)
        self.addName.setGeometry(QtCore.QRect(300, 10, 41, 41))
        self.addName.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/svgs/svg/accept.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addName.setIcon(icon1)
        self.addName.setIconSize(QtCore.QSize(30, 30))
        self.addName.setFlat(True)
        self.addName.setObjectName("addName")
        self.cancel = QtWidgets.QPushButton(AddDirectoryDialog)
        self.cancel.setGeometry(QtCore.QRect(350, 10, 41, 41))
        self.cancel.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/svgs/svg/close.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancel.setIcon(icon2)
        self.cancel.setIconSize(QtCore.QSize(30, 30))
        self.cancel.setFlat(True)
        self.cancel.setObjectName("cancel")
        self.nameInput = QtWidgets.QLineEdit(AddDirectoryDialog)
        self.nameInput.setGeometry(QtCore.QRect(10, 20, 271, 25))
        self.nameInput.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.nameInput.setInputMask("")
        self.nameInput.setText("")
        self.nameInput.setObjectName("nameInput")

        self.retranslateUi(AddDirectoryDialog)
        self.cancel.clicked.connect(AddDirectoryDialog.close)
        QtCore.QMetaObject.connectSlotsByName(AddDirectoryDialog)

    def retranslateUi(self, AddDirectoryDialog):
        _translate = QtCore.QCoreApplication.translate
        AddDirectoryDialog.setWindowTitle(_translate("AddDirectoryDialog", "Add Directory"))
import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddDirectoryDialog = QtWidgets.QDialog()
    ui = Ui_AddDirectoryDialog()
    ui.setupUi(AddDirectoryDialog)
    AddDirectoryDialog.show()
    sys.exit(app.exec_())
