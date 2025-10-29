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



### Cómo Jugar en CLI:



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
Legajo: [Tu Legajo]  
Repositorio: [computacion-2025-backgammon-BarbozaFederico](https://github.com/BarbozaFederico/computacion-2025-backgammon-BarbozaFederico)

## Licencia

Este proyecto es parte del curso de Computación 2025.
