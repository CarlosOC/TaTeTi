##								TaTeTi 
Versión Alpha 1.0
### Introducción
TaTeTi o Tres en Linea es un juego infantil que consiste en un tablero de nueve casillas, donde los participantes colocan de forma alternada círculos (O) y equis (X) en un intento por alinear tres de sus símbolos de manera horizontal, vertical o diagonal antes que su oponente.
### Reglas:
Cada jugador solo debe colocar su símbolo una vez por turno y no debe ser sobre una casilla ya jugada. En caso de que el jugador haga trampa el ganador será el otro. Se debe conseguir realizar una línea recta o diagonal por símbolo.

### Librerías Utilizadas 

- PyQt5
- PyQt5.QtWidgets
- PyQt5.QtMultimedia
- PyQt5.QtCore
- PyQt5.QtGui
- Sqlite3
- Random 



### Configuración inicial

1. **Crear nuevo jugador:** Accede a la pestaña "Perfiles" y selecciona "Crear Perfil" para ingresar los datos del nuevo jugador.
   
2. **Modificar Jugador:** Desde la pestaña "Perfiles", elige "Modificar", ingresa tu nick y contraseña, luego podrás editar tu perfil y guardar los cambios.

3. **Eliminar Jugador:** En la pestaña "Perfiles", selecciona "Eliminar", ingresa tu nick y contraseña, y luego elimina tu perfil.

### Guía del producto

1. **Partida Rápida:**
   - **Humano vs Humano:** Ingresa los nicks de ambos jugadores y presiona "Jugar".
   - **Humano vs PC:** Ingresa el nick del jugador 1 y presiona "Jugar".

2. **Campeonato:**
   - Crea el fixture de cruces entre jugadores automáticamente, selecciona la cantidad de jugadores, elige los participantes y haz click en "Crear Campeonato".

3. **Tabla de Puntajes:**
   - Muestra el historial de partidas y puntos de cada jugador. Accede en la pestaña "Puntajes".

   **Puntajes:**
   - Victoria: 2 Puntos
   - Empate: 1 Punto
   - Derrota: 0 Puntos

### Instalación

1. **Descargar e instalar Python:**
   - Descarga el intérprete de Python desde python.org/downloads.
   - Instálalo como administrador, marcando la opción "Install launcher for all users" y "Add Python 3.8 (o la versión que descargaste) to PATH".

2. **Descargar e instalar PyQt5:**
   - Abre una terminal (cmd) y escribe los comandos `pip install pyqt5` y `pip install pyqt5-tools`.

### Ejecución 

1. Extrae la carpeta "Ta-Te-Ti Alpha" y ejecuta "TaTeTi".

### Versiones de Python y QT

- Python 3.8.5
- PyQt 5

