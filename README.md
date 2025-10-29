# Backgammon Game

### Alumno: Federico Barboza - Legajo: [64281]

## Descripción

Implementación completa del juego de Backgammon con interfaz gráfica (Pygame) y CLI. El proyecto incluye todas las reglas oficiales del juego, testing exhaustivo, documentación detallada y un diseño basado en principios SOLID.

## Requisitos Previos

1. Instalar Python 3.11+
2. Crear un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```
3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Cómo Ejecutar

### Ejecutar la aplicación con interfaz gráfica (Pygame)

```bash
python main.py
```

### Ejecutar la aplicación con CLI (Consola)

```bash
python -m backgammon.cli.console
```

## Uso de la Interfaz Pygame

### Controles:

- **Clic del mouse**: Seleccionar fichas y realizar movimientos

### Cómo Jugar en Pygame:

1. Al iniciar, se realiza una tirada automática para determinar quién juega primero
2. Haz clic en una ficha para seleccionarla (se resalta con un círculo verde)
3. Haz clic en un destino válido para mover la ficha
4. El juego cambia de turno automáticamente cuando no hay movimientos disponibles
5. Gana el jugador que saque todas sus fichas primero del tablero

### Indicadores Visuales:

- **Círculo verde**: Destinos válidos para la ficha seleccionada
- **Visualización de dados**: Muestra la tirada actual y los dados disponibles
- **Indicador de turno**: Muestra de quién es el turno actual
- **Mensaje de victoria**: Se muestra cuando un jugador gana
- **Barra central**: Muestra las fichas capturadas (blancas arriba, negras abajo)
- **Zona de bear-off**: A la derecha del tablero, muestra las fichas que han salido

## Uso de la Interfaz CLI

La interfaz de consola (CLI) te permite jugar Backgammon directamente desde tu terminal. Es ideal para partidas rápidas y para entender la lógica del juego sin distracciones.

### Cómo Jugar en CLI:

1. **Inicio del Juego**:
   - Ejecuta el comando `python -m backgammon.cli.console`.
   - El juego te pedirá que introduzcas el nombre para el Jugador 1 (blancas) y el Jugador 2 (negras). Si no introduces un nombre, se usarán "Blanco" y "Negro" por defecto.

2. **Lanzar los Dados**:
   - El juego te indicará de quién es el turno.
   - Presiona `ENTER` para lanzar los dados. Los resultados se mostrarán en pantalla.

3. **Ver el Tablero**:
   - Después de lanzar los dados, se mostrará una representación textual del tablero.
   - Las fichas se representan por su inicial (`B` para blancas, `N` para negras).
   - La barra central y las fichas que han salido del juego (bear-off) también se muestran.

4. **Seleccionar un Movimiento**:
   - El juego calculará y mostrará una lista numerada de todos los movimientos legales que puedes hacer con los dados obtenidos.
   - Cada opción describe la secuencia de movimientos (origen, destino y dado utilizado). Ejemplo: `1: 24 -> 18 (Dado: 6) | 18 -> 16 (Dado: 2)`.
   - Si una ficha es capturada, se indicará con `[Captura]`.

5. **Introducir tu Elección**:
   - Escribe el número del movimiento que deseas realizar y presiona `ENTER`.
   - El juego aplicará el movimiento y actualizará el estado del tablero.

6. **Finalizar el Turno**:
   - Una vez realizado el movimiento, presiona `ENTER` para pasar el turno al siguiente jugador.

7. **Ganar la Partida**:
   - El juego termina cuando un jugador ha sacado (bear-off) todas sus 15 fichas del tablero.
   - Se mostrará un mensaje indicando quién es el ganador.

### Ejemplo de Interacción en CLI:

```
$ python -m backgammon.cli.console
Nombre jugador 1 (blancas): JugadorA
Nombre jugador 2 (negras): JugadorB

--- Turno de JugadorA (blancas) ---
... (tablero) ...
Presiona ENTER para lanzar los dados...
Dados lanzados: [5, 2]

JugadorA, selecciona tu movimiento:
1: 8 -> 3 (Dado: 5) | 6 -> 4 (Dado: 2)
2: 6 -> 1 (Dado: 5) | 13 -> 11 (Dado: 2)
Ingrese el número de movimiento (1-2): 1

Movimiento aplicado.
Presiona ENTER para finalizar tu turno...
```

## Estructura del Proyecto

```
backgammon/
├── core/                 # Lógica del juego
│   ├── backgammon.py    # Clase principal del juego
│   ├── board.py         # Tablero y reglas
│   ├── player.py        # Jugador
│   ├── checker.py       # Ficha individual
│   ├── dice.py          # Dados
│   └── move.py          # Movimiento
├── pygame_ui/           # Interfaz gráfica
│   └── ui.py            # Implementación Pygame
├── cli/                 # Interfaz de consola
│   └── console.py       # Implementación CLI
└── tests/               # Tests unitarios
    ├── test_board.py
    ├── test_player.py
    ├── test_dice.py
    └── ...
```

## Reglas Implementadas

- ✅ Movimientos básicos según el resultado de los dados
- ✅ Dobles (lanzar el mismo número en ambos dados da 4 movimientos)
- ✅ Capturas y reingresos desde la barra
- ✅ Prioridad de la barra (debes reingresar antes de mover otras fichas)
- ✅ Bear-off (sacar fichas cuando todas están en el cuadrante final)
- ✅ Bloqueos (puntos con 2+ fichas del mismo color)
- ✅ Detección automática de fin de juego
- ✅ Tirada inicial para determinar el primer jugador

## Testing

Ejecutar todos los tests:

```bash
pytest
```

Ejecutar tests con cobertura:

```bash
pytest --cov=backgammon --cov-report=html
```

Ver reporte de cobertura:

```bash
# El reporte se genera en htmlcov/index.html
```

## Documentación

- **CHANGELOG.md**: Registro detallado de todas las versiones y cambios
- **JUSTIFICACION.md**: Justificación del diseño, clases y decisiones técnicas
- **prompts/**: Documentación de todos los prompts de IA utilizados
  - `prompts-desarrollo.md`: Prompts relacionados con desarrollo
  - `prompts-documentacion.md`: Prompts relacionados con documentación
  - `prompts-testing.md`: Prompts relacionados con testing
- **plantaUML.mermaid**: Diagrama UML completo de las clases del core

## Principios de Diseño

El proyecto sigue los principios SOLID:

- **S**ingle Responsibility: Cada clase tiene una única responsabilidad
- **O**pen/Closed: Abierto a extensión, cerrado a modificación
- **L**iskov Substitution: Las clases derivadas pueden sustituir a sus bases
- **I**nterface Segregation: Interfaces específicas mejor que generales
- **D**ependency Inversion: Depender de abstracciones, no de concreciones

## Tecnologías Utilizadas

- **Python 3.11+**: Lenguaje de programación
- **Pygame**: Interfaz gráfica
- **pytest**: Framework de testing
- **GitHub Copilot / Jules**: Asistencia con IA (documentado en carpeta prompts/)

## Autor

**Federico Barboza**  
Legajo: [64281]  
Repositorio: [computacion-2025-backgammon-BarbozaFederico](https://github.com/BarbozaFederico/computacion-2025-backgammon-BarbozaFederico)

## Licencia

Este proyecto es parte del curso de Computación 2025.
