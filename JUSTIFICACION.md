# Justificación del Diseño - Backgammon

## Resumen del Diseño General

Este proyecto implementa el juego de Backgammon siguiendo una arquitectura modular y bien estructurada. La idea principal es separar la lógica del juego (core) de la interfaz de usuario, permitiendo que el código sea mantenible, testeable y fácil de entender.

Se creó:
- Una **lógica central** (`core`) que maneja todas las reglas del Backgammon
- Una **interfaz gráfica** (`pygame_ui`) para que los jugadores puedan jugar visualmente
- Una **interfaz de consola** (`cli`) para pruebas y desarrollo
- **Tests exhaustivos** para garantizar que todo funciona correctamente

---

## Justificación de las Clases Elegidas

### 1. Clase `Checker` - La Ficha Individual

**¿Por qué existe?**
Cada ficha del Backgammon necesita representarse como un objeto independiente. Aunque podrían guardarse solo como colores en listas, crear una clase `Checker` permite:
- Rastrear el estado de cada ficha (en tablero, barra, fuera)
- Facilitar futuras extensiones (por ejemplo, marcar fichas especiales)
- Mejorar la claridad del código

**Atributos principales:**
- `color` (str): El color de la ficha ('blanca' o 'negra')

**Métodos principales:**
- `get_color()`: Devuelve el color de la ficha para verificar a quién pertenece

**¿Por qué es simple?**
Mantuvimos esta clase simple porque las fichas no necesitan lógica compleja. El estado complejo (dónde está, si está en la barra, etc.) se gestiona en el `Board` y no en la ficha misma.

---

### 2. Clase `Dice` - Los Dados

**¿Por qué existe?**
Los dados son fundamentales en Backgammon. Esta clase encapsula toda la lógica relacionada con los dados:
- Tirar los dados y obtener valores aleatorios
- Manejar dobles (cuando ambos dados muestran el mismo número)
- Rastrear qué dados ya han sido usados en el turno

**Atributos principales:**
- `valores` (List[int]): Los valores actuales de los dos dados (1-6 cada uno)
- `usados` (List[bool]): Rastrea cuál dado ya se utilizó en este turno

**Métodos principales:**
- `tirar()`: Genera dos números aleatorios entre 1 y 6
- `usar_dado(valor)`: Marca un dado como utilizado después de hacer un movimiento
- `disponibles()`: Devuelve qué valores de dados aún pueden usarse
- `set_values(valores)`: Para testing, permite establecer valores específicos

**Manejo de errores:**
- Se valida que los valores estén entre 1 y 6
- Se previene usar el mismo dado dos veces en un movimiento

---

### 3. Clase `Checker` vs. `Player` - ¿Quién gestiona qué?

**Decisión importante:**
- `Checker` = Una ficha individual (simple, solo color)
- `Player` = El jugador (nombre, color, control de fichas, reglas personales)

Esto respeta el **Principio de Responsabilidad Única (S de SOLID)**:
- `Checker` solo sabe qué color es
- `Player` sabe cómo juega ese color (cuántas fichas tiene, si puede hacer bear-off, etc.)

---

### 4. Clase `Player` - El Jugador

**¿Por qué existe?**
Un jugador en Backgammon no es solo un color. Necesita:
- Saber cuántas fichas tiene
- Saber si tiene fichas en la barra (esperando reingresar)
- Saber si puede hacer bear-off (sacar fichas del tablero)
- Rastrear fichas que ya salieron del juego

**Atributos principales:**
- `nombre` (str): El nombre del jugador
- `color` (str): Su color ('blanca' o 'negra')
- `fichas` (List[Checker]): Sus 15 fichas
- `en_barra` (int): Cantidad de fichas esperando reingresar
- `fuera` (int): Cantidad de fichas que han salido del tablero

**Métodos principales:**
- `puede_bear_off(board)`: Verifica si todas sus fichas están en el home y puede sacarlas
- `fichas_en_juego()`: Cuenta cuántas fichas aún no han salido del juego
- `agregar_ficha_barra()` / `quitar_ficha_barra()`: Gestiona fichas capturadas

