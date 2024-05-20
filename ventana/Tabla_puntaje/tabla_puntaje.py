from PyQt5.QtWidgets import QMainWindow, QApplication, QHeaderView, QTableWidgetItem  # Importa las clases necesarias desde PyQt5.QtWidgets.
from PyQt5 import uic  # Importa el módulo uic desde PyQt5 para cargar archivos .ui.
from PyQt5.QtGui import QIcon  # Importa la clase QIcon desde PyQt5.QtGui.
from clases.Class_BDSqlite import BD_Slite  # Importa la clase BD_Slite desde el módulo clases.Class_BDSqlite.
from clases.ClassPlayers import player  # Importa la clase player desde el módulo clases.ClassPlayers.

class TablaPuntaje(QMainWindow):
    def __init__(self, BaseDeDatos_nombre):
        super().__init__()
        self.BaseDeDatos_nombre = BaseDeDatos_nombre  # Inicializa el nombre de la base de datos.
        self.BaseDeDatos = BD_Slite(self.BaseDeDatos_nombre)  # Crea una instancia de BD_Slite.
        self.BaseDeDatos.db_connect()  # Conecta a la base de datos.
        uic.loadUi("ventana\Tabla_puntaje/tabla_puntaje.ui", self)  # Carga la interfaz de usuario desde un archivo .ui.
        self.setWindowIcon(QIcon("imagenes/tateti.png"))  # Establece el ícono de la ventana.

        # Abre y aplica el archivo de estilo CSS.
        with open("styles.css") as f:
            self.setStyleSheet(f.read())

        # Conecta el botón de cerrar a la función CloseWindow.
        self.QPushButton_Cerrar.clicked.connect(self.CloseWindow)

        # Crea la tabla y llena sus datos.
        self.CreateTable()
        self.InsertTablaData()

    def CreateTable(self):
        # Define las columnas de la tabla.
        self.Columnas = ("Nick;N° de Partidas;Partidas Ganadas;Partidas Empatadas;Partidas Perdidas; Puntaje Acumulado").split(";")
        self.QTableWidget_Tabla.setColumnCount(len(self.Columnas))  # Establece el número de columnas.
        self.QTableWidget_Tabla.setHorizontalHeaderLabels(self.Columnas)  # Establece los encabezados de las columnas.

        # Distribuye uniformemente el tamaño de las columnas.
        for i in range(len(self.Columnas)):
            self.QTableWidget_Tabla.horizontalHeader().setSectionResizeMode(i, QHeaderView.Stretch)

    def CloseWindow(self):
        self.close()  # Cierra la ventana.

    def InsertTablaData(self):
        Lista_Jugadores = []  # Lista para almacenar los jugadores.

        # Trae todos los datos de los jugadores desde la base de datos.
        Jugadores = self.BaseDeDatos.AllPlayersData()

        # Agrega cada jugador a la lista de jugadores.
        for jugador in Jugadores:
            Lista_Jugadores.append(player(jugador[0], jugador[1], jugador[2], jugador[3], jugador[4], jugador[5], jugador[6], jugador[7], jugador[8], jugador[9]))

        # Ordena la lista de jugadores según sus puntos en orden descendente.
        Lista_Jugadores.sort(reverse=True)

        # Limpia la tabla antes de llenarla.
        self.QTableWidget_Tabla.setRowCount(0)

        # Llena la tabla con los datos de los jugadores.
        for fila in range(len(Lista_Jugadores)):
            self.QTableWidget_Tabla.insertRow(fila)  # Crea una nueva fila.
            # Inserta los datos del jugador en las celdas correspondientes.
            self.QTableWidget_Tabla.setItem(fila, 0, QTableWidgetItem(Lista_Jugadores[fila].nick))
            self.QTableWidget_Tabla.setItem(fila, 1, QTableWidgetItem(str(Lista_Jugadores[fila].Paridos_Jugados())))
            self.QTableWidget_Tabla.setItem(fila, 2, QTableWidgetItem(str(Lista_Jugadores[fila].PG)))
            self.QTableWidget_Tabla.setItem(fila, 3, QTableWidgetItem(str(Lista_Jugadores[fila].PE)))
            self.QTableWidget_Tabla.setItem(fila, 4, QTableWidgetItem(str(Lista_Jugadores[fila].PP)))
            self.QTableWidget_Tabla.setItem(fila, 5, QTableWidgetItem(str(Lista_Jugadores[fila].puntos)))
