import pygame
import sys
import time
import random
from backgammon.core.backgammon import BackgammonGame
from backgammon.core.player import (
    PasoMovimiento,
    SecuenciaMovimiento,
)  # pylint: disable=unused-import

# Constants
WIDTH, HEIGHT = 1400, 800

# --- Nueva Paleta de Colores ---
# --- Nueva Paleta de Colores (Dark Edition) ---

COLOR_FONDO_TABLERO = (40, 40, 45)  # Gris grafito oscuro (fondo principal)
COLOR_TRIANGULO_CLARO = (175, 155, 135)  # Beige apagado
COLOR_TRIANGULO_OSCURO = (92, 64, 51)  # Marrón chocolate profundo

COLOR_FONDO_MESA = (32, 32, 35)  # Gris muy oscuro (background interno)
COLOR_BEAR_OFF_BAR = (110, 85, 60)  # Madera tostada (zona de borneado)

COLOR_PIEZA_NEGRA = (15, 15, 15)  # Negro mate
COLOR_PIEZA_BLANCA = (245, 240, 230)  # Marfil cálido (evita blanco chillón)

COLOR_BORDE_BLANCA = (200, 200, 200)  # Borde gris claro para fichas blancas
COLOR_BORDE_NEGRA = (50, 50, 50)  # Borde gris oscuro para fichas negras
COLOR_TEXTO_NEGRO = (230, 230, 230)  # Gris claro para texto sobre fondo oscuro
COLOR_TEXTO_BLANCO = (250, 244, 227)  # Blanco cálido para contraste

COLOR_HIGHLIGHT = (0, 155, 130)  # Verde azulado profundo (destaca sin molestar)
COLOR_BOTON_HOVER = (119, 97, 82)  # Marrón suave (hover amigable)


# --- Colores Antiguos (se mantendrán si son necesarios para elementos no temáticos) ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BOARD_COLOR = COLOR_FONDO_TABLERO
GREEN = (0, 255, 0)


# Game States
SELECCION_COLOR = "SELECCION_COLOR"
TIRADA_INICIAL = "TIRADA_INICIAL"
JUEGO = "JUEGO"