**Lógica especial:**
- Un jugador NO puede mover sus fichas si tiene fichas en la barra. Primero debe reingresar.
- El bear-off solo se permite si el jugador ha juntado todas sus fichas en el "home" (últimos 6 puntos para blancas, primeros 6 para negras).

---

### 5. Clase `Board` - El Tablero

**¿Por qué es la clase más compleja?**
El tablero es el "cerebro" del juego. Gestiona:
- La posición de todas las fichas
- Las reglas de movimiento legal
- Las capturas y el reinicio desde la barra
- El bear-off
- La validación de todos los movimientos

**Atributos principales:**
- `puntos` (List[List[Checker]]): Una lista de 24 puntos, cada uno con sus fichas
- `barra_blanca` y `barra_negra` (List[Checker]): Fichas esperando reingresar
- `fuera_blanca` y `fuera_negra` (List[Checker]): Fichas que completaron el recorrido

**Estructura del tablero:**
```
Para fichas BLANCAS (van de 1 a 24):
- Puntos 1-6: Home (donde comienzan)
- Puntos 7-18: Terreno del oponente (viaje largo)
- Puntos 19-24: Home del oponente (final del recorrido)

Para fichas NEGRAS (van de 24 a 1):
- Puntos 24-19: Home (donde comienzan)
- Puntos 18-7: Terreno del oponente
- Puntos 6-1: Home del oponente (final del recorrido)
```

**Métodos principales:**

1. **`jugador_tiene_en_barra(player)`**
   - Verifica si un jugador tiene fichas esperando reingresar
   - Es esencial porque los movimientos en barra tienen prioridad

2. **`jugador_todo_en_home(player)`**
   - Comprueba si todas las fichas del jugador están en su home
   - Condición necesaria para poder hacer bear-off

3. **`oponente_en_cuadrante(player)`**
   - Verifica si el oponente tiene fichas en el cuadrante de bear-off del jugador
   - Si es así, el bear-off está bloqueado

4. **`aplicar_movimiento(player, movimientos)`**
   - Ejecuta una secuencia completa de movimientos
   - Maneja capturas, reingresos desde barra y bear-off

5. **`enumerar_opciones_legales(player, dados)`**
   - Genera todas las combinaciones posibles de movimientos legales
   - Por ejemplo, si tienes (3,5), puedes mover 3 primero o 5 primero

---

### 6. Clase `Move` - Un Movimiento

**¿Por qué existe?**
Para representar un movimiento individual de forma clara:
- `origen`: De dónde sale la ficha (0 = barra, 1-24 = punto, 25 = fuera)
- `destino`: Hacia dónde va la ficha
- `valor_dado`: Qué valor del dado se usó

Esto facilita:
- Registrar movimientos
- Deshacer movimientos si es necesario
- Validar si un movimiento es legal

---

### 7. Clase `BackgammonGame` - El Coordinador

**¿Por qué existe?**
Alguien debe coordinar todo: los jugadores, el tablero, los dados. Esta clase:
- Inicializa una nueva partida
- Alterna turnos entre jugadores
- Aplica movimientos
- Detecta ganadores

**Métodos principales:**
- `iniciar_partida()`: Pone el tablero en su estado inicial
- `siguiente_turno()`: Cambia de jugador activo
- `aplicar_movimiento(movimientos)`: Ejecuta los movimientos del turno actual
- `obtener_ganador()`: Verifica si alguien ha ganado

---

## Justificación de Atributos

### En `Board`

**¿Por qué `puntos` es una lista de 24 elementos?**
- Backgammon tiene exactamente 24 puntos (triangles en inglés)
- Cada punto puede tener 0 o más fichas del mismo color
- Usar una lista permite acceso rápido por índice: `puntos[0]` es el punto 1

