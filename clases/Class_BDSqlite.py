import sqlite3

class BD_Slite ():
    def __init__            (self,nombre_archivo):
        if isinstance (nombre_archivo,str):
            self.file = nombre_archivo
        else:
           print ( "Error nombre_archivo: ",nombre_archivo,"invalid type") 

# Conecta el Archivo o lo crea.
    def db_connect          (self):
       self.db = sqlite3.connect(self.file) # Creamos la base de datos
       self.cursor = self.db.cursor()

# Desconectar el Archivo.   
    def db_disconnect       (self):
        self.db.close()

# Creamos Todas las Tablas de la Base de Dato   
    def db_create                   (self):
        # Creamos la Tabla PlayerData y sus Columnas
        self.cursor.execute ("CREATE TABLE IF NOT EXISTS PlayerData " 
                             "(ID_Player INTEGER PRIMARY KEY AUTOINCREMENT, "
                             "Correo varchar(20), Contraseña varchar(20)," 
                             "Nick varchar(20), Edad int,"
                             "Sexo varchar(20));")
        self.db.commit()
        
        # Creamos la Tabla Player_Game y sus Columnas        
        self.cursor.execute ("CREATE TABLE IF NOT EXISTS Player_Game " 
                             "(ID_player_game INTEGER PRIMARY KEY AUTOINCREMENT, "
                             "ID_Player int, ID_Game int," 
                             "Resultado varchar(20));")
        self.db.commit()
        
        # Creamos la Tabla Game y sus Columnas 
        self.cursor.execute ("CREATE TABLE IF NOT EXISTS Game " 
                             "(ID_Game INTEGER PRIMARY KEY AUTOINCREMENT, "
                             "Duracion int);")
        self.db.commit()        
        
        # Creamos la Tabla PlayerRecord y sus Columnas 
        self.cursor.execute ("CREATE TABLE IF NOT EXISTS PlayerRecord " 
                             "(ID_Player INTEGER PRIMARY KEY, "
                             "Partidas_Ganadas int, Partidas_Perdidas int,"
                             "Partidas_Empatadas int, Puntaje_Acumulado int);")
        self.db.commit() 

# Insertar Datos en Cada Tabla    
    def db_insert_PlayerData        (self,correo,contraseña,nick,edad,sexo):
        if isinstance (correo,str) and isinstance (contraseña,str) and isinstance (nick,str) and isinstance (edad,int) and isinstance (sexo,str):
            self.cursor.execute ("INSERT INTO PlayerData (Correo,Contraseña,Nick,Edad,Sexo)  VALUES('"+ correo +"','"+contraseña+"','"+nick+"','"+str(edad)+"','"+sexo+"');")
            self.db.commit()
        else:
           print ( "Invalid Type db_insert_PlayerData") 
    
    def db_insert_Player_Game       (self,id_player,id_game,resultado):
        if isinstance (id_player,int) and isinstance (id_game,int) and isinstance (resultado,str):
            if resultado == "V" or resultado == "P" or resultado == "E":
                self.cursor.execute ("INSERT INTO Player_Game (ID_Player,ID_Game,Resultado)  VALUES('"+ str(id_player) +"','"+str(id_game)+"','"+resultado+"');")
                self.db.commit()
            else:
                print ( "Erro: ",resultado," Invalid Data")   
        else:
           print ( "Invalid Type db_insert_Player_Game") 

    def db_insert_Game              (self,duracion):
        if isinstance (duracion,int) :
            self.cursor.execute ("INSERT INTO Game (Duracion)  VALUES('"+ str(duracion) +"');")
            self.db.commit() 
        else:
           print ( "Invalid Type db_insert_Game")          

    def db_insert_PlayerRecord      (self,id_player,pg,pp,pe,puntos):
        if isinstance (id_player,int) and isinstance (pg,int) and isinstance (pp,int) and isinstance (pe,int) and isinstance (puntos,int):
            self.cursor.execute ("INSERT INTO PlayerRecord (ID_Player,Partidas_Ganadas,Partidas_Perdidas,Partidas_Empatadas,Puntaje_Acumulado)  VALUES('"+ str(id_player) +"','"+str(pg)+"','"+str(pp)+"','"+str(pe)+"','"+str(puntos)+"');")
            self.db.commit()   
        else:
           print ( "Invalid Type db_insert_PlayerRecord")         