class PygameUI:
    """
    A class to handle the Pygame user interface for the Backgammon game.

    This class is responsible for initializing Pygame, drawing the game board,
    handling user input, and managing the overall game flow from the UI perspective.

    Attributes
    ----------
    screen : pygame.Surface
        The main screen surface for drawing.
    font : pygame.font.Font
        The default font for rendering text.
    large_font : pygame.font.Font
        A larger font for titles and important messages.
    clock : pygame.time.Clock
        Pygame clock for controlling the frame rate.
    estado_juego : str
        The current state of the game (e.g., SELECCION_COLOR, TIRADA_INICIAL, JUEGO).
    dados_iniciales : dict
        Stores the results of the initial dice roll for each color.
    ganador_tirada_inicial : str or None
        The color of the player who won the initial roll, or 'empate'.
    tiempo_inicio_tirada : float or None
        Timestamp of when the initial roll animation started.
    boton_empezar_rect : pygame.Rect or None
        The rectangle for the 'Empezar' button.
    juego_iniciado : bool
        Flag to indicate if the main game loop has started.
    game_over : bool
        Flag to indicate if the game has ended.
    winner : Player or None
        The winning player object.
    game_over_time : float or None
        Timestamp of when the game ended.
    board_edge : int
        The width of the board's outer edge.
    point_height : int
        The height of the triangular points.
    point_width : int
        The width of the triangular points.
    bar_width : int
        The width of the central bar.
    checker_radius : int
        The radius of the checkers.
    selected_point : int or None
        The index of the currently selected point (0-23).
    point_rects : list[pygame.Rect]
        A list of 24 rectangles for each point on the board.
    bar_rects : dict
        A dictionary mapping player colors to their bar rectangles.
    bear_off_rects : dict
        A dictionary mapping player colors to their bear-off area rectangles.
    used_dice : list
        A list of dice values that have been used in the current turn.
    possible_moves : list
        (Currently unused) A list to store possible moves.
    possible_dests : list
        A list of possible destination indices for the selected checker.
    selected_source : int or str or None
        The selected source for a move, can be a point index (0-23) or 'bar'.
    game : BackgammonGame
        An instance of the core BackgammonGame logic.

    Methods
    -------
    run()
        Starts and manages the main game loop.
    _setup_game()
        Initializes players and the core game logic.
    _calculate_point_rects()
        Calculates the screen positions for all 24 points.
    _calculate_bar_rects()
        Calculates the screen positions for the central bar areas.
    _calculate_bear_off_rects()
        Calculates the screen positions for the bear-off areas.
    _draw_board()
        Draws the static elements of the game board.
    _draw_checkers()
        Draws the checkers on the points, bar, and bear-off areas.
    _draw_game_info()
        Displays the current player's turn and dice roll.
    _draw_game_over_screen()
        Displays the winner when the game ends.
    _handle_click(pos)
        Handles user mouse clicks to select and move checkers.
    _get_point_from_pos(pos)
        Converts mouse coordinates to a point index.
    _get_bear_off_from_pos(pos)
        Checks if a click is within the current player's bear-off area.
    _is_valid_source(point_idx)
        Checks if a selected point is a valid source for a move.
    _get_possible_dests(source)
        Determines possible destinations for a checker from a given source.
    _attempt_move(source, destination)
        Validates and applies a player's move.
    _end_turn()
        Ends the current player's turn and starts the next.
    _get_current_dice()
        Gets the full list of dice values for the turn.
    _get_available_dice()
        Gets the list of unused dice values for the turn.
    _has_any_legal_moves()
        Checks if the current player has any possible legal moves.
    _draw_pantalla_seleccion_color()
        Draws the initial screen to start the game.
    _handle_eventos_seleccion_color(event)
        Handles input on the color selection screen.
    _draw_pantalla_tirada_inicial()
        Draws the screen for the initial dice roll.
    _manejar_logica_tirada_inicial()
        Manages the logic for the initial dice roll to decide who goes first.
    _draw_boton_redondeado(...)
        A helper function to draw rounded buttons.
    """

    def __init__(self):
        """
        Initializes the Pygame UI.

        Sets up the Pygame window, fonts, clock, and initializes all
        game state variables and UI layout parameters.
        """
        pygame.init()  # pylint: disable=no-member
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Backgammon")
        self.font = pygame.font.Font(None, 24)
        self.large_font = pygame.font.Font(None, 74)
        self.clock = pygame.time.Clock()

        # Game state
        self.estado_juego = SELECCION_COLOR
        self.dados_iniciales = {"blancas": 0, "negras": 0}
        self.ganador_tirada_inicial = None
        self.tiempo_inicio_tirada = None
        self.boton_empezar_rect = None
        self.juego_iniciado = False

        self.game_over = False
        self.winner = None
        self.game_over_time = None

        # Dynamic board layout constants
        self.board_edge = int(WIDTH * 0.02)
        self.point_height = int(HEIGHT * 0.4)

        # Define a specific width for the main board area, leaving space for bear-off etc.
        main_board_width_ratio = 0.85  # Let's say the main board takes 85% of the width
        playing_width = int(WIDTH * main_board_width_ratio) - (2 * self.board_edge)

        # We have 12 points and 1 bar. Bar is ~1.5x a point.
        # Total units = 12 + 1.5 = 13.5
        unit_width = playing_width / 13.5
        self.point_width = int(unit_width)
        self.bar_width = int(unit_width * 1.5)

        self.checker_radius = int(self.point_width * 0.4)
        self.selected_point = None
        self.point_rects = [None] * 24
        self.bar_rects = {}
        self.bear_off_rects = {}
        self._calculate_point_rects()
        self._calculate_bar_rects()
        self._calculate_bear_off_rects()
        self.used_dice = []
        self.possible_moves = []
        self.possible_dests = []
        self.selected_source = None  # Can be point index or 'bar'

        self.game = BackgammonGame()
        # self._setup_game() will be called after the initial screens

    def _calculate_bar_rects(self):
        """
        Calculates the clickable rects for each player's bar.

        This method defines the screen areas for the white and black sections of
        the central bar, used for checkers that have been hit.
        """
        bar_x = self.board_edge + 6 * self.point_width
        # The top half of the bar is for white's checkers
        self.bar_rects["blancas"] = pygame.Rect(bar_x, 0, self.bar_width, HEIGHT / 2)
        # The bottom half of the bar is for black's checkers
        self.bar_rects["negras"] = pygame.Rect(bar_x, HEIGHT / 2, self.bar_width, HEIGHT / 2)

    def _calculate_bear_off_rects(self):
        """
        Calculates the clickable rects for each player's bear-off area.

        This defines the dedicated areas on the side of the board where players
        will move their checkers to bear them off.
        """
        # This area is now to the right of the main board
        bear_off_x = self.board_edge + (12 * self.point_width) + self.bar_width + self.board_edge
        bear_off_width = WIDTH - bear_off_x - self.board_edge

        # White's bear-off is top-right
        self.bear_off_rects["blancas"] = pygame.Rect(
            bear_off_x, self.board_edge, bear_off_width, self.point_height
        )

        # Black's bear-off is bottom-right
        self.bear_off_rects["negras"] = pygame.Rect(
            bear_off_x,
            HEIGHT - self.board_edge - self.point_height,
            bear_off_width,
            self.point_height,
        )

    def _setup_game(self):
        """
        Sets up the players and starts the game.

        Initializes the `BackgammonGame` instance with two players, 'Blanco' and
        'Negro', setting their respective colors, directions, and home points.
        It then starts the game logic.
        """
        player_configs = [
            {
                "id": "P1",
                "nombre": "Blanco",
                "color": "blancas",
                "direccion": 1,
                "home_points": range(18, 24),
                "entry_point": -1,
            },
            {
                "id": "P2",
                "nombre": "Negro",
                "color": "negras",
                "direccion": -1,
                "home_points": range(0, 6),
                "entry_point": 24,
            },
        ]
        self.game.setup_players(player_configs)
        self.game.start_game(primer_jugador_color=self.ganador_tirada_inicial)
        # La tirada de dados y la configuración del turno se harán en el bucle principal del juego
        self.game.roll_dice()

    def _calculate_point_rects(self):
        """
        Calculates the clickable rects for each point and stores them.

        This method iterates through the 12 columns of the board and calculates
        the rectangular area for both the top and bottom points, storing them
        in `self.point_rects` for later use in drawing and click detection.
        """
        # i is the visual column from left to right
        for i in range(12):
            # Bottom row
            point_x_bottom = self.board_edge + i * self.point_width
            if i >= 6:
                point_x_bottom += self.bar_width

            # The core indices for the bottom row run from 11 (left) to 0 (right)
            core_idx_bottom = 11 - i
            self.point_rects[core_idx_bottom] = pygame.Rect(
                point_x_bottom,
                HEIGHT - self.board_edge - self.point_height,
                self.point_width,
                self.point_height,
            )

            # Top row
            point_x_top = self.board_edge + i * self.point_width
            if i >= 6:
                point_x_top += self.bar_width

            # The core indices for the top row run from 12 (left) to 23 (right)
            core_idx_top = 12 + i
            self.point_rects[core_idx_top] = pygame.Rect(
                point_x_top, self.board_edge, self.point_width, self.point_height
            )

    def _draw_checkers(self):
        """
        Draws the checkers on the board based on the game state.

        This function renders all checkers on their respective points, on the bar,
        and displays the count of borne-off checkers. It also handles highlighting
        for selected checkers and their possible destinations.
        """
        checker_colors = {"blancas": COLOR_PIEZA_BLANCA, "negras": COLOR_PIEZA_NEGRA}

        # Highlight selected source
        if self.selected_source is not None:
            if self.selected_source == "bar":
                player_color = self.game.get_current_player().get_color()
                rect = self.bar_rects[player_color]
            else:
                rect = self.point_rects[self.selected_source]
            pygame.draw.rect(self.screen, COLOR_HIGHLIGHT, rect, 4)

        # Draw checkers on points first
        for point_idx, checkers in enumerate(self.game.board.points):
            if not checkers:
                continue

            rect = self.point_rects[point_idx]
            player_color = checkers[0].get_color()
            checker_color = checker_colors[player_color]
            is_top_row = point_idx >= 12
            direction = 1 if is_top_row else -1
            base_y = (
                rect.top + self.checker_radius if is_top_row else rect.bottom - self.checker_radius
            )

            # Draw up to 4 checkers
            num_to_draw = min(len(checkers), 5)
            for i in range(num_to_draw):
                center_x = rect.centerx
                center_y = base_y + (i * 2 * self.checker_radius * direction)
                border_color = (
                    COLOR_BORDE_BLANCA if player_color == "blancas" else COLOR_BORDE_NEGRA
                )
                pygame.draw.circle(
                    self.screen,
                    checker_color,
                    (center_x, center_y),
                    self.checker_radius,
                )
                pygame.draw.circle(
                    self.screen,
                    border_color,
                    (center_x, center_y),
                    self.checker_radius,
                    2,
                )

            # If there are more than 5 checkers, display the count on the last visible checker
            if len(checkers) > 5:
                text_color = COLOR_PIEZA_NEGRA if player_color == "blancas" else COLOR_PIEZA_BLANCA
                count_text = self.font.render(str(len(checkers)), True, text_color)
                # Position the count on the 5th checker's position (index 4)
                count_y = base_y + (4 * 2 * self.checker_radius * direction)
                text_rect = count_text.get_rect(center=(rect.centerx, count_y))
                self.screen.blit(count_text, text_rect)

        # Draw checkers on the bar
        bar_x = self.board_edge + 6 * self.point_width + self.bar_width / 2

        # Define fixed Y positions for bar checkers to align with hitboxes
        y_pos_blancas = HEIGHT * 0.25  # Center of the top half
        y_pos_negras = HEIGHT * 0.75  # Center of the bottom half

        positions = {"blancas": y_pos_blancas, "negras": y_pos_negras}

        for color_name, checkers in self.game.board.bar.items():
            if not checkers:
                continue

            color = checker_colors[color_name]
            center_y = positions[color_name]

            # Draw a single checker representing the stack on the bar
            border_color = COLOR_BORDE_BLANCA if color_name == "blancas" else COLOR_BORDE_NEGRA
            pygame.draw.circle(self.screen, color, (bar_x, center_y), self.checker_radius)
            pygame.draw.circle(self.screen, border_color, (bar_x, center_y), self.checker_radius, 2)

            # If there's more than one, draw the count
            if len(checkers) > 1:
                text_color = COLOR_PIEZA_NEGRA if color_name == "blancas" else COLOR_PIEZA_BLANCA
                count_text = self.font.render(str(len(checkers)), True, text_color)
                text_rect = count_text.get_rect(center=(bar_x, center_y))
                self.screen.blit(count_text, text_rect)

        # Draw borne-off checkers count inside the bear-off areas
        white_borne_off = len(self.game.board.get_borne_off("blancas"))
        if white_borne_off > 0:
            white_rect = self.bear_off_rects["blancas"]
            white_text = self.font.render(f"Off: {white_borne_off}", True, COLOR_TEXTO_NEGRO)
            self.screen.blit(
                white_text,
                (
                    white_rect.centerx - white_text.get_width() / 2,
                    white_rect.centery - white_text.get_height() / 2,
                ),
            )

        black_borne_off = len(self.game.board.get_borne_off("negras"))
        if black_borne_off > 0:
            black_rect = self.bear_off_rects["negras"]
            black_text = self.font.render(f"Off: {black_borne_off}", True, COLOR_TEXTO_BLANCO)
            self.screen.blit(
                black_text,
                (
                    black_rect.centerx - black_text.get_width() / 2,
                    black_rect.centery - black_text.get_height() / 2,
                ),
            )

        # Now, draw the highlights on top of everything
        for dest in self.possible_dests:
            if dest == "bear_off":
                player_color = self.game.get_current_player().get_color()
                rect = self.bear_off_rects[player_color]
                pygame.draw.rect(self.screen, COLOR_HIGHLIGHT, rect, 4)
            else:
                rect = self.point_rects[dest]
                pygame.draw.circle(
                    self.screen, COLOR_HIGHLIGHT, rect.center, self.checker_radius * 0.3
                )

    def _draw_game_over_screen(self):
        """
        Draws the game over screen.

        This method displays a semi-transparent overlay and a message indicating
        which player has won the game.
        """
        # Create a semi-transparent overlay
        overlay = pygame.Surface(
            (WIDTH, HEIGHT), pygame.SRCALPHA  # pylint: disable=no-member
        )  # pylint: disable=no-member
        overlay.fill((0, 0, 0, 180))  # Black with alpha
        self.screen.blit(overlay, (0, 0))

        # Display winner message
        winner_text = f"¡Gana el jugador {self.winner.get_nombre()}!"
        text_surface = self.large_font.render(winner_text, True, COLOR_TEXTO_BLANCO)
        text_rect = text_surface.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        self.screen.blit(text_surface, text_rect)

    def _draw_game_info(self):
        """
        Displays the current player and dice roll within the central bar.

        Renders the name of the current player and the values of their dice roll
        in the middle of the board for clear visibility.
        """
        player = self.game.get_current_player()
        dice = self.game.dice.get_values()

        # Define the central bar area for text
        bar_center_x = self.board_edge + 6 * self.point_width + self.bar_width / 2
        bar_top = HEIGHT / 2 - 100  # Example vertical positioning
        bar_bottom = HEIGHT / 2 + 100

        # Player's turn text
        player_color_name = player.get_color().capitalize()
        turn_font = pygame.font.Font(None, 36)
        player_surface = turn_font.render(player_color_name, True, COLOR_TEXTO_BLANCO)
        player_rect = player_surface.get_rect(center=(bar_center_x, bar_top + 50))
        self.screen.blit(player_surface, player_rect)

        # Dice roll text
        dice_text = f"{dice[0]} - {dice[1]}" if dice else "..."
        dice_font = pygame.font.Font(None, 48)
        dice_surface = dice_font.render(dice_text, True, COLOR_TEXTO_BLANCO)
        dice_rect = dice_surface.get_rect(center=(bar_center_x, bar_bottom - 50))
        self.screen.blit(dice_surface, dice_rect)

    def _draw_board(self):
        """
        Draws the static elements of the backgammon board.

        This method handles rendering the board's background, the central bar,
        the bear-off areas, and the triangular points using pre-calculated
        rectangles and color constants.
        """
        # Dibuja el fondo de la mesa y el marco del tablero
        self.screen.fill(COLOR_FONDO_MESA)
        pygame.draw.rect(
            self.screen, COLOR_FONDO_TABLERO, (0, 0, WIDTH, HEIGHT), self.board_edge * 2
        )

        # Dibuja la barra central
        bar_x = self.board_edge + 6 * self.point_width
        pygame.draw.rect(self.screen, COLOR_FONDO_TABLERO, (bar_x, 0, self.bar_width, HEIGHT))

        # Dibuja las áreas de bear-off
        for (
            color,
            rect,
        ) in self.bear_off_rects.items():  # pylint: disable=unused-variable
            pygame.draw.rect(self.screen, COLOR_BEAR_OFF_BAR, rect)
            # Simular textura de madera o fieltro con líneas
            for i in range(0, rect.width, 5):
                line_color = (
                    *COLOR_TRIANGULO_OSCURO,
                    50,
                )  # Añadir canal alfa para transparencia
                start_pos = (rect.left + i, rect.top)
                end_pos = (rect.left + i, rect.bottom)
                pygame.draw.line(self.screen, line_color, start_pos, end_pos, 1)
            pygame.draw.rect(
                self.screen, COLOR_TRIANGULO_CLARO, rect, 3
            )  # Borde más grueso y claro

        # Colores de los triángulos
        color1 = COLOR_TRIANGULO_CLARO
        color2 = COLOR_TRIANGULO_OSCURO

        # Dibuja los triángulos
        for i, rect in enumerate(self.point_rects):
            if rect is None:
                continue

            # Determine color based on visual column
            if i >= 12:
                vis_i = i - 12
            else:
                vis_i = 11 - i
            point_color = (
                color1 if vis_i % 2 != 0 else color2
            )  # Flipped this to match original look

            # Draw triangle
            triangle_margin = 2
            if i >= 12:  # Top row points down
                pygame.draw.polygon(
                    self.screen,
                    point_color,
                    [
                        (rect.left, rect.top + triangle_margin),
                        (rect.right, rect.top + triangle_margin),
                        rect.midbottom,
                    ],
                )
            else:  # Bottom row points up
                pygame.draw.polygon(
                    self.screen,
                    point_color,
                    [
                        (rect.left, rect.bottom - triangle_margin),
                        (rect.right, rect.bottom - triangle_margin),
                        rect.midtop,
                    ],
                )

    def _get_point_from_pos(self, pos):
        """
        Converts mouse coordinates to a board point index (0-23).

        Parameters
        ----------
        pos : tuple(int, int)
            The (x, y) coordinates of the mouse click.

        Returns
        -------
        int or None
            The index of the clicked point (0-23), or None if the click
            was not on any point.
        """
        for i, rect in enumerate(self.point_rects):
            if rect and rect.collidepoint(pos):
                return i
        return None

    def _get_bear_off_from_pos(self, pos):
        """
        Checks if the mouse click is on a valid bear-off area.

        Parameters
        ----------
        pos : tuple(int, int)
            The (x, y) coordinates of the mouse click.

        Returns
        -------
        str or None
            Returns 'bear_off' if the click is within the current player's
            bear-off area, otherwise returns None.
        """
        player = self.game.get_current_player()
        if self.bear_off_rects[player.get_color()].collidepoint(pos):
            return "bear_off"
        return None

    def _get_possible_dests(self, source):
        """
        Calculates possible destinations for a checker from a given source.

        Based on the available (unused) dice, this method queries the core game
        logic to find all legal moves for a checker at the specified source point
        or on the bar.

        Parameters
        ----------
        source : int or str
            The starting point of the checker, either an index (0-23) or 'bar'.

        Returns
        -------
        list
            A list of possible destinations, where each destination is either a
            point index (0-23) or the string 'bear_off'.
        """
        dests = []
        start_point = None if source == "bar" else source
        player = self.game.get_current_player()
        available_dice = self._get_available_dice()

        # We need to check moves for each unique die value
        for die_value in set(available_dice):
            # Generate moves for the current board state and one die
            # Note: _generar_movimientos_posibles returns PasoMovimiento, not OpcionMovimiento
            possible_steps = self.game.board._generar_movimientos_posibles(
                player, die_value, self.game.board
            )
            for paso in possible_steps:
                if paso.desde == start_point:
                    if paso.hasta is None:
                        dests.append("bear_off")
                    else:
                        dests.append(paso.hasta)
        return list(set(dests))

    def _attempt_move(self, source, destination):
        """
        Finds a valid move, applies it, and updates the game state.

        This method identifies which available die allows the specified move from
        source to destination. It then applies this single move to the game board,
        marks the die as used, and checks if the turn should end.

        Parameters
        ----------
        source : int or str
            The starting point of the checker (0-23 or 'bar').
        destination : int or str
            The target point for the checker (0-23 or 'bear_off').
        """
        player = self.game.get_current_player()
        start_idx = None if source == "bar" else source
        dest_idx = None if destination == "bear_off" else destination
        available_dice = self._get_available_dice()

        # Find which die can make this move
        move_to_apply = None
        used_die = None

        for die_value in sorted(
            list(set(available_dice)), reverse=True
        ):  # Prefer larger dice for ambiguity
            possible_steps = self.game.board._generar_movimientos_posibles(
                player, die_value, self.game.board
            )
            for paso in possible_steps:
                if paso.desde == start_idx and paso.hasta == dest_idx:
                    move_to_apply = paso
                    used_die = die_value
                    break
            if move_to_apply:
                break

        if not move_to_apply:
            print(
                f"ERROR: No valid die found for move from {source} to {destination}. This should not happen."
            )
            self.selected_source = None
            self.possible_dests = []
            return

        # Apply the single move
        self.game.board.aplicar_movimiento(player, [move_to_apply])
        self.used_dice.append(used_die)

        # Reset UI state for the next action in the turn
        self.selected_source = None
        self.possible_dests = []

        # After the move, check if the turn should end
        if not self._get_available_dice() or not self._has_any_legal_moves():
            self._end_turn()

    def _get_current_dice(self):
        """
        Returns the full list of dice for the current turn, handling doubles.

        Returns
        -------
        list
            A list of integers representing the dice values for the current turn.
            If doubles are rolled (e.g., two 5s), it returns four instances of
            that value (e.g., [5, 5, 5, 5]).
        """
        dice = list(self.game.dice.get_values())
        if not dice:
            return []
        if len(dice) == 2 and dice[0] == dice[1]:
            # If some doubles have been used, return the correct remaining number
            return [dice[0]] * 4
        return dice

    def _get_available_dice(self):
        """
        Returns the dice that have not yet been used this turn.

        This method filters the full list of dice for the turn, removing the
        values that have already been used to make moves.

        Returns
        -------
        list
            A list of integers representing the unused dice values.
        """
        available = self._get_current_dice()
        for die in self.used_dice:
            if die in available:
                available.remove(die)
        return available

    def _has_any_legal_moves(self):
        """
        Checks if there are any legal moves for any of the available dice.

        This function iterates through the unique available dice values and checks
        if the current player can make any valid move. This is crucial for
        determining if a player's turn should be skipped automatically.

        Returns
        -------
        bool
            True if at least one legal move exists, False otherwise.
        """
        player = self.game.get_current_player()
        available_dice = self._get_available_dice()
        # Test each unique die value. If any of them yield a move, return True.
        for die_value in set(available_dice):
            if self.game.board._generar_movimientos_posibles(player, die_value, self.game.board):
                return True
        return False

    def _end_turn(self):
        """
        Finalizes the current turn and sets up the next one.

        This method checks for a game over condition. If the game is not over,
        it advances to the next player, rolls the dice for them, and resets
        the UI state for the new turn. It also handles automatically skipping
        the turn if the new player has no legal moves.
        """
        print("--- Turno finalizado ---")

        if self.game.is_game_over():
            self.game_over = True
            self.winner = self.game.get_current_player()
            self.game_over_time = time.time()
            return

        self.game.next_turn()
        self.game.roll_dice()
        self.used_dice = []
        self.selected_source = None
        self.possible_dests = []
        print(
            f"Nuevo turno para {self.game.get_current_player().get_nombre()} con dados {self.game.dice.get_values()}"
        )

        # At the start of the new turn, immediately check if there are any moves.
        # If not, end the turn right away.
        if not self._has_any_legal_moves():
            print("No hay movimientos legales. Pasando el turno automáticamente.")
            # Give a brief moment for the user to see the dice roll before skipping.
            self._draw_board()
            self._draw_checkers()
            self._draw_game_info()
            pygame.display.flip()
            pygame.time.wait(1500)  # Wait 1.5 seconds
            self._end_turn()

    def _handle_click(self, pos):
        """
        Handles a mouse click, re-evaluating moves dynamically.

        This is the main input handler during the game. It processes a click to:
        - Select a checker as a source for a move.
        - Deselect the current checker.
        - Select a different checker.
        - Attempt to move the selected checker to a valid destination.

        Parameters
        ----------
        pos : tuple(int, int)
            The (x, y) coordinates of the mouse click.
        """
        player = self.game.get_current_player()
        clicked_point = self._get_point_from_pos(pos)
        clicked_bear_off = self._get_bear_off_from_pos(pos)
        clicked_destination = clicked_point if clicked_point is not None else clicked_bear_off

        # If a source is selected, a click can mean one of three things:
        if self.selected_source is not None:
            # 1. Click on a valid destination: attempt the move
            if clicked_destination in self.possible_dests:
                self._attempt_move(self.selected_source, clicked_destination)
                return
            # 2. Click on the same source: deselect
            elif clicked_point == self.selected_source:
                self.selected_source = None
                self.possible_dests = []
                return
            # 3. Click on another valid source: switch selection
            elif clicked_point is not None and self._is_valid_source(clicked_point):
                self.selected_source = clicked_point
                self.possible_dests = self._get_possible_dests(self.selected_source)
                return
            # 4. Click anywhere else: deselect
            else:
                self.selected_source = None
                self.possible_dests = []
                return

        # If no source is selected, a click can mean:
        # 1. Click on the bar (if checkers are present): select the bar as source
        if self.game.board.jugador_tiene_en_barra(player):
            if self.bar_rects[player.get_color()].collidepoint(pos):
                self.selected_source = "bar"
                self.possible_dests = self._get_possible_dests(self.selected_source)
        # 2. Click on a point with the player's checkers: select the point as source
        elif clicked_point is not None and self._is_valid_source(clicked_point):
            self.selected_source = clicked_point
            self.possible_dests = self._get_possible_dests(self.selected_source)

    def _is_valid_source(self, point_idx):
        """
        Check if a point is a valid source for a move.

        A point is a valid source if:
        1. It contains checkers belonging to the current player.
        2. There is at least one possible move from that point with the
           available dice.

        Parameters
        ----------
        point_idx : int
            The index of the point to check (0-23).

        Returns
        -------
        bool
            True if the point is a valid source, False otherwise.
        """
        player = self.game.get_current_player()
        # Must have checkers of the player's color
        if (
            not self.game.board.points[point_idx]
            or self.game.board.points[point_idx][0].get_color() != player.get_color()
        ):
            return False
        # Must have at least one possible destination
        if not self._get_possible_dests(point_idx):
            return False
        return True

    def _draw_boton_redondeado(self, text, rect, text_color, bg_color, hover_color, radius=20):
        """
        Draws a rounded button with text and hover effect.

        A helper function to create visually appealing rounded buttons that
        change color when the mouse pointer is over them.

        Parameters
        ----------
        text : str
            The text to display on the button.
        rect : pygame.Rect
            The rectangular area for the button.
        text_color : tuple(int, int, int)
            The color of the button's text.
        bg_color : tuple(int, int, int)
            The background color of the button.
        hover_color : tuple(int, int, int)
            The background color when the mouse hovers over the button.
        radius : int, optional
            The border radius for the rounded corners (default is 20).
        """
        mouse_pos = pygame.mouse.get_pos()
        is_hovered = rect.collidepoint(mouse_pos)

        color_actual = hover_color if is_hovered else bg_color

        # Dibuja el rectángulo redondeado
        pygame.draw.rect(self.screen, color_actual, rect, border_radius=radius)

        # Dibuja el texto
        text_surface = self.large_font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=rect.center)
        self.screen.blit(text_surface, text_rect)

    def _draw_pantalla_seleccion_color(self):
        """
        Draws the initial welcome screen.

        This screen displays the game title and an 'Empezar' (Start) button
        to begin the game.
        """
        self.screen.fill(COLOR_FONDO_MESA)
        titulo_surface = self.large_font.render(
            "Bienvenido/a a Backgammon", True, COLOR_TEXTO_NEGRO
        )
        titulo_rect = titulo_surface.get_rect(center=(WIDTH / 2, HEIGHT / 3))
        self.screen.blit(titulo_surface, titulo_rect)

        # Botón Empezar
        empezar_text = "Empezar"
        empezar_surface = self.large_font.render(empezar_text, True, COLOR_TEXTO_BLANCO)
        empezar_rect_inflated = empezar_surface.get_rect(center=(WIDTH / 2, HEIGHT / 2)).inflate(
            40, 20
        )
        self.boton_empezar_rect = empezar_rect_inflated

        self._draw_boton_redondeado(
            empezar_text,
            self.boton_empezar_rect,
            COLOR_TEXTO_BLANCO,
            COLOR_FONDO_TABLERO,
            COLOR_BOTON_HOVER,
        )

    def _handle_eventos_seleccion_color(self, event):
        """
        Handles events on the color selection screen.

        Specifically, it checks for a mouse click on the 'Empezar' button to
        transition the game state to the initial dice roll.

        Parameters
        ----------
        event : pygame.event.Event
            The Pygame event to process.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:  # pylint: disable=no-member
            if self.boton_empezar_rect and self.boton_empezar_rect.collidepoint(event.pos):
                self.estado_juego = TIRADA_INICIAL

    def _draw_pantalla_tirada_inicial(self):
        """
        Draws the screen for the initial dice roll.

        This screen shows the "Tirando dados..." (Rolling dice...) message,
        the results of the roll for both players, and announces the winner who
        will start the game.
        """
        self.screen.fill(COLOR_FONDO_MESA)
        if not self.ganador_tirada_inicial:
            msg = "Tirando dados..."
        else:
            msg = f"Blancas: {self.dados_iniciales['blancas']} | Negras: {self.dados_iniciales['negras']}"

        texto_surface = self.large_font.render(msg, True, COLOR_TEXTO_NEGRO)
        texto_rect = texto_surface.get_rect(center=(WIDTH / 2, HEIGHT / 3))
        self.screen.blit(texto_surface, texto_rect)

        if self.ganador_tirada_inicial and self.ganador_tirada_inicial != "empate":
            ganador_msg = f"Comienzan las {self.ganador_tirada_inicial}"
            ganador_surface = self.large_font.render(ganador_msg, True, COLOR_TEXTO_NEGRO)
            ganador_rect = ganador_surface.get_rect(center=(WIDTH / 2, HEIGHT / 2))
            self.screen.blit(ganador_surface, ganador_rect)

    def _manejar_logica_tirada_inicial(self):
        """
        Manages the logic for the initial dice roll.

        This method handles the timing and logic for the pre-game roll. It rolls
        one die for each player, determines the winner, and handles ties by
        re-rolling. It includes timed pauses to make the process clear to the user.
        """
        ahora = time.time()
        # Si no hay una tirada en curso, empezamos una
        if self.tiempo_inicio_tirada is None:
            self.tiempo_inicio_tirada = ahora
            self.dados_iniciales["blancas"] = random.randint(1, 6)
            self.dados_iniciales["negras"] = random.randint(1, 6)

            if self.dados_iniciales["blancas"] > self.dados_iniciales["negras"]:
                self.ganador_tirada_inicial = "blancas"
            elif self.dados_iniciales["negras"] > self.dados_iniciales["blancas"]:
                self.ganador_tirada_inicial = "negras"
            else:
                # Empate, preparamos para re-tirar después de una pausa
                self.ganador_tirada_inicial = "empate"

        # Lógica de transición
        if self.ganador_tirada_inicial:
            # Si hay un ganador, esperamos para mostrar el resultado y luego cambiamos de estado
            if self.ganador_tirada_inicial != "empate":
                if ahora - self.tiempo_inicio_tirada > 2.5:
                    self.estado_juego = JUEGO
                    self._setup_game()
            # Si es un empate, esperamos un segundo y luego reiniciamos la tirada
            elif self.ganador_tirada_inicial == "empate":
                if ahora - self.tiempo_inicio_tirada > 1.0:
                    self.tiempo_inicio_tirada = (
                        None  # Esto provocará una nueva tirada en el siguiente frame
                    )
                    self.ganador_tirada_inicial = None

    def run(self):
        """
        The main loop of the game.

        This method contains the main event loop that drives the entire application.
        It handles user input, updates the game state, and calls the appropriate
        drawing functions based on the current `estado_juego`.
        """
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # pylint: disable=no-member
                    running = False

                if self.estado_juego == SELECCION_COLOR:
                    self._handle_eventos_seleccion_color(event)
                elif self.estado_juego == JUEGO:
                    if self.game_over:
                        if event.type in [pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN]:
                            running = False
                    else:
                        if (
                            event.type == pygame.MOUSEBUTTONDOWN  # pylint: disable=no-member
                        ):  # pylint: disable=no-member
                            self._handle_click(event.pos)

            # --- State-based Drawing and Logic ---
            if self.estado_juego == SELECCION_COLOR:
                self._draw_pantalla_seleccion_color()
            elif self.estado_juego == TIRADA_INICIAL:
                self._manejar_logica_tirada_inicial()
                self._draw_pantalla_tirada_inicial()
            elif self.estado_juego == JUEGO:
                if not self.juego_iniciado:
                    print(
                        f"Inicia el turno para {self.game.get_current_player().get_nombre()} con dados {self.game.dice.get_values()}"
                    )
                    if not self._has_any_legal_moves():
                        self._end_turn()
                    self.juego_iniciado = True

                self.screen.fill(BOARD_COLOR)
                self._draw_board()
                self._draw_checkers()
                self._draw_game_info()
                if self.game_over:
                    self._draw_game_over_screen()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()  # pylint: disable=no-member
        sys.exit()


if __name__ == "__main__":
    ui = PygameUI()
    ui.run()