**¿Por qué separar barra y "fuera"?**
- Las fichas en la barra (capturadas) tienen reglas especiales: deben reingresar en puntos específicos
- Las fichas "fuera" (que completaron el recorrido) no pueden volver al juego
- Mantenerlas separadas evita confusiones

### En `Player`

**¿Por qué `en_barra` es un número y no una lista?**
- Las fichas en la barra son idénticas: solo importa la cantidad
- Usar un número es más eficiente que una lista de fichas
- Las fichas específicas (cuál es cuál) no importan, solo su cantidad

**¿Por qué `fichas` es una lista si todas son iguales?**
- Cada ficha es un objeto `Checker` (buena práctica OOP)
- Permite futuras extensiones (por ejemplo, marcar fichas)
- Facilita la integración con la UI que manipula fichas individuales

---

## Decisiones de Diseño Relevantes

### 1. Orientación Opuesta de Jugadores

**Decisión:**
- Fichas blancas avanzan de 1 → 24
- Fichas negras avanzan de 24 → 1

**Por qué:**
- Representa correctamente el juego real
- Añade complejidad pero es más realista
- La UI maneja la visualización correctamente

### 2. Prioridad de la Barra

**Decisión:**
- Si un jugador tiene fichas en la barra, DEBE reingresar antes de mover otras fichas

**Por qué:**
- Regla oficial del Backgammon
- Favorece el castigo por capturar fichas: "captura y espera"
- Se valida en `enumerar_opciones_legales`

### 3. Bear-off Dinámico

**Decisión:**
- No pre-calcular si el bear-off es legal al inicio del turno
- Recalcular después de cada movimiento

**Por qué:**
- El bear-off es complejo: tienes que tener TODAS las fichas en home, y el oponente no puede tener fichas en tu cuadrante
- Un movimiento puede cambiar estas condiciones
- Ejemplo: si mueves una ficha fuera del home, el bear-off se bloquea

### 4. Validación de Puntos

**Decisión:**
- Un punto con 3 o más fichas de un color es "propiedad" de ese jugador
- El oponente NO puede pasar por ese punto (solo si es el destino final)

**Por qué:**
- Regla oficial: bloques
- Añade estrategia: defender tus propios puntos

### 5. Generación de Opciones Legales

**Decisión:**
- Generar TODAS las combinaciones posibles (no solo movimientos individuales)
- Por ejemplo: dados (3,5) puede dar 2 opciones de secuencias

**Por qué:**
- Algunos movimientos solo son legales si se ejecutan en cierto orden
- La IA o jugador deben ver todas las posibilidades
- Favorece al jugador: "usa el máximo número de dados posible"

---

## Excepciones y Manejo de Errores

### 1. `ValueError` en `Dice`

**Cuándo se lanza:**
- Si intentas establecer valores fuera de 1-6
- Si intentas usar un dado que no existe

```python
if not (1 <= valor <= 6):
    raise ValueError(f"El valor del dado debe estar entre 1 y 6, recibido: {valor}")
```

**Por qué:**
- Los dados siempre tienen valores 1-6
- Detectar errores temprano evita bugs oscuros después

### 2. `IndexError` en `Board`

**Cuándo se lanza:**
- Si intentas acceder a un punto que no existe (< 0 o > 24)
- Se captura internamente y se retorna `False` para movimientos inválidos

**Manejo:**
```python
try:
    ficha = self.puntos[destino][0]
except (IndexError, ValueError):
    return False  # Movimiento inválido
```

### 3. `AttributeError` en `Player`

**Cuándo se lanza:**
- Si intentas jugar sin inicializar correctamente el jugador

**Prevención:**
- Validar en `__init__` que nombre y color sean válidos
- No permitir jugadores sin fichas

### 4. Manejo de Capturas

**Cuándo ocurre:**
- Si una ficha llega a un punto con solo 1 ficha del oponente

