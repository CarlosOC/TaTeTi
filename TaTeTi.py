# Importa las clases QMainWindow y QApplication del módulo PyQt5.QtWidgets.
from PyQt5.QtWidgets import QMainWindow, QApplication  
# Importa la clase Main del módulo ventana.Main.Main.
from ventana.Main.Main import Main  
# Importa la clase BD_Slite del módulo clases.Class_BDSqlite.
from clases.Class_BDSqlite import BD_Slite  

# Creación de la Base de Datos
BaseDeDatos_nombre = "data.sql"  # Nombre del archivo de la base de datos SQLite.
BaseDeDatos = BD_Slite(BaseDeDatos_nombre)  # Crea una instancia de BD_Slite con el nombre de la base de datos.
BaseDeDatos.db_connect()  # Conecta a la base de datos.
BaseDeDatos.db_create()  # Crea las tablas necesarias en la base de datos si no existen.

# Creación de la aplicación Qt
app = QApplication([])  # Crea una instancia de la aplicación Qt.

# Creación y visualización de la ventana principal
win = Main(BaseDeDatos_nombre)  # Crea una instancia de la clase Main, pasando el nombre de la base de datos.
win.show()  # Muestra la ventana principal.
app.exec_()  # Inicia el bucle de eventos de la aplicación Qt.