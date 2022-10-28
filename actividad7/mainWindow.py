import PySide2
from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from admin import Admin
from particula import Particula
from algoritmos import distacia_euclidiana

class MainWIndow(QMainWindow):
    def __init__(self):
        super(MainWIndow,self).__init__()

        self.admin=Admin()

        self.ui=Ui_MainWindow()
        self.ui.setupUi(self) ##mete la intrerfaz
        self.ui.Agre_Final_buttom.clicked.connect(self.click_agregar) ##conectar clase a boton
        self.ui.Agre_Inicio_Buttom.clicked.connect(self.click_agregar_inicio)
        self.ui.Mostrar_buttom.clicked.connect(self.click_mostrar)


        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar)


    @Slot()
    def action_abrir_archivo(self):
        #print("abrir archivo")
        ubicacion=QFileDialog.getOpenFileName(
            self,
            "abrir archivo",
            ".",
            "JSON (*.json)"
        )[0]
        if self.admin.open(ubicacion):
            QMessageBox.information(
                 self,
                "exito",
                "Se abrio el archivo"+ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "Error abrir archivo "
            ) 
        
        

    @Slot()
    def action_guardar(self):
       #print("guardar")
       ubicacion= QFileDialog.getSaveFileName(
        self,
        'Guardar Archivo',
        '.',
        'JSON (*.json)'
       )[0]
       print( ubicacion)
       self.admin.save(ubicacion)
       if self.admin.save(ubicacion):
            QMessageBox.information(
                self,
                "exito",
                "se pudo crear archivo"+ubicacion
            )
       else:
            QMessageBox.critical(
                self,
                "Error",
                "no se pudo crear archivo"
            )
            

    @Slot()
    def click_agregar(self):
            id=self.ui.Id_spinBox.value()
            OrigenX=self.ui.OrigenX_spinBox.value()
            OrigenY=self.ui.OrigenY_spinBox.value()
            DestinoX=self.ui.DestinoX_spinBox.value()
            DestinoY=self.ui.DestinoY_spinBox.value()
            Velocidad=self.ui.Velocidad_spinBox.value()
            Red=self.ui.Red_spinBox.value()
            Green=self.ui.Green_spinBox.value()
            Blue=self.ui.Blue_spinBox.value()
            distancia=distacia_euclidiana

            particula=Particula(id,OrigenX,OrigenY,DestinoX,DestinoY,Velocidad, Red,Green,Blue,distancia)
            self.admin.agregar_final(particula)

            #print(OrigenX,OrigenY, DestinoX,DestinoY,Velocidad,Red,Green,Blue)
            #self.ui.salida.insertPlainText(str(OrigenX) + str( OrigenY) + str(DestinoX) + str (DestinoY) + str (Velocidad) +str( Red)+ str(Green) + str(Blue))
    @Slot()
    def click_agregar_inicio(self):
            id=self.ui.Id_spinBox.value()
            OrigenX=self.ui.OrigenX_spinBox.value()
            OrigenY=self.ui.OrigenY_spinBox.value()
            DestinoX=self.ui.DestinoX_spinBox.value()
            DestinoY=self.ui.DestinoY_spinBox.value()
            Velocidad=self.ui.Velocidad_spinBox.value()
            Red=self.ui.Red_spinBox.value()
            Green=self.ui.Green_spinBox.value()
            Blue=self.ui.Blue_spinBox.value()
            distancia=distacia_euclidiana
           
            particula=Particula(id,OrigenX,OrigenY,DestinoX,DestinoY,Velocidad, Red,Green,Blue,distancia)
            self.admin.agregar_inicio(particula)

    @Slot()
    def click_mostrar(self):
           # self.admin.mostrar()
            self.ui.salida.clear()
            self.ui.salida.insertPlainText(str(self.admin))