**Lógica:**
```python
if len(self.puntos[destino]) == 1 and self.puntos[destino][0].color != ficha.color:
    # Capturar la ficha del oponente
    ficha_capturada = self.puntos[destino][0]
    oponente.agregar_ficha_barra()
    self.puntos[destino] = [ficha]  # Solo la nueva ficha
else:
    # Agregar la ficha
    self.puntos[destino].append(ficha)
```

### 5. Prevención de Movimientos Inválidos

**Validaciones en `_es_movimiento_valido`:**
1. ¿Existe la ficha en el origen?
2. ¿Es del color del jugador?
3. ¿Es el destino válido (0-24)?
4. ¿El destino está ocupado por 2+ fichas del oponente? → Bloqueado
5. ¿Es bear-off? → Validar que todas las fichas estén en home
6. ¿Hay fichas en barra? → Deben reingresar primero

---

## Estrategias de Testing y Cobertura

### 1. Pruebas Unitarias por Clase

**Para `Dice`:**
- Verificar que `tirar()` devuelve valores 1-6
- Verificar que dobles se detectan correctamente
- Verificar que `set_values()` funciona para testing

**Para `Player`:**
- Verificar que puede_bear_off se bloquea correctamente
- Verificar que `fichas_en_juego()` cuenta correctamente
- Verificar que el reinicio desde barra funciona

**Para `Board`:**
- Verificar movimientos legales en diferentes estados
- Verificar capturas
- Verificar bear-off
- Verificar bloqueos (puntos con 3+ fichas)

**Para `BackgammonGame`:**
- Verificar que una partida completa se puede jugar
- Verificar que el ganador se detecta correctamente

### 2. Pruebas de Integración

- Una partida completa de 2 turnos
- Captura y reinicio desde barra
- Bear-off sin obstáculos
- Bear-off con obstáculos

### 3. Cobertura de Código

**Meta:** 100% de líneas de código probadas

**Herramienta:** pytest + coverage

**Archivos:**
- `tests/test_dice.py`
- `tests/test_player.py`
- `tests/test_checker.py`
- `tests/test_board.py`
- `tests/test_backgammon.py`

---

## Referencias a Requisitos SOLID

### S - Responsabilidad Única

**Ejemplo:**
- `Dice` SOLO maneja dados
- `Board` SOLO maneja el tablero y validaciones
- `Player` SOLO maneja el estado del jugador
- `BackgammonGame` SOLO coordina

Cada clase tiene una única razón para cambiar.

### O - Abierto/Cerrado

**Ejemplo:**
- Las reglas de Backgammon están centralizadas en `Board`
- Si cambian las reglas, solo modificamos `Board`, no la UI
- La UI puede extenderse sin cambiar el core

### L - Sustitución de Liskov

**Ejemplo:**
- Un `Checker` siempre funciona de la misma manera sin importar su color
- Se puede usar cualquier instancia de `Player` sin problemas

### I - Segregación de Interfaces

**Ejemplo:**
- `Player` no necesita conocer detalles internos de `Dice`
- `Dice` no necesita conocer cómo juega `Player`
- Cada clase usa solo lo que necesita

### D - Inversión de Dependencias

**Ejemplo:**
- `BackgammonGame` depende de interfaces (`Player`, `Board`, `Dice`), no de implementaciones
- Cambiar la implementación de `Board` no afecta a `BackgammonGame`

---

## Anexos: Diagramas UML

Ver archivo `plantaUML.mermaid` para el diagrama completo de clases.

**Relaciones principales:**
```
BackgammonGame -----> Board
    |
    +-----> Player (x2)
    +-----> Dice

Board -----> Checker (muchos)
    |
    +-----> Player (referencia)

Player -----> Checker (15 fichas)
```

---

## Conclusión

El diseño de este proyecto equilibra:
- **Claridad:** Código fácil de entender
- **Mantenibilidad:** Fácil de modificar y extender
- **Corrección:** Las reglas de Backgammon se implementan fielmente
- **Testabilidad:** Cada componente se puede probar independientemente

Cada decisión fue tomada considerando estos principios, resultando en un codebase robusto y profesional.
