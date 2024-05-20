from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtGui import QFont, QFontDatabase, QIcon
from PyQt5 import uic
from clases.Class_BDSqlite import BD_Slite
from clases.ClassPlayers import player
from ventana.Eliminar.Eliminar import Eliminar
from ventana.Registro_de_usuario.registro import VentanaRegistro

class formulario(QMainWindow):
    def __init__(self, BaseDeDatos_nombre):
        super().__init__()
        
        # Nombre de la base de datos
        self.BaseDeDatos_nombre = BaseDeDatos_nombre
        
        # Instancia de la clase BD_Slite para la base de datos
        self.BaseDeDatos = BD_Slite(BaseDeDatos_nombre)
        self.BaseDeDatos.db_connect()
        
        # Cargar la interfaz de usuario desde el archivo .ui
        uic.loadUi("ventana\Loggin/loggin.ui", self)
        
        # Configurar el ícono de la ventana
        self.setWindowIcon(QIcon("imagenes/tateti.png"))

        # Abrir la hoja de estilos CSS
        with open("styles.css") as f:
            self.setStyleSheet(f.read())
        
        # Conectar los botones de Aceptar y Cancelar a sus funciones respectivas
        self.pushButton_Aceptar.clicked.connect(self.validar_pass)
        self.pushButton_Cancelar.clicked.connect(self.cerrar)
        
        # Inicializar las ventanas de Eliminar y Registro
        self.ventana_eliminar = Eliminar(self.BaseDeDatos_nombre)
        self.ventana_registro = VentanaRegistro(self.BaseDeDatos_nombre)
        
    # Función para limpiar los campos de entrada
    def limpiar_pantalla(self):
        self.lineEdit_Nick.clear()
        self.lineEdit_Password.clear()

    # Función para validar el nick y la contraseña ingresados
    def validar_pass(self):
        nick = self.lineEdit_Nick.text()
        contrasenia = self.lineEdit_Password.text()
        Validado = False   

        Lista_Jugadores = []
        
        # Obtener todos los jugadores de la base de datos
        Jugadores = self.BaseDeDatos.AllPlayersData()
        
        # Agregar los jugadores a la lista
        for jugador in Jugadores:
            Lista_Jugadores.append(player(jugador[0], jugador[1], jugador[2], jugador[3], jugador[4], jugador[5], jugador[6], jugador[7], jugador[8], jugador[9]))

        # Validar las credenciales ingresadas
        Validado = False
        for item in Lista_Jugadores:
            if nick == item.nick and contrasenia == item.password:
                Validado = True 
                self.id_encontrado = item.id    

        if Validado == True:
            # Acciones dependiendo del origen (Eliminar o Modificar)
            if self.origen == "Eliminar":
                self.ventana_eliminar.id_eliminar(self.id_encontrado)
                self.ventana_eliminar.show()
                self.limpiar_pantalla()
                self.close()
            elif self.origen == "Modificar":
                self.ventana_registro.ID(self.id_encontrado)
                self.ventana_registro.modificar_crear("Modificar") 
                self.ventana_registro.abrir_ventana()
                self.limpiar_pantalla()
                self.close()

        elif Validado == False:
            # Mostrar un mensaje de error si las credenciales son incorrectas
            msg = QMessageBox()
            with open("styles.css") as f:
                msg.setStyleSheet(f.read())
            font_name = "Kodchasan-SemiBold"
            QFontDatabase.addApplicationFont("fuentes/Kodchasan-SemiBold.ttf")
            fuente = QFont(font_name)
            msg.setFont(fuente)             
            msg.setWindowTitle("Error")
            msg.setWindowIcon(QIcon("imagenes/tateti.png"))
            Texto = "Nick o Contraseña incorrectos"
            msg.setText(Texto)
            msg.setIcon(QMessageBox.NoIcon)
            msg.exec_()
    
    # Función para definir el origen (Eliminar o Modificar)
    def entrada(self, origen):
        self.origen = origen 

    # Función para cerrar la ventana y limpiar los campos de entrada
    def cerrar(self):
        self.limpiar_pantalla()
        self.close()
