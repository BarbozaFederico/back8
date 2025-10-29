import pytest
from backgammon.core.board import Board
from backgammon.core.checker import Checker


def test_enumerar_opciones_legales_invalid_dados_type():
    """Testea que con un tipo de dado inválido no se generen opciones."""
    board = Board()

    class DummyPlayer:
        def get_color(self):
            return "blancas"

        def get_home_points(self):
            return set(range(18, 24))

        def get_direccion(self):
            return 1

        def get_entry_point(self):
            return 0

        def get_checkers(self):
            return [Checker("blancas") for _ in range(15)]

        def puede_bear_off(self, b):
            return False

    # No debería lanzar un error, sino devolver una lista vacía.
    opciones = board.enumerar_opciones_legales(DummyPlayer(), "invalid_dice")
    assert opciones == []
