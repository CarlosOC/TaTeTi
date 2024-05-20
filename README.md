# TaTeTi 
## Versión Alpha 1.0

![Tablero](https://github.com/CarlosOC/TaTeTi/blob/main/ScreenShot/Tablero.png)

### Introducción
Revive la diversión del TaTeTi con este juego épico. Desafía a tus amigos, juega contra la IA y crea tu propio legado en la tabla de puntajes. TaTeTi o Tres en línea consiste en un tablero de nueve casillas, donde los jugadores colocan de forma alternada círculos (O) y equis (X) en un intento por alinear tres de sus símbolos de manera horizontal, vertical o diagonal antes que su oponente.

#### Características destacadas:
- **Modos de juego variados:** Humano vs Humano, Humano vs PC y Campeonato.
- **Perfiles de jugador:** Crea, personaliza y guarda tu progreso.
- **Tabla de puntajes:** Sigue tu rendimiento y el de tus amigos.
- **Interfaz intuitiva:** Fácil de usar para jugadores de todas las edades.

### Reglas del juego
Cada jugador solo puede colocar su símbolo una vez por turno y no sobre una casilla ya jugada. Se debe conseguir realizar una línea recta o diagonal con tres de sus símbolos para ganar la partida.

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
   - Descarga el intérprete de Python desde [python.org/downloads](https://www.python.org/downloads/).
   - Instálalo como administrador, marcando la opción "Install launcher for all users" y "Add Python 3.8 (o la versión que descargaste) to PATH".

2. **Descargar e instalar PyQt5:**
   - Abre una terminal (cmd) y escribe los comandos `pip install pyqt5` y `pip install pyqt5-tools`.

### Ejecución 

1. Extrae la carpeta "Ta-Te-Ti Alpha" y ejecuta "TaTeTi".

### Versiones de Python y QT

- Python 3.8.5
- PyQt 5
