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
        FileExplorer.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(FileExplorer)
        self.statusbar.setObjectName("statusbar")
        FileExplorer.setStatusBar(self.statusbar)

        self.retranslateUi(FileExplorer)
        QtCore.QMetaObject.connectSlotsByName(FileExplorer)

    def retranslateUi(self, FileExplorer):
        _translate = QtCore.QCoreApplication.translate
        FileExplorer.setWindowTitle(_translate("FileExplorer", "FileExplorer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FileExplorer = QtWidgets.QMainWindow()
    ui = Ui_FileExplorer()
    ui.setupUi(FileExplorer)
    FileExplorer.show()
    sys.exit(app.exec_())
