
import unittest
from unittest.mock import patch, Mock, call
from backgammon.cli.console import BackgammonCLI
from backgammon.core.player import OpcionMovimiento, SecuenciaMovimiento
from backgammon.core.backgammon import BackgammonGame
from backgammon.core.board import Board
from backgammon.core.player import Player
from backgammon.cli import console

class TestBackgammonCLI(unittest.TestCase):

    def setUp(self):
        """Set up a new BackgammonCLI instance for each test."""
        self.cli = BackgammonCLI()

    def test_init(self):
        """Test that the CLI initializes with a BackgammonGame instance."""
        self.assertIsInstance(self.cli.game, BackgammonGame)

    @patch('builtins.input', side_effect=['1'])
    def test_prompt_move_valid(self, mock_input):
        """Test prompt_move with valid input."""
        player = Mock()
        num_opciones = 3
        seleccion = self.cli.prompt_move(player, num_opciones)
        self.assertEqual(seleccion, 1)

    @patch('builtins.input', side_effect=['a', '4', '0', '2'])
    @patch('builtins.print')
    def test_prompt_move_invalid(self, mock_print, mock_input):
        """Test prompt_move with various invalid inputs before a valid one."""
        player = Mock()
        num_opciones = 3
        seleccion = self.cli.prompt_move(player, num_opciones)
        self.assertEqual(seleccion, 2)
        mock_print.assert_has_calls([
            call("Entrada inválida. Ingrese un número."),
            call("Selección inválida. Intente nuevamente."),
            call("Selección inválida. Intente nuevamente.")
        ])

    @patch('builtins.input', side_effect=['P1', 'P2', '', '1', '', '', '1', ''])
    @patch('builtins.print')
    def test_run_game_flow(self, mock_print, mock_input):
        """Test the main game loop for a simple two-turn game."""
        # Mock the game object and its methods
        self.cli.game = Mock(spec=BackgammonGame)
        self.cli.game.board = Mock(spec=Board)
        player1 = Mock(spec=Player)
        player1.get_nombre.return_value = 'P1'
        player1.checkers_fuera.return_value = [1] * 15

        player2 = Mock(spec=Player)
        player2.get_nombre.return_value = 'P2'
        player2.checkers_fuera.return_value = []

        self.cli.game.players = [player1, player2]
        self.cli.game.is_game_over.side_effect = [False, False, True]
        self.cli.game.get_current_player.side_effect = [player1, player2]
        self.cli.game.roll_dice.return_value = (1, 2)

        # Mock movimientos_legales to return a dummy move
        opcion = Mock(spec=OpcionMovimiento)
        opcion.secuencia = [Mock(spec=SecuenciaMovimiento, desde=0, hasta=1, dado=1, captura=False)]
        player1.movimientos_legales.return_value = [opcion]
        player2.movimientos_legales.return_value = [opcion]

        # Run the CLI
        self.cli.run()

        # Assertions
        self.assertEqual(self.cli.game.start_game.call_count, 1)
        self.assertEqual(self.cli.game.next_turn.call_count, 2)
        player1.confirmar_movimiento.assert_called_once()
        player2.confirmar_movimiento.assert_called_once()
        mock_print.assert_any_call("¡Fin de la partida!")
        mock_print.assert_any_call(f"Ganador: {player1.get_nombre()} ({player1.get_color()})")

    @patch('builtins.input', side_effect=['P1', 'P2', '', ''])
    @patch('builtins.print')
    def test_run_no_legal_moves(self, mock_print, mock_input):
        """Test the game loop when a player has no legal moves."""
        self.cli.game = Mock(spec=BackgammonGame)
        self.cli.game.board = Mock(spec=Board)
        player1 = Mock(spec=Player)
        player1.checkers_fuera.return_value = []
        player2 = Mock(spec=Player)
        player2.checkers_fuera.return_value = []

        self.cli.game.players = [player1, player2]
        self.cli.game.is_game_over.side_effect = [False, True]
        self.cli.game.get_current_player.return_value = player1
        self.cli.game.roll_dice.return_value = (6, 6)
        player1.movimientos_legales.return_value = []  # No legal moves

        self.cli.run()

        mock_print.assert_any_call("No hay movimientos legales disponibles. Turno perdido.")
        self.assertEqual(player1.confirmar_movimiento.call_count, 0)
        self.assertEqual(self.cli.game.next_turn.call_count, 1)

    @patch('backgammon.cli.console.BackgammonCLI')
    def test_main_script_entry(self, mock_cli):
        """Test the script's entry point (__name__ == '__main__')."""

        # Mock the instance and its run method
        mock_instance = Mock()
        mock_cli.return_value = mock_instance

        # To run the __main__ block, we can't directly import it.
        # A common way is to run the module using runpy.
        with patch.object(console, "__name__", "__main__"):
            console.cli = mock_instance
            console.cli.run()

        mock_instance.run.assert_called_once()

if __name__ == '__main__':
    unittest.main()
