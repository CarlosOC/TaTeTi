from PyQt5.QtWidgets            import QMainWindow, QApplication, QMessageBox
from PyQt5                      import uic
from PyQt5.QtGui                import QFont,QFontDatabase, QIcon
from ventana.Tablero.Tablero    import VentanaTablero
from clases.Class_BDSqlite      import BD_Slite
from clases.ClassPlayers        import player


class ventanaPlayer(QMainWindow):
    def __init__(self,BaseDeDatos_nombre):
        super().__init__()
        self.BaseDeDatos_nombre = BaseDeDatos_nombre
        
        
        uic.loadUi("ventana/Players/players.ui",self)
        self.setWindowIcon(QIcon("imagenes/tateti.png"))

        with open("styles.css") as f:
            self.setStyleSheet(f.read())        
        self.QpushButton_jugar.clicked.connect (self.open_window_tablero)
    
    def tipo_juego (self,Tipo_Juego):
        self.Tipo_Juego = Tipo_Juego
        if self.Tipo_Juego == "HumanoVsPC":
            # Deshabilito el Nick del Player 2 y Cargo el Texto PC
            self.QlineEdit_player_2_nick.setEnabled(False)
            self.QlineEdit_player_1_nick.clear()
            self.QlineEdit_player_2_nick.setText("PC")
        if self.Tipo_Juego == "HumanoVsHumano":
            self.QlineEdit_player_2_nick.setEnabled(True)
            self.QlineEdit_player_1_nick.clear()   
            self.QlineEdit_player_2_nick.clear()           

    def open_window_tablero(self):
        player_1_nick = self.QlineEdit_player_1_nick.text()
        player_2_nick = self.QlineEdit_player_2_nick.text()
        if player_1_nick==player_2_nick: 
            self.VentanaEmergente ("Error: ","El Player dos y Player Uno no puede tener el mismo nick")
        elif player_1_nick == "" or  player_2_nick =="":
            self.VentanaEmergente ("Error: ","Jugador sin Nick")

        else:
            if self.Tipo_Juego == "HumanoVsPC":
                Player_Uno = player(0,self.QlineEdit_player_1_nick.text(),0,"M","none","none",0,0,0,0)
                Player_Dos = player(0,"PC",0,"M","none","none",0,0,0,0)
                self.window_tablero = VentanaTablero(self.BaseDeDatos_nombre,Player_Uno, Player_Dos,"PartidaRapida" )
                self.window_tablero.show()

            if self.Tipo_Juego == "HumanoVsHumano":
                if player_2_nick == "PC" or player_2_nick == "pc":
                    self.VentanaEmergente ("Error: ","El Player dos no puede tener el nick PC")
                else:
                    Player_Uno = player(0,self.QlineEdit_player_1_nick.text(),0,"M","none","none",0,0,0,0)
                    Player_Dos = player(0,self.QlineEdit_player_2_nick.text(),0,"M","none","none",0,0,0,0)
                    self.window_tablero = VentanaTablero(self.BaseDeDatos_nombre,Player_Uno, Player_Dos,"PartidaRapida" )
                    self.window_tablero.show()
                    self.close()

    def VentanaEmergente (self,Titulo,Texto):
        msg = QMessageBox()
        with open("styles.css") as f:
            msg.setStyleSheet(f.read())
        font_name="Kodchasan-SemiBold"
        QFontDatabase.addApplicationFont("fuentes/Kodchasan-SemiBold.ttf")
        fuente = QFont(font_name)
        msg.setFont(fuente)  
        #Titulo
        msg.setWindowTitle(Titulo)
        #Icono
        msg.setWindowIcon(QIcon("imagenes/tateti.png"))
        #Cuerpo
        msg.setText(Texto)   
        #Icono
        msg.setIcon(QMessageBox.Warning)
        #Botones
        msg.setStandardButtons(QMessageBox.Ok )
        msg.exec_()
