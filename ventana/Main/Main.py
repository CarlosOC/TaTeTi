from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QSplashScreen
from PyQt5.QtGui import QFont, QFontDatabase, QIcon, QPixmap
from PyQt5 import uic
from PyQt5.QtCore import QTimer
from ventana.Menu_partidarapida.menu_partidarapida import PartidaRapida
from ventana.Menu_campeonato.menu_campeonato import Menu_campeonato
from ventana.Tabla_puntaje.tabla_puntaje import TablaPuntaje
from ventana.Registro_de_usuario.registro import VentanaRegistro
from ventana.Loggin.loggin import formulario

class Main(QMainWindow):
    def __init__(self, BaseDeDatos_nombre):
        super().__init__()
        
        # Configuración de la pantalla de bienvenida (splash screen)
        self.splash = QSplashScreen(QPixmap("imagenes/splash.png"))
        self.splash.show()
        QTimer.singleShot(5, self.splash.close)  # Cierra la pantalla de bienvenida después de un breve tiempo
        
        # Configuración de la fuente externa
        font_name = "Kodchasan-SemiBold"
        QFontDatabase.addApplicationFont("fuentes/Kodchasan-SemiBold.ttf")
        fuente = QFont(font_name)
        self.setFont(fuente)
 
        self.BaseDeDatos_nombre = BaseDeDatos_nombre
        
        # Cargar la interfaz de usuario y configurar el ícono de la ventana
        uic.loadUi("ventana/Main/main.ui", self)
        self.setWindowIcon(QIcon("imagenes/tateti.png"))

        # Abrir la hoja de estilos en CSS
        with open("styles.css") as f:
            self.setStyleSheet(f.read())

        # Inicializar las ventanas de la aplicación
        self.Window_PartidaRapida = PartidaRapida(self.BaseDeDatos_nombre)
        self.Window_Menu_campeonato = Menu_campeonato(self.BaseDeDatos_nombre)
        self.Window_TablaPuntaje = TablaPuntaje(self.BaseDeDatos_nombre)
        self.Window_TablaPuntaje = TablaPuntaje(self.BaseDeDatos_nombre)  # Se inicializa dos veces
        self.Window_Registro = VentanaRegistro(self.BaseDeDatos_nombre)
        self.Window_Formulario = formulario(self.BaseDeDatos_nombre)
    
        # Conectar acciones de menú y botones a funciones
        self.actionCrear_Perfil.triggered.connect(self.OpenWindow_perfiles)
        self.actionModificar_Perfil.triggered.connect(self.OpenWindow_loggin_modificar)
        self.actionEliminar.triggered.connect(self.OpenWindow_loggin_eliminar)
        self.QPushButton_PartidaRapida.clicked.connect(self.OpenWindow_partidarapida)
        self.QPushButton_Campeonato.clicked.connect(self.OpenWindow_menucampeonato)
        self.actionVer_Tabla.triggered.connect(self.OpenWindow_tabladepuntaje)
        self.actionAbout_US.triggered.connect(self.OpenWindow_About_US)

    # Funciones para abrir diferentes ventanas
    def OpenWindow_partidarapida(self):
        self.Window_PartidaRapida.show()

    def OpenWindow_perfiles(self):
        self.Window_Registro.abrir_ventana()

    def OpenWindow_loggin_modificar(self):
        self.Window_Formulario.entrada("Modificar")
        self.Window_Formulario.show()
       
    def OpenWindow_loggin_eliminar(self):
        self.Window_Formulario.entrada("Eliminar")
        self.Window_Formulario.show()

    def OpenWindow_menucampeonato(self):
        self.Window_Menu_campeonato.AbrirVentana()      

    def OpenWindow_tabladepuntaje(self):
        self.Window_TablaPuntaje.InsertTablaData()
        self.Window_TablaPuntaje.show() 
 
    def OpenWindow_About_US (self):
        # Mostrar información sobre el programa y sus creadores en una ventana emergente
        msg = QMessageBox()
        with open("styles.css") as f:
            msg.setStyleSheet(f.read())
        font_name = "Kodchasan-SemiBold"
        QFontDatabase.addApplicationFont("fuentes/Kodchasan-SemiBold.ttf")
        
        fuente = QFont(font_name)
        msg.setFont(fuente)             
        msg.setWindowTitle("About US")
        msg.setWindowIcon(QIcon("imagenes/tateti.png"))
        Texto = "Tateti 2020 Version Alpha 1.0\nTrabajo Practico TUP 2020\nProgramador:\n\t\t* Oviedo Codigoni, Carlos Nicolas\n "
        msg.setText(Texto)
        msg.setIcon(QMessageBox.NoIcon)
        msg.exec_()