								Tateti 2020 Versión Alpha 1.0

								Trabajo Práctico TUP 2020

						    Integrantes:
								•Oviedo Codigoni, Carlos Nicolas 	- ROL: Lider
								•Ortíz López, Mauricio 			- ROL: Tester
								•Mora Maisonave, Gabriel		- ROL: Documentador



Librerías Utilizadas 

•	PyQt5
•	PyQt5.QtWidgets
•	PyQt5.QtMultimedia
•	PyQt5.QtCore
•	PyQt5.QtGui
•	Sqlite3
•	Random 





									MANUAL DE USUARIO
								TA-TE-TI 2020 VERSIÓN ALPHA 1.0
	

								PROYECTO FINAL PROGRAMACION II



			  						   INTEGRANTES

		    						    CARLOS OVIEDO CODIGONI
		    						     MAURICIO ORTIZ LOPEZ
							       GABRIEL SANTIAGO MORA MAISONAVE


Introducción

El Ta-Te-Ti es un juego infantil, posee nueve casilleros y consiste en colocar uno de los participantes un botón en un punto de cruce de los casilleros; el adversario hace otro tanto y continúan de forma alternada hasta cubrir 8 de las intersecciones. Luego uno mueve su ficha al punto que ha quedado vacante, y el otro la suya, hasta que termina el juego por haber colocado los botones en línea recta o haberse ocupado todos los casilleros.


1. Configuración inicial

	1.1. Crear nuevo jugador: Para crear un nuevo jugador debe acceder a la pestaña superior izquierda “Perfiles”, al hacer click se despliega un menú en cascada donde debe seleccionar la opción “Crear Perfil”. Una vez seleccionada la opción “Crear Perfil”, se abrirá un nuevo menú donde debe ingresar los datos del nuevo jugador.

	1.2. Modificar Jugador: Para modificar un jugador de la base de datos del juego debe acceder a la pestaña superior izquierda “Perfiles”, al hacer click se despliega un menú en cascada donde debe seleccionar la opción “Modificar”. Una vez seleccionada la opción “Modificar”, deberá logearse ingresando su nick y contraseña, después de haberse logeado se abrirá el menú “Crear Perfil”, donde podrá realizar las modificaciones que desee, al finalizar debe presionar el botón “Guardar Cambios”.

	1.3. Eliminar Jugador: Para eliminar un jugador de la base de datos del juego debe acceder a la pestaña superior izquierda “Perfiles”, al hacer click se despliega un menú en cascada donde debe seleccionar la opción “Eliminar”. Una vez seleccionada la opción “Eliminar”, deberá logearse ingresando su nick y contraseña, después de haberse logeado podrá eliminar el perfil haciendo click en “Eliminar”.


2. Guía del producto: 

	2.1. Partida Rápida: Partida rápida es la forma más ágil de jugar, puede seleccionar jugar contra la PC o versus otro jugador.

	2.1.1. Humano vs Humano: Aquí debe ingresar el Nick de los dos jugadores, el cual no puede ser PC y presionar el botón “Jugar”. El jugador 1, tendrá la X en el juego, mientras que el jugador 2 poseerá O.

	2.1.2. Humano vs PC: Aquí debe ingresar el Nick del jugador 1 y presionar el botón “Jugar”.

2.2. Campeonato: La opción campeonato genera el fixture automático de los cruces entre jugadores. En primer instancia debe seleccionar la cantidad de jugadores, debe seleccionar de la lista de jugadores los participantes (en caso de no estar el jugador que desea, tiene la opción de crear uno haciendo click en “Crear Jugador”) una vez seleccionado los participantes, presione el botón “Crear Campeonato” y se crearan los cruces de forma automática. El campeonato consta de dos cruces por jugadores. Para iniciar el juego debe presionar el botón jugar.

	2.3. Tabla de Puntajes: En la tabla de puntaje se encuentra el historial de partidas y puntos de cada jugador. Puede acceder en la pestaña superior “Puntajes”, al hacer click se despliega la información del historial.

2.3.1.	Puntajes: 
	2.3.1.1. Victoria: 2 Puntos
	2.3.1.2. Empate: 1 Punto
	2.3.1.3. Derrota: 0 Puntos


Instalación

1.	Descargar e instalar Python
	1.1.	Descargar interprete de Python: Ir a python.org/downloads y conseguir la versión actual.
	1.2.	Instalar: Ejecutamos como administrador, debe marcar la opción Install launcher for all users y la opción Add Python 3.8 (o la versión que descargue) to PATH. Una vez configurado haga click en Install Now.
	1.3.	Probar el interprete: Presione la combinación de teclas Windows + R (ejecutar), en la caja que le aparece escriba Python y presione enter. Le saldrá una ventana (consola) con la versión de Python instalada, para salir escriba exit.

2.	Descargar e instalar PyQt5
	2.1.	Abrir una terminal(cmd), escriba el comando pip install pyqt5 y pip install pyqt5-tools

Ejecución 

	Extraiga la carpeta Ta-Te-Ti Alpha y ejecute TaTeTi


Versiones de Python y QT
	•	Python 3.8.5
	•	PyQt 5



