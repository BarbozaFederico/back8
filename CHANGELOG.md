# Changelog

Todas las modificaciones notables de este proyecto serán documentadas en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/),
y este proyecto sigue [Semantic Versioning](https://semver.org/lang/es/).

## [1.6.5] - 2025-10-29

### Added

- docs: Se completó el archivo `JUSTIFICACION.md` con una documentación exhaustiva y accesible del diseño del proyecto.
  - Se justifica cada clase (Checker, Dice, Player, Board, Move, BackgammonGame) de forma clara y sin tecnicismos innecesarios.
  - Se detallan todos los atributos con explicaciones de por qué existen y cómo funcionan.
  - Se documentan las decisiones de diseño principales: orientación opuesta de jugadores, prioridad de la barra, bear-off dinámico, validación de puntos.
  - Se incluye un análisis completo del manejo de errores y excepciones en cada clase.
  - Se describe la estrategia de testing y cobertura de código.
  - Se explican las referencias a los principios SOLID aplicados en el proyecto.

---

**Referencias:**

- JUSTIFICACION.md

## [1.6.4] - 2025-10-29

### Added

- docs: Se añadió un diagrama UML completo y detallado de todas las clases del core (Player, Checker, Dice, Board, BackgammonGame, Move) en `plantaUML.mermaid`.
  - El diagrama incluye atributos, métodos principales y relaciones entre clases para facilitar la comprensión y el mantenimiento del diseño.

---

**Referencias:**

- plantaUML.mermaid

## [1.6.3] - 2025-10-29

### Added

- docs: Se añadieron docstrings completos y detallados a la clase `PygameUI` y a todos sus métodos en `backgammon/pygame_ui/ui.py`.
  - La documentación sigue el formato solicitado por el usuario, incluyendo secciones de atributos y métodos.
  - Mejora la claridad y mantenibilidad del código.

---

**Referencias:**

- backgammon/pygame_ui/ui.py

## [1.6.2] - 2025-10-28

### Changed

- UI: Se quitaron los números de columna (números de punta) que colisionaban visualmente con las fichas, evitando superposiciones y mejorando la legibilidad.
- UI: Se movió el indicador de los dados al centro de la barra central para mejorar su visibilidad y coherencia con el diseño del tablero.

---

**Referencias:**

- backgammon/pygame_ui/ui.py

## [1.6.1] - 2025-10-28

### Fixed

- fix(ui): Alinear las hit-boxes de las fichas en la barra con su representación visual.

  Se resolvió un problema por el cual el área clicable (hitbox) de las fichas ubicadas en la barra no coincidía con su nueva posición visual. Cambios clave:

  - Se ajustaron las posiciones verticales de dibujo de las fichas blancas y negras en la barra para que queden centradas en la mitad superior (blancas) y en la mitad inferior (negras) de la barra, respectivamente.
  - Este ajuste alinea la representación visual de las fichas con los rectángulos clicables subyacentes, de modo que las fichas sean seleccionables según lo previsto.
  - Se mantienen las mejoras de UI previas, como la visualización de una sola ficha con un contador cuando hay múltiples fichas en la barra.

---

**Referencias:**

- backgammon/pygame_ui/ui.py

## [1.6.0] - 2025-10-27

### Added

- UI: Nueva paleta de colores oscuros y suaves aplicada globalmente.

  Se ha implementado una nueva paleta de colores cálidos y suaves en todos los elementos del juego: tablero, triángulos, fichas, fondos y texto. El objetivo es conseguir una apariencia más acogedora y homogénea en todas las pantallas.

- UI: Rediseño del botón de bienvenida.

  Se ha rediseñado el botón de la pantalla de bienvenida con bordes redondeados y un sutil efecto de `hover` para una apariencia más moderna y accesible.

- UI: Aplicación consistente del nuevo estilo.

  El nuevo estilo se ha aplicado de manera consistente en la pantalla de bienvenida, la pantalla de tirada de dados y el tablero de juego principal.

---

**Referencias:**

- backgammon/pygame_ui/ui.py
- assets/styles.md (documentación de paleta y tokens de estilo)

## [1.5.0] 27/10/2025

### Added

- feat: Añade tirada de dados inicial para decidir el primer jugador

  Se ha implementado una tirada de dados al inicio de la partida para determinar qué jugador comienza.

  - Ambos jugadores lanzan dos dados.
  - El jugador con la suma más alta empieza.
  - En caso de empate, se vuelve a lanzar hasta desempatar.
  - Se muestra un mensaje en la barra central indicando quién empieza.
  - El mensaje desaparece con el primer movimiento del jugador.

---

## [1.4.0] 23/10/2025

### Refactor

- refactor(core, ui): Reevaluar dinámicamente los movimientos de bear-off

  Se ha refactorizado la lógica de gestión de turnos para que los movimientos legales se recalculen después de cada acción del jugador. Esto resuelve un problema en el que la lógica de bear-off, especialmente con dobles y movimientos de excepción, no se actualizaba correctamente.

  Cambios principales:
  - La UI ahora calcula los movimientos posibles para cada dado individualmente y sobre el estado actual del tablero.
  - Se ha eliminado el sistema de pre-cálculo de secuencias de movimientos (`enumerar_opciones_legales`), simplificando el código en `core/board.py`.
  - Se ha implementado la cesión automática del turno cuando no hay movimientos legales disponibles.

---

**Referencias:**

- [board](./backgammon/core/board.py)

- [player](./backgammon/core/player.py)

- [test_board](./tests/test_board.py)

## [1.3.1] 23/10/2025

### Added

- Se ha añadido un método `oponente_en_cuadrante` a la clase `Board` para detectar la presencia de fichas oponentes.
- Se ha actualizado el método `puede_bear_off` en la clase `Player` para usar esta nueva comprobación, bloqueando el bear-off si es necesario.
- Se ha añadido una nueva prueba unitaria (`test_puede_bear_off_con_oponente_en_cuadrante`) para verificar la nueva lógica.

---

**Referencias:**

- [board](./backgammon/core/board.py)

- [player](./backgammon/core/player.py)

- [test_board](./tests/test_board.py)

## [1.3.0] 23/10/2025

### Added

- Se ha añadido un estado de fin de juego en la clase `PygameUI` para detectar y gestionar la condición de victoria.
- Se ha creado un nuevo método, `_draw_game_over_screen`, que muestra un mensaje de victoria centrado sobre un fondo semitransparente.
- Se ha modificado el bucle principal del juego para mostrar la pantalla de victoria durante 5 segundos antes de cerrar la aplicación.
- Se ha añadido una nueva prueba unitaria (`test_game_over_detection`) para verificar que la lógica de detección de fin de juego funciona correctamente.

---

**Referencias:**

- [pygame_ui](./backgammon/pygame_ui/ui.py)

- [test_ui](./tests/test_ui.py)

## [1.2.0] 22/10/2025

### Added

- Ampliación de la ventana del juego a 1400x800 para crear más espacio y mejorar la presentación.
- Reposicionamiento de las zonas de "bear-off" a la derecha del tablero, evitando la superposición con los puntos del juego.
- Ajuste de las constantes de diseño y cálculos de la interfaz para adaptarse a la nueva resolución de la ventana.

### Fixed

- Corrección del orden de renderizado para que los indicadores de movimiento (círculos verdes) siempre se muestren por encima de las fichas.
- Actualización de la prueba unitaria de "bear-off" para reflejar la nueva ubicación de la zona de "bear-off".

---

**Referencias:**

- [pygame_ui](./backgammon/pygame_ui/ui.py)

- [test_ui](./tests/test_ui.py)

## [1.1.1] 21/10/2025

### Fixed

- Corrige el reingreso de fichas desde la barra en la UI de Pygame.
- Refactorización del método `_handle_click` en `backgammon/pygame_ui/ui.py` para gestionar correctamente la selección de la barra y el clic en un punto de destino válido.
- Corrección en el método `_attempt_move` para permitir la correcta aplicación del movimiento desde la barra.
- Añadida prueba unitaria en `tests/test_ui.py` para verificar la lógica de reingreso desde la barra, simulando clics y validando el estado del juego.
- Añadido el método `set_values` a la clase `Dice` para facilitar escenarios de prueba con valores de dados predecibles.
- Corrección de prueba existente en `tests/test_checker.py` para asegurar que todo el conjunto de pruebas pase.

## [1.1.0] 19/09/2025

### Added

- Implementación completa y funcional del CLI para 2 jugadores en `backgammon/cli/console.py`, con selección y visualización de movimientos legales, orientación de picos (1-24), y lógica de juego completa.
- Integración de todas las clases principales (`Player`, `Checker`, `Dice`, `Board`, `BackgammonGame`, `Move`) y solución de errores de importación y compatibilidad.
- Visualización de los números de los picos en el tablero para mejor orientación del jugador.
- Tests unitarios y de integración para todas las clases principales, asegurando cobertura total y cumplimiento de reglas de Backgammon.
- Lógica de movimientos legales en el CLI, incluyendo jugada forzada, dobles, barra, bear-off y restricciones de ocupación de puntos.
- Carpeta y clase `move.py` para representar movimientos y solucionar dependencias en el CLI.
- Documentación tipo NumPy para todas las clases y métodos principales, siguiendo el formato de copilot-instructions.md.
- Registro y actualización de todos los prompts y respuestas generadas en los archivos de la carpeta `prompts`.
- Reporte de cobertura de código en `coverage_report.txt`.

### Fixed

- Corrección de importaciones circulares y anotaciones de tipo entre módulos core.
- Corrección de visualización y orientación del tablero en CLI (puntas 1-24).
- Ajuste de la lógica de movimientos para cumplir con las reglas oficiales de Backgammon.
- Eliminación de errores en la generación y aplicación de movimientos, y en la visualización de opciones.

---

**Referencias:**  

- [backgammon](./backgammon/core/backgammon.py)

- [player](./backgammon/core/player.py)

- [dice](./backgammon/core/dice.py)

- [board](./backgammon/core/board.py)

- [move.py](./backgammon/core/move.py)

- [console](./backgammon/cli/console.py)

- [test_player](./tests/test_player.py)

- [test_checker](./tests/test_checker.py)

- [test_dice](./tests/test_dice.py)

- [test_board](./tests/test_board.py)

- [test_backgammon](./tests/test_backgammon.py)

- [test_move](./tests/test_move.py)

- [coverage](./coverage_report.txt)

- [prompts_desarrollo](./prompts/prompts-desarrollo.md)

- [prompts_documentacion](./prompts/prompts-documentacion.md)

- [prompts_testing](./prompts/prompts-testing.md)

# [1.0.0] 18/09/2025

### Added

- Implementación completa del CLI funcional para 2 jugadores en [console](./backgammon/cli/console.py) con selección de movimientos legales y visualización de opciones.
- Visualización de los números de los picos (puntas) en el tablero para mejor orientación del jugador.
- Integración para todas las clases principales, asegurando cobertura total y cumplimiento de reglas de Backgammon.
- Lógica de movimientos legales en el CLI, incluyendo jugada forzada, dobles, barra, bear-off y restricciones de ocupación de puntos.
- Actualización y registro de todos los prompts y respuestas generadas en los archivos de la carpeta `prompts`.
- Creación de la carpeta [move](./backgammon/core/move.py) para solución de error en [console](./backgammon/cli/console.py).

### Fixed

- Corrección de importaciones circulares y anotaciones de tipo entre módulos core.
- Corrección de visualización y orientación del tablero en CLI.
- Ajuste de la lógica de movimientos para cumplir con las reglas oficiales de Backgammon.

### Summary

La implementación es funcional y estable. A continuación, un resumen de lo implementado:

#### Métodos principales en `Board`

1. `jugador_tiene_en_barra(player)` – Verifica si un jugador tiene fichas en la barra.  
2. `jugador_todo_en_home(player)` – Verifica si todas las fichas de un jugador están en su home.  
3. `jugador_pip_count(player)` – Calcula el pip count (distancia total para sacar las fichas).  
4. `aplicar_movimiento(player, secuencia)` – Aplica una secuencia de movimientos al tablero.  
5. `enumerar_opciones_legales(player, dados)` – Genera todas las opciones de movimientos legales.  

#### Métodos auxiliares

6. `_generar_secuencias_movimiento()` – Genera recursivamente todas las secuencias de movimientos posibles.  
7. `_generar_movimientos_posibles()` – Genera movimientos posibles para un valor de dado.  
8. `_es_movimiento_valido()` – Valida si un movimiento es legal según las reglas.  
9. `_es_captura()` – Verifica si un movimiento captura una ficha del rival.  
10. `_calcular_hash_secuencia()` – Calcula un hash único para cada secuencia de movimientos.  
11. `_aplicar_paso_movimiento()` – Aplica un paso de movimiento al tablero.  

#### Características clave

- Cumplimiento de todas las reglas de Backgammon: movimientos regulares, capturas, entrada desde barra y bear-off.  
- Manejo de dobles: genera automáticamente 4 movimientos en caso de dados iguales.  
- Prioridad a la barra: se obliga a reingresar fichas antes de mover otras.  
- Validación de bear-off: solo permitido si todas las fichas están en home.  
- Generación completa de opciones: devuelve combinaciones de movimientos, no solo individuales.  
- Eliminación de duplicados en las secuencias de movimientos.  
- Sistema básico de puntuación que prioriza el uso de más dados.  

#### Resultados de pruebas

- ✅ Eliminado el `NotImplementedError`.  
- ✅ CLI funcional y corriendo correctamente.  
- ✅ Generación de movimientos funcionando para distintas combinaciones de dados.  
- ✅ Reglas implementadas y verificadas.  
- ✅ Correcto manejo de diferentes estados del tablero.  

---

## [0.7.0] 17/09/2025

### Added

- Se creó la clase [backgammon.py](./backgammon/core/backgammon.py) que integra y coordina las clases principales del juego (Player, Checker, Dice, Board).
- Se creó la clase [board.py](./backgammon/core/board.py).
- Documentación tipo NumPy para las clases `Player`, `Checker`, `Dice`, `Board` y `BackgammonGame`, siguiendo el formato de copilot-instructions.md.
- Tests completos con pytest para las clases [Player](./tests/test_player.py), [Checker](./tests/test_checker.py), [Dice](./tests/test_dice.py), [Board](./tests/test_board.py) y [BackgammonGame](./tests/test_backgammon.py), cubriendo el 100% de los métodos públicos y privados relevantes.

---

**Referencias:**  

- [backgammon](./backgammon/core/backgammon.py)

- [player](./backgammon/core/player.py)

- [player](./backgammon/core/player.py)  

- [dice](./backgammon/core/dice.py)

- [board](./backgammon/core/board.py)

- [test_player](./tests/test_player.py)

- [test_checker](./tests/test_checker.py)

- [test_dice](./tests/test_dice.py)

- [test_board](./tests/test_board.py)

- [test_backgammon](./tests/test_backgammon.py)

- [prompts_desarrollo](./prompts/prompts-desarrollo.md)  

- [prompts_documentacion](./prompts/prompts-documentacion.md)

- [prompts_testing](./prompts/prompts-testing.md)

## [0.6.0] 17/09/2025

### Added

- Creacion de [test_player.py](./tests/test_player.py) para la clase [player](./backgammon/core/player.py)
- Creacion del archivo [coverage_report.txt](./coverage_report.txt) para dejar registro del porcentaje de codigo cubierto

### Fixed

- Se resolvió el problema de importación circular entre `checker.py` y `player.py` usando `TYPE_CHECKING` para anotaciones de tipo.

### Changed

- Se mejoró la cobertura y claridad de la documentación y los tests para las clases principales del núcleo del juego.

---

**Referencias:**  

- [player](./backgammon/core/player.py)

- [checker](./backgammon/core/checker.py)

- [test_player](./tests/test_player.py)

## [0.5.0] 16/09/2025

### Added

- Creacion de clase [player](./backgammon/core/player.py)
- Actualizacion del [copilot-intructions](./.github/copilot-instructions.md)

## [0.4.0] 16/09/2025

### added

- Creacion de la logica de la clase [checker.py](./backgammon/core/checker.py)

- se añadio [REPORTS.md](./REPORTS.md)

- Se creo estructura completa de [core](./backgammon/core/) y [tests](./tests/)
- creacion de la carpeta [workflows](./.github/workflows/)

- creacion del archivo [ci.yml](./.github/workflows/ci.yml)

### Fixed

- Se realizo el debug y reescritura de [ci.yml](./.github/workflows/ci.yml)

- se corrigio errores de tests creando [conftest.py](./tests/conftest.py) y [pytest.ini](./pytest.ini)

## [0.3.0] 10-08-2025

### Added+

- logica basica de la clase [dice](./backgammon/core/dice.py)
- Documentacion de funciones de la clase [dice](./backgammon/core/dice.py)

## [0.2.0] 08-09/2025

### Added

- Creacion de logica basica de tablero
- Actualizacion de prompts a traves de [copilot-instructions](./.github/copilot-instructions.md)

## [0.1.0] 07-08-2025

### Added

- Creacion del esqueleto del proyecto
- Creacion de archivo [requeriments.txt](./requirements.txt)
