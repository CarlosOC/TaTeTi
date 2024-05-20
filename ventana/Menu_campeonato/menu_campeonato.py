from PyQt5.QtWidgets import QMainWindow, QApplication, QHeaderView, QTableWidgetItem, QMessageBox
from PyQt5.QtGui import QFont, QFontDatabase, QIcon
from PyQt5 import uic
from ventana.Tablero.Tablero import VentanaTablero
from clases.Class_BDSqlite import BD_Slite
from clases.ClassPlayers import player
from ventana.Registro_de_usuario.registro import VentanaRegistro

class Menu_campeonato(QMainWindow):
    def __init__(self, BaseDeDatos_nombre):
        super().__init__()
        uic.loadUi("ventana/Menu_campeonato/menu_campeonato.ui", self)
        self.setWindowIcon(QIcon("imagenes/tateti.png"))

        # Abrir la hoja de estilos en CSS
        with open("styles.css") as self.f:
            self.setStyleSheet(self.f.read())
        
        self.BaseDeDatos_nombre = BaseDeDatos_nombre
        self.boton_crear_jugar = False
        self.partida = 0
        
        # Inicializar la base de datos
        self.BaseDeDatos = BD_Slite(self.BaseDeDatos_nombre)
        self.BaseDeDatos.db_connect()
        
        # Inicializar la ventana de registro
        self.Window_Registro = VentanaRegistro(self.BaseDeDatos_nombre)

        # Conectar los botones a sus funciones correspondientes
        self.QPushButton_AgregarJugador.clicked.connect(self.AgregarJugador)
        self.QPushButton_QuitarJugador.clicked.connect(self.QuitarJugador)
        self.QPushButton_Cancelar.clicked.connect(self.Cancelar)
        self.QpushButton_CrearCampeonato_Jugar.clicked.connect(self.CrearCampeonato_JugarPartida)
        self.QSpinBox_CantidadJugadores.valueChanged.connect(self.CantidadJugadoresChange)
        
        # Cargar la lista de jugadores y crear la tabla
        self.CargaListaPlayers()
        self.CreateTable()

    def Cancelar(self):
        self.close()

    def CantidadJugadoresChange(self):
        # Si se cambia el valor del número de jugadores, se reinicia todo
        self.CreateTable()
        while self.QListWidget_Seleccionados.count() > 0:
            self.QListWidget_Seleccionados.takeItem(self.QListWidget_Seleccionados.count() - 1)
        self.boton_crear_jugar = False
        self.QpushButton_CrearCampeonato_Jugar.setText("Crear Campeonato")

    def CrearCampeonato_JugarPartida(self):
        # Verifica si se ha presionado el botón "Crear Campeonato" antes
        if self.boton_crear_jugar == False:
            if self.QListWidget_Seleccionados.count() == 0 or self.QListWidget_Seleccionados.count() < 2:
                self.VentanaEmergente("Error", "Número de jugadores seleccionados incorrecto")
            elif self.QListWidget_Seleccionados.count() >= 2:
                self.QpushButton_CrearCampeonato_Jugar.setText("Jugar")
                self.TablaPartidas()
                self.boton_crear_jugar = True
        else:
            self.Jugar()

    def CargaListaPlayers(self):
        self.QListWidget_Players.clear()
        self.Lista_Jugadores = []
        self.Jugadores = self.BaseDeDatos.AllPlayersData()
        for jugador in self.Jugadores:
            self.Lista_Jugadores.append(player(jugador[0], jugador[1], jugador[2], jugador[3], jugador[4], jugador[5], jugador[6], jugador[7], jugador[8], jugador[9]))
        for item in self.Lista_Jugadores:
            self.QListWidget_Players.addItem(item.nick)

    def AgregarJugador(self):
        JugadorCargado = False
        indice = self.QListWidget_Players.currentRow()
        for i in range(self.QListWidget_Seleccionados.count()):
            if self.QListWidget_Players.item(indice).text() == self.QListWidget_Seleccionados.item(i).text():
                JugadorCargado = True
        if not JugadorCargado:
            if self.QSpinBox_CantidadJugadores.value() - 1 >= self.QListWidget_Seleccionados.count():
                self.QListWidget_Seleccionados.addItem(self.Lista_Jugadores[indice].nick)
        else:
            self.VentanaEmergente("Error", "El jugador ya se encuentra cargado")

    def QuitarJugador(self):
        indice = self.QListWidget_Seleccionados.currentRow()
        self.QListWidget_Seleccionados.takeItem(indice)

    def CreateTable(self):
        self.QTableWidget_Partidas.clear()
        while self.QTableWidget_Partidas.rowCount() > 0:
            self.QTableWidget_Partidas.removeRow(self.QTableWidget_Partidas.rowCount() - 1)
        self.Columnas = ("Partida;Jugador Uno;;Jugador Dos").split(";")
        self.QTableWidget_Partidas.setColumnCount(len(self.Columnas))
        self.QTableWidget_Partidas.setHorizontalHeaderLabels(self.Columnas)
        for i in range(len(self.Columnas)):
            self.QTableWidget_Partidas.horizontalHeader().setSectionResizeMode(i, QHeaderView.Stretch)

    def Jugar(self):
        for JUGADOR in self.Lista_Jugadores:
            if JUGADOR.nick == self.QTableWidget_Partidas.item(self.partida, 1).text():
                Player_Uno = JUGADOR
            if JUGADOR.nick == self.QTableWidget_Partidas.item(self.partida, 3).text():
                Player_Dos = JUGADOR
        self.window_tablero = VentanaTablero(self.BaseDeDatos_nombre, Player_Uno, Player_Dos, "Campeonato")
        self.window_tablero.show()
        self.partida += 1
        if self.partida == self.QTableWidget_Partidas.rowCount():
            self.partida = 0
            self.CreateTable()
            self.QpushButton_CrearCampeonato_Jugar.setText("Crear Campeonato")
            self.boton_crear_jugar = False

    def TablaPartidas(self):
        numero_de_jugador = self.QListWidget_Seleccionados.count()
        fila = 0
        for i in range(numero_de_jugador):
            for j in range(self.QListWidget_Seleccionados.count()):
                if i != j:
                    self.QTableWidget_Partidas.insertRow(fila)
                    self.QTableWidget_Partidas.setItem(fila, 0, QTableWidgetItem(str(fila + 1)))
                    self.QTableWidget_Partidas.setItem(fila, 1, QTableWidgetItem(self.QListWidget_Seleccionados.item(i).text()))
                    self.QTableWidget_Partidas.setItem(fila, 2, QTableWidgetItem("vs"))
                    self.QTableWidget_Partidas.setItem(fila, 3, QTableWidgetItem(self.QListWidget_Seleccionados.item(j).text()))
                    fila += 1

    def VentanaEmergente(self, Titulo, Texto):
        msg = QMessageBox()
        with open("styles.css") as f:
            msg.setStyleSheet(f.read())
        font_name = "Kodchasan-SemiBold"
        QFontDatabase.addApplicationFont("fuentes/Kodchasan-SemiBold.ttf")
        fuente = QFont(font_name)
        msg.setWindowIcon(QIcon("imagenes/tateti.png"))
        msg.setFont(fuente)
        msg.setWindowTitle(Titulo)
        msg.setWindowIcon(QIcon("imagenes/tateti.png"))
        msg.setText(Texto)
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def AbrirVentana(self):
        self.QListWidget_Seleccionados.clear()
        self.CreateTable()
        self.boton_crear_jugar = False
        self.CargaListaPlayers()
        self.show()