# Busca en las tablas una fila      
    def db_serch_PlayerData         (self,id_player):
        if isinstance (id_player,int):
            self.cursor.execute ("SELECT * FROM PlayerData where ID_Player = " + str(id_player)+";")
            fila = self.cursor.fetchone() #Seleciona la Primera (unica encontrada)
            if fila != None:
                return fila
            else:
                return False
        else:
           print ( "Error id_player: ",id_player,"invalid type")         

    def db_serch_Player_Game        (self,id_player_game):
        if isinstance (id_player_game,int):
            self.cursor.execute ("SELECT * FROM Player_Game where ID_player_game = " + str(id_player_game)+";")
            fila = self.cursor.fetchone() #Seleciona la Primera (unica encontrada)
            if fila != None:
                return fila
            else:
                return False
        else:
           print ( "Error id_player_game: ",id_player_game,"invalid type") 

    def db_serch_Game               (self,id_game):
        if isinstance (id_game,int):
            self.cursor.execute ("SELECT * FROM Game where ID_Game = " + str(id_game)+";")
            fila = self.cursor.fetchone() #Seleciona la Primera (unica encontrada)
            if fila != None:
                return fila
            else:
                return False
        else:
           print ( "Error id_game: ",id_game,"invalid type") 

    def db_serch_PlayerRecord       (self,id_player):
        if isinstance (id_player,int):
            self.cursor.execute ("SELECT * FROM PlayerRecord where ID_Player = " + str(id_player)+";")
            fila = self.cursor.fetchone() #Seleciona la Primera (unica encontrada)
            if fila != None:
                return fila
            else:
                return False
        else:
           print ( "Error id_player: ",id_player,"invalid type") 

# Borra de las tablas una fila 
    def db_delete_PlayerData        (self,id_player):
        if isinstance (id_player,int):
            self.cursor.execute ("DELETE FROM PlayerData WHERE ID_Player = " + str(id_player)+";")
            self.db.commit()
        else:
           print ( "Error id_player: ",id_player,"invalid type")         

    def db_delete_Player_Game       (self,id_player_game):
        if isinstance (id_player_game,int):
            self.cursor.execute ("DELETE FROM Player_Game WHERE ID_player_game = " + str(id_player_game)+";")
            self.db.commit()
        else:
           print ( "Error id_player_game: ",id_player_game,"invalid type")         

    def db_delete_Game              (self,id_game):
        if isinstance (id_game,int):
            self.cursor.execute ("DELETE FROM Game WHERE ID_Game = " + str(id_game)+";")
            self.db.commit()
        else:
           print ( "Error id_game: ",id_game,"invalid type")         

    def db_delete_PlayerRecord      (self,id_player):
        if isinstance (id_player,int):
            self.cursor.execute ("DELETE FROM PlayerRecord WHERE ID_Player = " + str(id_player)+";")
            self.db.commit()
        else:
           print ( "Error id_player: ",id_player,"invalid type")         

