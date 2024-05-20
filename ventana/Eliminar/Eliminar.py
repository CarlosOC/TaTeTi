from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from clases.Class_BDSqlite import BD_Slite
from clases.ClassPlayers import player

class Eliminar(QMainWindow):
    def __init__(self, BaseDeDatos_nombre):
        super().__init__()
        
        # Cargar la interfaz de usuario desde el archivo .ui
        uic.loadUi("ventana\Eliminar/Eliminar.ui", self)
        
        # Configurar el ícono de la ventana
        self.setWindowIcon(QIcon("imagenes/tateti.png"))

        # Abrir la hoja de estilos CSS
        with open("styles.css") as f:
            self.setStyleSheet(f.read())
        
        # Nombre de la base de datos
        self.BaseDeDatos_nombre = BaseDeDatos_nombre
        
        # Instancia de la clase BD_Slite para la base de datos
        self.BaseDeDatos = BD_Slite(BaseDeDatos_nombre)
        self.BaseDeDatos.db_connect()
        
        # Conectar los botones de Eliminar y Cancelar a sus funciones respectivas
        self.QPushButton_Eliminar.clicked.connect(self.eliminar_player)
        self.QPushButton_Cancelar.clicked.connect(self.close)

    # Función para establecer el ID del jugador a eliminar
    def id_eliminar(self, id_encontrado):
        self.id_encontrado = id_encontrado   

    # Función para eliminar el jugador de la base de datos
    def eliminar_player(self):
        self.BaseDeDatos.db_delete_PlayerData(self.id_encontrado)
        self.BaseDeDatos.db_delete_PlayerRecord(self.id_encontrado)
        self.close()