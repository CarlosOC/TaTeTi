from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox  # Importa las clases necesarias desde PyQt5.QtWidgets.
from PyQt5.QtGui import QFont, QFontDatabase, QIcon  # Importa las clases necesarias desde PyQt5.QtGui.
from PyQt5 import uic  # Importa el módulo uic desde PyQt5 para cargar archivos .ui.
from clases.Class_BDSqlite import BD_Slite  # Importa la clase BD_Slite desde el módulo clases.Class_BDSqlite.

class VentanaRegistro(QMainWindow):
    def __init__(self, BaseDeDatos_nombre):
        super().__init__()
        # Inicializa la variable con el nombre del archivo de base de datos.
        self.BaseDeDatos_nombre = BaseDeDatos_nombre
        # Crea una instancia de BD_Slite con el nombre de la base de datos.
        self.BaseDeDatos = BD_Slite(self.BaseDeDatos_nombre)
        # Conecta a la base de datos.
        self.BaseDeDatos.db_connect()
        # Inicializa variables de estado.
        self.origen = "Crear"
        self.id_encontrado = -1
    
        # Carga la interfaz de usuario desde un archivo .ui.
        uic.loadUi("ventana/Registro_de_usuario/RegistroDeUsuario.ui", self)
        # Establece el ícono de la ventana.
        self.setWindowIcon(QIcon("imagenes/tateti.png"))

        # Aplica estilos desde un archivo CSS.
        with open("styles.css") as f:
            self.setStyleSheet(f.read())
      
        # Conecta los botones a las funciones correspondientes.
        self.aceptar_QpushButton.clicked.connect(self.enviar_datos)
        self.cancelar_QpushButton.clicked.connect(self.close)
    
    def abrir_ventana(self):
        # Limpia los campos de entrada.
        self.nick_QlineEdit.clear()
        self.email_QlineEdit.clear()
        self.password_QlineEdit.clear()
        self.QspinBox_edad.setValue(0)

        # Si la ventana se abre para modificar, muestra los datos existentes.
        if self.origen == "Modificar":
            self.mostrar_datos()
        self.show()   

    def enviar_datos(self):
        # Obtiene los datos ingresados.
        nick = self.nick_QlineEdit.text()
        correo = self.email_QlineEdit.text()
        contraseña = self.password_QlineEdit.text()
        edad = self.QspinBox_edad.value()
        sex_female = self.radioButton_femenino.isChecked()
        sex_male = self.radioButton_masculino.isChecked()

        # Verifica que todos los campos estén completos.
        if nick != "" and contraseña != "" and correo != "" and edad != 0:
            if self.origen != "Modificar":
                # Determina el sexo seleccionado.
                if sex_female:
                    sexo = 'F'
                elif sex_male:
                    sexo = 'M'
                # Crea un nuevo jugador en la base de datos.
                self.BaseDeDatos.NewPlayer(correo, contraseña, nick, edad, sexo)
                # Limpia los campos después de enviar los datos.
                self.nick_QlineEdit.setText('')
                self.email_QlineEdit.setText('')
                self.password_QlineEdit.setText('')
                self.QspinBox_edad.setValue(0)
                self.close()
            else:
                # Modifica los datos existentes.
                self.modificar_datos()
                self.close()
        else:
            # Muestra un mensaje de error si faltan datos.
            msg = QMessageBox()
            with open("styles.css") as f:
                msg.setStyleSheet(f.read())
            font_name = "Kodchasan-SemiBold"
            QFontDatabase.addApplicationFont("fuentes/Kodchasan-SemiBold.ttf")
            fuente = QFont(font_name)
            msg.setFont(fuente)
            msg.setWindowTitle("Error")
            msg.setWindowIcon(QIcon("imagenes/tateti.png"))
            msg.setText("Faltan Cargar Datos")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
    
    def mostrar_datos(self):
        # Obtiene los datos del jugador desde la base de datos.
        player = self.BaseDeDatos.Serch_PlayerData(self.id_encontrado)
       
        # Muestra los datos del jugador en los campos correspondientes.
        self.nick_QlineEdit.setText(player[0][1])
        self.email_QlineEdit.setText(player[0][4])
        self.password_QlineEdit.setText(player[0][5])
        self.QspinBox_edad.setValue(int(player[0][2]))
        if player[0][3] == 'M':
            self.radioButton_masculino.setChecked(True)
        else:
            self.radioButton_femenino.setChecked(True)

    def modificar_datos(self):
        # Obtiene los datos ingresados.
        nick = self.nick_QlineEdit.text()
        correo = self.email_QlineEdit.text()
        contraseña = self.password_QlineEdit.text()
        edad = self.QspinBox_edad.value()
        sex_female = self.radioButton_femenino.isChecked()
        if sex_female:
            sexo = 'F'
        sex_male = self.radioButton_masculino.isChecked()
        if sex_male:
            sexo = 'M'
                                
        # Actualiza los datos del jugador en la base de datos.
        self.BaseDeDatos.db_update_PlayerData(self.id_encontrado, correo, contraseña, nick, edad, sexo)

        # Limpia los campos después de modificar los datos.
        self.nick_QlineEdit.setText('')
        self.email_QlineEdit.setText('')
        self.password_QlineEdit.setText('')
        self.QspinBox_edad.setValue(0)

        self.close()

    def modificar_crear(self, origen):
        # Establece el origen de la acción (Crear o Modificar).
        self.origen = origen

    def ID(self, id_encontrado):
        # Establece el ID del jugador a modificar.
        self.id_encontrado = id_encontrado