# Actualizacion de las Tablas     
    def db_update_PlayerData        (self,id_player,correo,contraseña,nick,edad,sexo):
        if isinstance (id_player,int) and isinstance (correo,str) and isinstance (contraseña,str) and isinstance (nick,str) and isinstance (edad,int) and isinstance (sexo,str):
            self.cursor.execute ("UPDATE PlayerData" 
                                " SET Correo='"+correo+"',Contraseña='"+contraseña+"', Nick='"+nick+"', Edad="+str(edad)+", Sexo='"+sexo+"'"+
                                " WHERE ID_Player= "+ str(id_player)+";")
            self.db.commit() 
        else:
           print ( "Error nombre_archivo: ",nombre_archivo,"invalid type") 
    
    def db_update_Player_Game       (self,id_player_game,id_player,id_game,resultado): 
        if isinstance (id_player,int) and isinstance (id_game,int) and isinstance (resultado,str):
            if resultado == "V" or resultado == "P" or resultado == "E":
                self.cursor.execute ("UPDATE Player_Game" 
                                     " SET ID_Player='"+str(id_player)+"',ID_Game='"+str(id_game)+"', Resultado='"+resultado+"'"+
                                     " WHERE ID_player_game= "+ str(id_player_game)+";")
                self.db.commit()
            else:
                print ( "Erro: ",resultado," Invalid Data")   
        else:
           print ( "Invalid Type") 

    def db_update_Game              (self,id_game,duracion): 
        if isinstance (id_game,int) and isinstance (duracion,int) :
            self.cursor.execute ("UPDATE Game" 
                                " SET Duracion='"+str(duracion)+"'"+
                                " WHERE ID_Game= "+ str(id_game)+";")
            self.db.commit()    
        else:
           print ( "Invalid Type") 
    
    def db_update_PlayerRecord      (self,id_player,pg,pp,pe,puntos): 
        if isinstance (id_player,int) and isinstance (pg,int) and isinstance (pp,int) and isinstance (pe,int) and isinstance (puntos,int):
            self.cursor.execute ("UPDATE PlayerRecord" 
                                 " SET Partidas_Ganadas='"+str(pg)+"',Partidas_Perdidas='"+str(pp)+"', Partidas_Empatadas='"+str(pe)+"', Puntaje_Acumulado='"+str(puntos)+"'"+
                                 " WHERE ID_Player= "+ str(id_player)+";")
            self.db.commit()  
        else:
           print ( "Invalid Type")         

#Devuelve el numero de filas
    def db_rowsnumber_PlayerData    (self):
        self.cursor.execute ("SELECT * FROM PlayerData ;")
        rows = self.cursor.fetchall() #Seleciona Todas
        return (len(rows))

    def db_rowsnumber_Player_Game   (self):
        self.cursor.execute ("SELECT * FROM Player_Game ;")
        rows = self.cursor.fetchall() #Seleciona Todas
        return (len(rows))

    def db_rowsnumber_Game          (self):
        self.cursor.execute ("SELECT * FROM Game ;")
        rows = self.cursor.fetchall() #Seleciona Todas
        return (len(rows))

    def db_rowsnumber_PlayerRecord  (self):
        self.cursor.execute ("SELECT * FROM PlayerRecord ;")
        rows = self.cursor.fetchall() #Seleciona Todas
        return (len(rows))              

