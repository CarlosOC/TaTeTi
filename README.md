								Tateti 2020 Versi�n Alpha 1.0

								Trabajo Pr�ctico TUP 2020

						    Integrantes:
								�Oviedo Codigoni, Carlos Nicolas 	- ROL: Lider
								�Ort�z L�pez, Mauricio 			- ROL: Tester
								�Mora Maisonave, Gabriel		- ROL: Documentador



Librer�as Utilizadas 

�	PyQt5
�	PyQt5.QtWidgets
�	PyQt5.QtMultimedia
�	PyQt5.QtCore
�	PyQt5.QtGui
�	Sqlite3
�	Random 





									MANUAL DE USUARIO
								TA-TE-TI 2020 VERSI�N ALPHA 1.0
	

								PROYECTO FINAL PROGRAMACION II



			  						   INTEGRANTES

		    						    CARLOS OVIEDO CODIGONI
		    						     MAURICIO ORTIZ LOPEZ
							       GABRIEL SANTIAGO MORA MAISONAVE


Introducci�n

El Ta-Te-Ti es un juego infantil, posee nueve casilleros y consiste en colocar uno de los participantes un bot�n en un punto de cruce de los casilleros; el adversario hace otro tanto y contin�an de forma alternada hasta cubrir 8 de las intersecciones. Luego uno mueve su ficha al punto que ha quedado vacante, y el otro la suya, hasta que termina el juego por haber colocado los botones en l�nea recta o haberse ocupado todos los casilleros.


1. Configuraci�n inicial

	1.1. Crear nuevo jugador: Para crear un nuevo jugador debe acceder a la pesta�a superior izquierda �Perfiles�, al hacer click se despliega un men� en cascada donde debe seleccionar la opci�n �Crear Perfil�. Una vez seleccionada la opci�n �Crear Perfil�, se abrir� un nuevo men� donde debe ingresar los datos del nuevo jugador.

	1.2. Modificar Jugador: Para modificar un jugador de la base de datos del juego debe acceder a la pesta�a superior izquierda �Perfiles�, al hacer click se despliega un men� en cascada donde debe seleccionar la opci�n �Modificar�. Una vez seleccionada la opci�n �Modificar�, deber� logearse ingresando su nick y contrase�a, despu�s de haberse logeado se abrir� el men� �Crear Perfil�, donde podr� realizar las modificaciones que desee, al finalizar debe presionar el bot�n �Guardar Cambios�.

	1.3. Eliminar Jugador: Para eliminar un jugador de la base de datos del juego debe acceder a la pesta�a superior izquierda �Perfiles�, al hacer click se despliega un men� en cascada donde debe seleccionar la opci�n �Eliminar�. Una vez seleccionada la opci�n �Eliminar�, deber� logearse ingresando su nick y contrase�a, despu�s de haberse logeado podr� eliminar el perfil haciendo click en �Eliminar�.


2. Gu�a del producto: 

	2.1. Partida R�pida: Partida r�pida es la forma m�s �gil de jugar, puede seleccionar jugar contra la PC o versus otro jugador.

	2.1.1. Humano vs Humano: Aqu� debe ingresar el Nick de los dos jugadores, el cual no puede ser PC y presionar el bot�n �Jugar�. El jugador 1, tendr� la X en el juego, mientras que el jugador 2 poseer� O.

	2.1.2. Humano vs PC: Aqu� debe ingresar el Nick del jugador 1 y presionar el bot�n �Jugar�.

2.2. Campeonato: La opci�n campeonato genera el fixture autom�tico de los cruces entre jugadores. En primer instancia debe seleccionar la cantidad de jugadores, debe seleccionar de la lista de jugadores los participantes (en caso de no estar el jugador que desea, tiene la opci�n de crear uno haciendo click en �Crear Jugador�) una vez seleccionado los participantes, presione el bot�n �Crear Campeonato� y se crearan los cruces de forma autom�tica. El campeonato consta de dos cruces por jugadores. Para iniciar el juego debe presionar el bot�n jugar.

	2.3. Tabla de Puntajes: En la tabla de puntaje se encuentra el historial de partidas y puntos de cada jugador. Puede acceder en la pesta�a superior �Puntajes�, al hacer click se despliega la informaci�n del historial.

2.3.1.	Puntajes: 
	2.3.1.1. Victoria: 2 Puntos
	2.3.1.2. Empate: 1 Punto
	2.3.1.3. Derrota: 0 Puntos


Instalaci�n

1.	Descargar e instalar Python
	1.1.	Descargar interprete de Python: Ir a python.org/downloads y conseguir la versi�n actual.
	1.2.	Instalar: Ejecutamos como administrador, debe marcar la opci�n Install launcher for all users y la opci�n Add Python 3.8 (o la versi�n que descargue) to PATH. Una vez configurado haga click en Install Now.
	1.3.	Probar el interprete: Presione la combinaci�n de teclas Windows + R (ejecutar), en la caja que le aparece escriba Python y presione enter. Le saldr� una ventana (consola) con la versi�n de Python instalada, para salir escriba exit.

2.	Descargar e instalar PyQt5
	2.1.	Abrir una terminal(cmd), escriba el comando pip install pyqt5 y pip install pyqt5-tools

Ejecuci�n 

	Extraiga la carpeta Ta-Te-Ti Alpha y ejecute TaTeTi


Versiones de Python y QT
	�	Python 3.8.5
	�	PyQt 5



