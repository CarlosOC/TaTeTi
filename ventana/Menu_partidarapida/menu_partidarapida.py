from PyQt5.QtWidgets import QMainWindow, QApplication  # Importa las clases necesarias desde PyQt5.QtWidgets.
from PyQt5 import uic  # Importa el módulo uic desde PyQt5 para cargar archivos .ui.
from PyQt5.QtGui import QIcon  # Importa la clase QIcon desde PyQt5.QtGui.
from ventana.Players.players import ventanaPlayer  # Importa la clase ventanaPlayer desde el módulo correspondiente.

class PartidaRapida(QMainWindow):
    def __init__(self, BaseDeDatos_nombre):
        super().__init__()
        self.BaseDeDatos_nombre = BaseDeDatos_nombre
        
        # Carga la interfaz de usuario desde un archivo .ui.
        uic.loadUi("ventana/Menu_partidarapida/menu_partidarapida.ui", self)
        # Establece el ícono de la ventana.
        self.setWindowIcon(QIcon("imagenes/tateti.png"))

        # Aplica estilos desde un archivo CSS.
        with open("styles.css") as f:
            self.setStyleSheet(f.read())
        
        # Crea una instancia de la ventana de selección de jugadores.
        self.window_players = ventanaPlayer(self.BaseDeDatos_nombre)
        
        # Conecta los botones a las funciones correspondientes.
        self.QPushButton_dosjugadores.clicked.connect(self.open_window_DosJugadores)
        self.QPushButton_vsPC.clicked.connect(self.open_window_vsPC)
    
    def open_window_DosJugadores(self):
        # Configura el tipo de juego como Humano vs Humano y abre la ventana de selección de jugadores.
        self.window_players.tipo_juego("HumanoVsHumano")
        self.window_players.show()
        self.close()

    def open_window_vsPC(self):
        # Configura el tipo de juego como Humano vs PC y abre la ventana de selección de jugadores.
        self.window_players.tipo_juego("HumanoVsPC")
        self.window_players.show()
        self.close()
