
class player:
    #PJ: Numero de partidos Jugados.  - 
    #PG: Numero de partidos Ganados.  -  Genera  2 Puntos
    #PP: Numero de partidos Perdidos. -  Genera -1 Puntos
    #PE: Numero de partidos Empatados.-  Genera  1 Puntos 
    #Puntos: Puntaje         
    def __init__(self,id,nick,edad,sexo,mail,password,PG,PE,PP,puntos):
        
        if isinstance (id,int):
            self.id = id
        else:
           print ( "Error id: ",id,"invalid type")

        if isinstance (mail,str):
            self.mail = mail
        else:
           print ( "Error Nombre Player: ",mail,"invalid type")
        
        if isinstance (password,str):
            self.password = password
        else:
           print ( "Error password: ",password,"invalid type")  
        
        if isinstance (nick,str):
            self.nick = nick
        else:
           print ( "Error nick: ",nick,"invalid type")  
        
        if isinstance (edad,int):
            self.edad = edad
        else:
           print ( "Error edad: ",edad,"invalid type")  
        
        if isinstance (sexo,str):
            self.sexo = sexo
        else:
           print ( "Error sexo: ",sexo,"invalid type")
            
        if isinstance (PG,int):
            self.PG = PG
        else:
           print ( "Error PG: ",PG,"invalid type") 
        
        if isinstance (PE,int):
            self.PE = PE
        else:
           print ( "Error PE: ",PE,"invalid type") 
        if isinstance (PP,int):
            self.PP = PP
        else:
           print ( "Error PP: ",PP,"invalid type") 
        self.PJ = 0 

        if isinstance (puntos,int):
            self.puntos = puntos
        else:
           print ( "Error puntos: ",puntos,"invalid type")   

    #Carga en el Jugador Partido Jugado,Partido Ganado,Partido Perdido,Partido Empatado
    def GamePlayed(self,PJ,PG,PP,PE):
        if isinstance (PJ,int):
            self.PJ = self.PJ+PJ
        else:
           print ( "Error PJ: ",PJ,"invalid type")  
        
        if isinstance (PG,int):
            self.PG = self.PG + PG
        else:
           print ( "Error PG: ",PG,"invalid type") 
       
        if isinstance (PP,int):
            self.PP = self.PP + PP
        else:
           print ( "Error PE: ",PP,"invalid type") 
        
        if isinstance (PE,int):
            self.PE = self.PE + PE
        else:
           print ( "Error PE: ",PE,"invalid type") 

    #Metodos para Editar:
    def edit_mail(self,mail):
        if isinstance (mail,str):
            self.mail = mail
        else:
           print ( "Error Nombre Player: ",mail,"invalid type")

    def edit_nick(self,nick):
        if isinstance (nick,str):
            self.nick = nick
        else:
           print ( "Error nick: ",nick,"invalid type")  

    def edit_password(self,password):
        if isinstance (password,str):
            self.password = password
        else:
           print ( "Error password: ",password,"invalid type")  

    def edit_edad(self,edad):
        if isinstance (edad,int):
            self.edad = edad
        else:
           print ( "Error edad: ",edad,"invalid type")  

    def edit_sexo(self,sexo):
        if isinstance (sexo,str):
            self.sexo = sexo
        else:
           print ( "Error sexo: ",sexo,"invalid type")
                                       
    #Devuelve Partidos Jugados    
    def Paridos_Jugados (self):
        self.PJ = self.PG+self.PE+self.PP
        return (self.PJ)  
    #Devuelve Partidos Ganados

    #Devuelve Calculo de Puntaje y Devuelve Puntos    
    def Puntos (self):
        self.puntos = (self.PG) * 2 + (self.PE)
        return (self.puntos)  

    # Metodos para comparar puntaje:
    def __eq__(self, otro): #Si Tiene el mismo puntaje
        if self.puntos == otro.puntos:
            return True
        else:
            return False

    def __lt__(self, otro): #Si el mismo puntaje es menor
        if self.puntos < otro.puntos:
            return True
        else:
            return False

    def __gt__(self, otro): #Si el mismo puntaje es mayor
        if self.puntos > otro.puntos:
            return True
        else:
            return False

    def __str__(self):                                          #id,nick,edad,sexo,mail,password,PG,PE,PP,puntos
        return '{0} {1} {2} {3} {4} {5} {6} {7} {8} {9}'.format(self.id,self.nick,self.edad,self.sexo,self.mail,self.password,self.PG,self.PE,self.PP,self.puntos)
             