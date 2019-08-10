pyuic5 -x fileExplorer.ui -o main.py
pyuic5 -x addFileDialog.ui -o addFileDialog.py
pyuic5 -x addDirectoryDialog.ui -o addDirectoryDialog.py
pyrcc5 -o icon_rc.py icons.qrc
