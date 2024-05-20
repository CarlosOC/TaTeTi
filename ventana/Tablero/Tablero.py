from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox  # Importa las clases QMainWindow, QApplication y QMessageBox desde PyQt5.QtWidgets.
from PyQt5.QtGui import QFont, QFontDatabase, QIcon  # Importa las clases QFont, QFontDatabase y QIcon desde PyQt5.QtGui.
from PyQt5 import uic, QtCore  # Importa el módulo uic y QtCore desde PyQt5.
from clases.Class_BDSqlite import BD_Slite  # Importa la clase BD_Slite desde el módulo clases.Class_BDSqlite.
from clases.ClassPlayers import player  # Importa la clase player desde el módulo clases.ClassPlayers.
from random import randrange  # Importa la función randrange desde el módulo random.

class VentanaTablero(QMainWindow):
    def __init__(self, BaseDeDatos_nombre, Player_Uno, Player_Dos, Tipo_Partida):
        super().__init__()
        self.Player_Uno = Player_Uno  # Inicializa el jugador uno.
        self.Player_Dos = Player_Dos  # Inicializa el jugador dos.
        self.Tipo_Partida = Tipo_Partida  # Inicializa el tipo de partida.
        self.BaseDeDatos_nombre = BaseDeDatos_nombre  # Inicializa el nombre de la base de datos.
        self.BaseDeDatos = BD_Slite(self.BaseDeDatos_nombre)  # Crea una instancia de BD_Slite.
        self.BaseDeDatos.db_connect()  # Conecta a la base de datos.

        uic.loadUi("ventana/Tablero/tablero.ui", self)  # Carga la interfaz de usuario desde un archivo .ui.
        self.setWindowIcon(QIcon("imagenes/tateti.png"))  # Establece el ícono de la ventana.

        # Aplica estilos desde un archivo CSS.
        with open("styles.css") as f:
            self.setStyleSheet(f.read())

        self.gameFinished = False  # Variable para verificar si el juego ha terminado.
        self.TurnoX = True  # Variable para determinar el turno.
        self.position = 0  # Inicializa la posición.
        self.board = [' '] * 9  # Inicializa el tablero con espacios vacíos.

        # Conecta los botones a sus respectivas funciones.
        self.pushButton_1.clicked.connect(self.btn1)
        self.pushButton_2.clicked.connect(self.btn2)
        self.pushButton_3.clicked.connect(self.btn3)
        self.pushButton_4.clicked.connect(self.btn4)
        self.pushButton_5.clicked.connect(self.btn5)
        self.pushButton_6.clicked.connect(self.btn6)
        self.pushButton_7.clicked.connect(self.btn7)
        self.pushButton_8.clicked.connect(self.btn8)
        self.pushButton_9.clicked.connect(self.btn9)

        # Establece los nombres de los jugadores en la interfaz.
        self.Qlabel_nick1.setText(self.Player_Uno.nick)
        self.Qlabel_nick2.setText(self.Player_Dos.nick)

        # Configuración del temporizador.
        self.timer = QtCore.QTimer()
        self.now = 0  # Inicializa el contador de tiempo.
        self.timer.start(1000)  # Configura el temporizador para que cuente cada segundo (1000 ms).
        self.timer.timeout.connect(self.tick_timer)  # Conecta la función tick_timer al temporizador.

    def tick_timer(self):
        # Actualiza el contador de tiempo y refresca el LCD.
        if not self.gameFinished:
            self.now += 1
            self.lcd_timer_update()

    def lcd_timer_update(self):
        # Actualiza el display del tiempo en el LCD.
        self.runtime = "%d:%02d" % (self.now / 60, self.now % 60)
        self.QLCDNumber_Tiempo.display(self.runtime)

    def btn1(self):
        # Acción del botón 1.
        self.position = 1
        self.botonPresionado(self.pushButton_1)
        self.game(self.position)

    def btn2(self):
        # Acción del botón 2.
        self.position = 2
        self.botonPresionado(self.pushButton_2)
        self.game(self.position)

    def btn3(self):
        # Acción del botón 3.
        self.position = 3
        self.botonPresionado(self.pushButton_3)
        self.game(self.position)

    def btn4(self):
        # Acción del botón 4.
        self.position = 4
        self.botonPresionado(self.pushButton_4)
        self.game(self.position)

    def btn5(self):
        # Acción del botón 5.
        self.position = 5
        self.botonPresionado(self.pushButton_5)
        self.game(self.position)

    def btn6(self):
        # Acción del botón 6.
        self.position = 6
        self.botonPresionado(self.pushButton_6)
        self.game(self.position)

    def btn7(self):
        # Acción del botón 7.
        self.position = 7
        self.botonPresionado(self.pushButton_7)
        self.game(self.position)

    def btn8(self):
        # Acción del botón 8.
        self.position = 8
        self.botonPresionado(self.pushButton_8)
        self.game(self.position)

    def btn9(self):
        # Acción del botón 9.
        self.position = 9
        self.botonPresionado(self.pushButton_9)
        self.game(self.position)

    def botonPresionado(self, boton):
        # Marca el botón con X u O según el turno y lo desactiva.
        if not self.gameFinished:
            if self.TurnoX:
                boton.setText("X")
            else:
                boton.setText("O")
            boton.setEnabled(False)

    def WindowResult(self, jugador):
        # Muestra una ventana emergente con el resultado del juego.
        msg = QMessageBox()
        with open("styles.css") as f:
            msg.setStyleSheet(f.read())
        font_name = "Kodchasan-SemiBold"
        QFontDatabase.addApplicationFont("fuentes/Kodchasan-SemiBold.ttf")
        fuente = QFont(font_name)
        msg.setFont(fuente)
        msg.setWindowTitle("Resultado")
        msg.setWindowIcon(QIcon("imagenes/tateti.png"))

        if jugador == "X":
            msg.setText("El ganador es: " + self.Player_Uno.nick)
        elif jugador == "O":
            msg.setText("El ganador es: " + self.Player_Dos.nick)
        else:
            msg.setText("Fue un empate")

        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def game(self, position):
        # Lógica principal del juego.
        if not self.gameFinished:
            if self.TurnoX:
                self.board[position - 1] = "X"
            else:
                self.board[position - 1] = "O"

            # Condiciones para ganar.
            if (self.board[0] == self.board[1] == self.board[2] and self.board[0] != ' ' or
                self.board[3] == self.board[4] == self.board[5] and self.board[3] != ' ' or
                self.board[6] == self.board[7] == self.board[8] and self.board[6] != ' ' or
                self.board[0] == self.board[3] == self.board[6] and self.board[0] != ' ' or
                self.board[1] == self.board[4] == self.board[7] and self.board[1] != ' ' or
                self.board[2] == self.board[5] == self.board[8] and self.board[2] != ' ' or
                self.board[0] == self.board[4] == self.board[8] and self.board[0] != ' ' or
                self.board[2] == self.board[4] == self.board[6] and self.board[2] != ' '):
                
                # Si se cumple una condición de ganar.
                if self.TurnoX:
                    self.finshgame(self.Player_Uno, self.Player_Dos)
                    self.WindowResult("X")
                else:
                    self.finshgame(self.Player_Dos, self.Player_Uno)
                    self.WindowResult("O")
                
                self.gameFinished = True

            # Si no hay espacios vacíos, es un empate.
            if not self.gameFinished and ' ' not in self.board:
                self.WindowResult("Empate")
                self.gameFinished = True
                self.empate(self.Player_Uno, self.Player_Dos)

            self.TurnoX = not self.TurnoX

            # Si no es el turno de X y el jugador dos es la PC, juega la PC.
            if not self.TurnoX and self.Player_Dos.nick == "PC":
                self.PC_Play()

    def empate(self, Player_Uno, Player_Dos):
        # Gestiona el resultado de un empate.
        if self.Tipo_Partida == "Campeonato":
            Resultado_JugadorUno = "E"
            Resultado_JugadorDos = "E"
            self.Player_Uno.PE += 1
            self.Player_Dos.PE += 1
            self.BaseDeDatos.NewGame(0, self.Player_Uno.id, self.Player_Dos.id, Resultado_JugadorUno, Resultado_JugadorDos)
            self.Player_Uno.Puntos()
            self.Player_Dos.Puntos()
            self.BaseDeDatos.NewGameResult(self.Player_Uno.id, self.Player_Uno.PG, self.Player_Uno.PP, self.Player_Uno.PE, self.Player_Uno.puntos, self.Player_Dos.id, self.Player_Dos.PG, self.Player_Dos.PP, self.Player_Dos.PE, self.Player_Dos.puntos)

    def finshgame(self, Player_Ganador, Player_Perdedor):
        # Gestiona el resultado de una partida finalizada.
        if self.Tipo_Partida == "PartidaRapida":
            print("GANADOR: ", Player_Ganador.nick)
            print("PERDEDOR: ", Player_Perdedor.nick)

        elif self.Tipo_Partida == "Campeonato":
            if self.Player_Uno.nick == Player_Ganador.nick:
                Resultado_JugadorUno = "V"
                self.Player_Uno.PG += 1
            elif self.Player_Uno.nick == Player_Perdedor.nick:
                Resultado_JugadorUno = "P"
                self.Player_Uno.PP += 1

            if self.Player_Dos.nick == Player_Ganador.nick:
                Resultado_JugadorDos = "V"
                self.Player_Dos.PG += 1
            elif self.Player_Dos.nick == Player_Perdedor.nick:
                Resultado_JugadorDos = "P"
                self.Player_Dos.PP += 1

            self.BaseDeDatos.NewGame(0, self.Player_Uno.id, self.Player_Dos.id, Resultado_JugadorUno, Resultado_JugadorDos)
            self.Player_Uno.Puntos()
            self.Player_Dos.Puntos()
            self.BaseDeDatos.NewGameResult(self.Player_Uno.id, self.Player_Uno.PG, self.Player_Uno.PP, self.Player_Uno.PE, self.Player_Uno.puntos, self.Player_Dos.id, self.Player_Dos.PG, self.Player_Dos.PP, self.Player_Dos.PE, self.Player_Dos.puntos)

    def PC_Play(self):
        # Lógica para que juegue la PC.
        casillero = 5
        while not self.gameFinished and (self.board[casillero - 1] == "X" or self.board[casillero - 1] == "O"):
            casillero = randrange(1, 9)
        
        if casillero == 1:
            self.btn1()
        elif casillero == 2:
            self.btn2()
        elif casillero == 3:
            self.btn3()
        elif casillero == 4:
            self.btn4()
        elif casillero == 5:
            self.btn5()
        elif casillero == 6:
            self.btn6()
        elif casillero == 7:
            self.btn7()
        elif casillero == 8:
            self.btn8()
        elif casillero == 9:
            self.btn9()