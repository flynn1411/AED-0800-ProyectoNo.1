# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addFileDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddFileDialog(object):
    def setupUi(self, AddFileDialog):
        AddFileDialog.setObjectName("AddFileDialog")
        AddFileDialog.resize(394, 62)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/svgs/svg/file.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AddFileDialog.setWindowIcon(icon)
        AddFileDialog.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.addName = QtWidgets.QPushButton(AddFileDialog)
        self.addName.setGeometry(QtCore.QRect(300, 10, 41, 41))
        self.addName.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/svgs/svg/accept.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addName.setIcon(icon1)
        self.addName.setIconSize(QtCore.QSize(30, 30))
        self.addName.setFlat(True)
        self.addName.setObjectName("addName")
        self.cancel = QtWidgets.QPushButton(AddFileDialog)
        self.cancel.setGeometry(QtCore.QRect(350, 10, 41, 41))
        self.cancel.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/svgs/svg/close.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancel.setIcon(icon2)
        self.cancel.setIconSize(QtCore.QSize(30, 30))
        self.cancel.setFlat(True)
        self.cancel.setObjectName("cancel")
        self.nameInput = QtWidgets.QLineEdit(AddFileDialog)
        self.nameInput.setGeometry(QtCore.QRect(10, 20, 271, 25))
        self.nameInput.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.nameInput.setInputMask("")
        self.nameInput.setText("")
        self.nameInput.setObjectName("nameInput")

        self.retranslateUi(AddFileDialog)
        self.cancel.clicked.connect(AddFileDialog.close)
        QtCore.QMetaObject.connectSlotsByName(AddFileDialog)

    def retranslateUi(self, AddFileDialog):
        _translate = QtCore.QCoreApplication.translate
        AddFileDialog.setWindowTitle(_translate("AddFileDialog", "Add File"))
import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddFileDialog = QtWidgets.QDialog()
    ui = Ui_AddFileDialog()
    ui.setupUi(AddFileDialog)
    AddFileDialog.show()
    sys.exit(app.exec_())
