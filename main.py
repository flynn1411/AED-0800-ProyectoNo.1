# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fileExplorer.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FileExplorer(object):
    def setupUi(self, FileExplorer):
        FileExplorer.setObjectName("FileExplorer")
        FileExplorer.setEnabled(True)
        FileExplorer.resize(766, 490)
        FileExplorer.setStyleSheet("color: rgb(238, 238, 236);\n"
"background-color: rgb(243, 243, 243);")
        self.centralwidget = QtWidgets.QWidget(FileExplorer)
        self.centralwidget.setObjectName("centralwidget")
        self.deleteLeft = QtWidgets.QPushButton(self.centralwidget)
        self.deleteLeft.setGeometry(QtCore.QRect(260, 380, 51, 61))
        self.deleteLeft.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/svgs/svg/delete.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteLeft.setIcon(icon)
        self.deleteLeft.setIconSize(QtCore.QSize(60, 60))
        self.deleteLeft.setFlat(True)
        self.deleteLeft.setObjectName("deleteLeft")
        self.leftTree = QtWidgets.QListWidget(self.centralwidget)
        self.leftTree.setGeometry(QtCore.QRect(30, 20, 291, 341))
        self.leftTree.setStyleSheet("background-color: rgb(227, 226, 226);")
        self.leftTree.setObjectName("leftTree")
        self.addDirectoryLeft = QtWidgets.QPushButton(self.centralwidget)
        self.addDirectoryLeft.setGeometry(QtCore.QRect(140, 380, 81, 61))
        self.addDirectoryLeft.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/svgs/svg/folder.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addDirectoryLeft.setIcon(icon1)
        self.addDirectoryLeft.setIconSize(QtCore.QSize(80, 60))
        self.addDirectoryLeft.setFlat(True)
        self.addDirectoryLeft.setObjectName("addDirectoryLeft")
        self.addFileLeft = QtWidgets.QPushButton(self.centralwidget)
        self.addFileLeft.setGeometry(QtCore.QRect(60, 380, 41, 61))
        self.addFileLeft.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/svgs/svg/file.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addFileLeft.setIcon(icon2)
        self.addFileLeft.setIconSize(QtCore.QSize(60, 60))
        self.addFileLeft.setFlat(True)
        self.addFileLeft.setObjectName("addFileLeft")
        self.rightTree = QtWidgets.QListWidget(self.centralwidget)
        self.rightTree.setGeometry(QtCore.QRect(440, 20, 291, 341))
        self.rightTree.setStyleSheet("background-color: rgb(227, 226, 226);")
        self.rightTree.setObjectName("rightTree")
        self.deleteRight = QtWidgets.QPushButton(self.centralwidget)
        self.deleteRight.setGeometry(QtCore.QRect(670, 380, 51, 61))
        self.deleteRight.setText("")
        self.deleteRight.setIcon(icon)
        self.deleteRight.setIconSize(QtCore.QSize(60, 60))
        self.deleteRight.setFlat(True)
        self.deleteRight.setObjectName("deleteRight")
        self.addDirectoryLeft_2 = QtWidgets.QPushButton(self.centralwidget)
        self.addDirectoryLeft_2.setGeometry(QtCore.QRect(570, 380, 81, 61))
        self.addDirectoryLeft_2.setText("")
        self.addDirectoryLeft_2.setIcon(icon1)
        self.addDirectoryLeft_2.setIconSize(QtCore.QSize(80, 60))
        self.addDirectoryLeft_2.setFlat(True)
        self.addDirectoryLeft_2.setObjectName("addDirectoryLeft_2")
        self.addFileLeft_2 = QtWidgets.QPushButton(self.centralwidget)
        self.addFileLeft_2.setGeometry(QtCore.QRect(490, 380, 41, 61))
        self.addFileLeft_2.setText("")
        self.addFileLeft_2.setIcon(icon2)
        self.addFileLeft_2.setIconSize(QtCore.QSize(60, 60))
        self.addFileLeft_2.setFlat(True)
        self.addFileLeft_2.setObjectName("addFileLeft_2")
        self.left2right = QtWidgets.QPushButton(self.centralwidget)
        self.left2right.setGeometry(QtCore.QRect(340, 110, 91, 61))
        self.left2right.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/svgs/svg/left2right.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.left2right.setIcon(icon3)
        self.left2right.setIconSize(QtCore.QSize(80, 80))
        self.left2right.setFlat(True)
        self.left2right.setObjectName("left2right")
        self.right2left = QtWidgets.QPushButton(self.centralwidget)
        self.right2left.setGeometry(QtCore.QRect(340, 190, 91, 61))
        self.right2left.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/svgs/svg/right2left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.right2left.setIcon(icon4)
        self.right2left.setIconSize(QtCore.QSize(80, 80))
        self.right2left.setFlat(True)
        self.right2left.setObjectName("right2left")
        FileExplorer.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(FileExplorer)
        self.statusbar.setObjectName("statusbar")
        FileExplorer.setStatusBar(self.statusbar)

        self.retranslateUi(FileExplorer)
        QtCore.QMetaObject.connectSlotsByName(FileExplorer)

    def retranslateUi(self, FileExplorer):
        _translate = QtCore.QCoreApplication.translate
        FileExplorer.setWindowTitle(_translate("FileExplorer", "FileExplorer"))
import Nucleo.icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FileExplorer = QtWidgets.QMainWindow()
    ui = Ui_FileExplorer()
    ui.setupUi(FileExplorer)
    FileExplorer.show()
    sys.exit(app.exec_())