#Funcione con Combinacion de Tablas.
    #New Player
    def NewPlayer           (self,correo,contraseña,nick,edad,sexo):
        # Uso la funcion Para insertar en la Tabla Player Data
        self.db_insert_PlayerData (correo,contraseña,nick,edad,sexo)
        # Ordeno la Tabla PlayerData de maner descendente y tomo el primer valor ID_Player
        self.cursor.execute ("SELECT ID_Player FROM PlayerData ORDER BY ID_Player DESC LIMIT 1;")
        ID = self.cursor.fetchone() #Me devuelve la Tupla
        id_player = int(ID[0]) #Tomo el Primer Valor de Tupla
        self.db_insert_PlayerRecord (id_player,0,0,0,0)

    #New Game
    def NewGame             (self,duracion,id_jugadorUno,id_jugadorDos,Resultado_JugadorUno,Resultado_JugadorDos):
        self.db_insert_Game (duracion)
        self.cursor.execute ("SELECT ID_Game FROM Game ORDER BY ID_Game DESC LIMIT 1;")
        ID = self.cursor.fetchone() #Me devuelve la Tupla
        id_game = ID[0]             #Tomo el Primer Valor de Tupla
        self.db_insert_Player_Game (id_jugadorUno,id_game,Resultado_JugadorUno)
        self.db_insert_Player_Game (id_jugadorDos,id_game,Resultado_JugadorDos)

    #Resultado del Juego:
    def NewGameResult             (self,jugadorUno_id,jugadorUno_pg,jugadorUno_pp,jugadorUno_pe,jugadorUno_puntos,jugadorDos_id,jugadorDos_pg,jugadorDos_pp,jugadorDos_pe,jugadorDos_puntos):
        self.db_update_PlayerRecord      (jugadorUno_id,jugadorUno_pg,jugadorUno_pp,jugadorUno_pe,jugadorUno_puntos)
        self.db_update_PlayerRecord      (jugadorDos_id,jugadorDos_pg,jugadorDos_pp,jugadorDos_pe,jugadorDos_puntos)

    #Devuelve Todos los Datos de un player
    def Serch_PlayerData    (self,id_player):
        if isinstance (id_player,int):
            self.cursor.execute ("SELECT "
                                 "PlayerData.ID_Player,"
                                 "PlayerData.Nick,"
                                 "PlayerData.Edad,"
                                 "PlayerData.Sexo,"
                                 "PlayerData.Correo,"
                                 "PlayerData.Contraseña,"
                                 "PlayerRecord.Partidas_Ganadas,"
                                 "PlayerRecord.Partidas_Empatadas,"
                                 "PlayerRecord.Partidas_Perdidas,"
                                 "PlayerRecord.Puntaje_Acumulado "
                                 "FROM PlayerData,PlayerRecord "
                                 "WHERE PlayerData.ID_Player = PlayerRecord.ID_Player "
                                        "AND PlayerData.ID_Player ="+str(id_player)+";")
            player = self.cursor.fetchall()
            #Devuelve: ID_Player,Nick,Edad,Sexo,Mail,Contraseña,PG,PE,PP,Puntaje Acumulado
            return(player)
        else:
           print ( "Error id_player: ",id_player,"invalid type")         
    
    #Devuelve Todos los Datos de un Juego
    def Serch_Game          (self,id_game):
        if isinstance (id_game,int):        
            self.cursor.execute ("SELECT "
                                 "Game.ID_Game,"
                                 "Game.Duracion,"
                                 "Player_Game.ID_Player,"
                                 "PlayerData.Nick,"
                                 "Player_Game.Resultado "
                                 "FROM Game,Player_Game,PlayerData "
                                 "WHERE Game.ID_Game = Player_Game.ID_Game "
                                        "AND Player_Game.ID_Player = PlayerData.ID_Player "
                                        "AND Game.ID_Game ="+str(id_game)+";")
            game = self.cursor.fetchall()
            #Devuelve: Game_ID, Duracion, ID_Player, Nick, Resultado
            return(game) 
        else:
           print ( "Error id_game: ",id_game,"invalid type")    
    
    #Devuelve Todos los Datos de Todos los Jugadores
    def AllPlayersData      (self):
        self.cursor.execute ("SELECT "
                                 "PlayerData.ID_Player,"
                                 "PlayerData.Nick,"
                                 "PlayerData.Edad,"
                                 "PlayerData.Sexo,"
                                 "PlayerData.Correo,"
                                 "PlayerData.Contraseña,"
                                 "PlayerRecord.Partidas_Ganadas,"
                                 "PlayerRecord.Partidas_Empatadas,"
                                 "PlayerRecord.Partidas_Perdidas,"
                                 "PlayerRecord.Puntaje_Acumulado "
                                 "FROM PlayerData,PlayerRecord "
                                 "WHERE PlayerData.ID_Player = PlayerRecord.ID_Player ;")
        players = self.cursor.fetchall()
        #Devuelve: ID_Player,Nick,Edad,Sexo,Mail,Contraseña,PG,PE,PP,Puntaje Acumulado
        return(players)
