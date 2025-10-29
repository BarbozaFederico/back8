"""
Punto de entrada principal para el juego de Backgammon.
"""

from backgammon.pygame_ui.ui import PygameUI

if __name__ == "__main__":
    game = PygameUI()
    game.run()
