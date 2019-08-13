import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.uic import loadUi


class MainPage(QDialog):
    def __init__(self):
        #Cargar la UI
        super(MainPage, self).__init__()
        loadUi('Principal.ui', self)

        #Accion 
        self.carpeta.clicked.connect(self.abrir)

         
    def abrir(self):
        #Importar
        from Abrircarpeta import AbrirCarpeta
        a = AbrirCarpeta()

        #Accion 
        a.CCarpeta.clicked.connect(a.obtenerString)

        #Finalizar sin cerrar  
        a.exec_()
      
 
  
       
        

    
app=QApplication(sys.argv)
widget=MainPage()
widget.show()
sys.exit(app.exec_())  
