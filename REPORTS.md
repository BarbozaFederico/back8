# Automated Reports
## Coverage Report
```text
........................................................................ [ 75%]
.....................F
=================================== FAILURES ===================================
______________________________ test_move_from_bar ______________________________

monkeypatch = <_pytest.monkeypatch.MonkeyPatch object at 0x7fa681ba3400>
mock_pygame = <Mock id='140353117755552'>

    def test_move_from_bar(monkeypatch, mock_pygame):
        """Test moving a checker from the bar to the board."""
        # Mock pygame to avoid display initialization
        monkeypatch.setattr("backgammon.pygame_ui.ui.pygame", mock_pygame)
    
        # Initialize UI
        ui = PygameUI()
        game = ui.game
>       player = game.get_current_player()

tests/test_ui.py:28: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <backgammon.core.backgammon.BackgammonGame object at 0x7fa681f0a470>

    def get_current_player(self) -> Player:
        """
        Returns the current Player object.
    
        Returns
        -------
        Player
        """
>       return self.players[self.current_player_idx]
E       IndexError: list index out of range

backgammon/core/backgammon.py:158: IndexError
=========================== short test summary info ============================
FAILED tests/test_ui.py::test_move_from_bar - IndexError: list index out of range
!!!!!!!!!!!!!!!!!!!!!!!!!! stopping after 1 failures !!!!!!!!!!!!!!!!!!!!!!!!!!!
1 failed, 93 passed in 1.45s

```
## Pylint Report
```text
************* Module cli.console
backgammon/cli/console.py:1:0: C0114: Missing module docstring (missing-module-docstring)
backgammon/cli/console.py:115:16: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
backgammon/cli/console.py:98:26: W0613: Unused argument 'player' (unused-argument)
backgammon/cli/console.py:2:0: W0611: Unused OpcionMovimiento imported from backgammon.core.player (unused-import)
backgammon/cli/console.py:2:0: W0611: Unused SecuenciaMovimiento imported from backgammon.core.player (unused-import)
************* Module core.backgammon
backgammon/core/backgammon.py:180:0: C0301: Line too long (107/100) (line-too-long)
backgammon/core/backgammon.py:1:0: C0114: Missing module docstring (missing-module-docstring)
backgammon/core/backgammon.py:93:16: W0212: Access to a protected member _player of a client class (protected-access)
************* Module core.board
backgammon/core/board.py:528:0: C0325: Unnecessary parens after '=' keyword (superfluous-parens)
backgammon/core/board.py:1:0: C0114: Missing module docstring (missing-module-docstring)
backgammon/core/board.py:15:0: C0413: Import "from backgammon.core.player import OpcionMovimiento" should be placed at the top of the module (wrong-import-position)
backgammon/core/board.py:70:8: C0104: Disallowed name "bar" (disallowed-name)
backgammon/core/board.py:256:8: C0206: Consider iterating with .items() (consider-using-dict-items)
backgammon/core/board.py:259:8: C0206: Consider iterating with .items() (consider-using-dict-items)
backgammon/core/board.py:199:4: R0912: Too many branches (13/12) (too-many-branches)
backgammon/core/board.py:317:16: R1705: Unnecessary "elif" after "return", remove the leading "el" from "elif" (no-else-return)
backgammon/core/board.py:351:12: R1724: Unnecessary "elif" after "continue", remove the leading "el" from "elif" (no-else-continue)
backgammon/core/board.py:436:4: R0914: Too many local variables (24/15) (too-many-locals)
backgammon/core/board.py:443:8: C0415: Import outside toplevel (backgammon.core.player.PasoMovimiento) (import-outside-toplevel)
backgammon/core/board.py:514:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
backgammon/core/board.py:436:4: R0912: Too many branches (25/12) (too-many-branches)
backgammon/core/board.py:436:4: R0915: Too many statements (55/50) (too-many-statements)
backgammon/core/board.py:581:4: R0911: Too many return statements (7/6) (too-many-return-statements)
backgammon/core/board.py:726:8: W0404: Reimport 'OpcionMovimiento' (imported line 15) (reimported)
backgammon/core/board.py:726:8: C0415: Import outside toplevel (backgammon.core.player.OpcionMovimiento, backgammon.core.player.ValorDado) (import-outside-toplevel)
backgammon/core/board.py:814:8: W0404: Reimport 'OpcionMovimiento' (imported line 15) (reimported)
backgammon/core/board.py:814:8: C0415: Import outside toplevel (backgammon.core.player.OpcionMovimiento) (import-outside-toplevel)
************* Module core.dice
backgammon/core/dice.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module core.move
backgammon/core/move.py:1:0: C0114: Missing module docstring (missing-module-docstring)
backgammon/core/move.py:4:0: C0115: Missing class docstring (missing-class-docstring)
backgammon/core/move.py:5:4: R0913: Too many arguments (6/5) (too-many-arguments)
backgammon/core/move.py:5:4: R0917: Too many positional arguments (6/5) (too-many-positional-arguments)
backgammon/core/move.py:1:0: W0611: Unused Optional imported from typing (unused-import)
************* Module core.player
backgammon/core/player.py:1:0: C0114: Missing module docstring (missing-module-docstring)
backgammon/core/player.py:56:4: C0116: Missing function or method docstring (missing-function-docstring)
backgammon/core/player.py:57:4: C0116: Missing function or method docstring (missing-function-docstring)
backgammon/core/player.py:58:4: C0116: Missing function or method docstring (missing-function-docstring)
backgammon/core/player.py:59:4: C0116: Missing function or method docstring (missing-function-docstring)
backgammon/core/player.py:60:4: C0116: Missing function or method docstring (missing-function-docstring)
backgammon/core/player.py:64:4: C0116: Missing function or method docstring (missing-function-docstring)
backgammon/core/player.py:73:4: C0116: Missing function or method docstring (missing-function-docstring)
backgammon/core/player.py:67:0: R0903: Too few public methods (1/2) (too-few-public-methods)
backgammon/core/player.py:84:4: C0116: Missing function or method docstring (missing-function-docstring)
backgammon/core/player.py:84:21: W0613: Unused argument 'opciones' (unused-argument)
backgammon/core/player.py:76:0: R0903: Too few public methods (1/2) (too-few-public-methods)
backgammon/core/player.py:88:0: R0902: Too many instance attributes (8/7) (too-many-instance-attributes)
backgammon/core/player.py:174:4: R0913: Too many arguments (9/5) (too-many-arguments)
backgammon/core/player.py:174:4: R0917: Too many positional arguments (9/5) (too-many-positional-arguments)
backgammon/core/player.py:88:0: R0904: Too many public methods (21/20) (too-many-public-methods)
************* Module pygame_ui.ui
backgammon/pygame_ui/ui.py:700:0: C0301: Line too long (109/100) (line-too-long)
backgammon/pygame_ui/ui.py:799:0: C0301: Line too long (117/100) (line-too-long)
backgammon/pygame_ui/ui.py:991:0: C0301: Line too long (106/100) (line-too-long)
backgammon/pygame_ui/ui.py:1076:0: C0301: Line too long (133/100) (line-too-long)
backgammon/pygame_ui/ui.py:1:0: C0302: Too many lines in module (1098/1000) (too-many-lines)
backgammon/pygame_ui/ui.py:1:0: C0114: Missing module docstring (missing-module-docstring)
backgammon/pygame_ui/ui.py:50:0: R0902: Too many instance attributes (27/7) (too-many-instance-attributes)
backgammon/pygame_ui/ui.py:325:4: R0914: Too many local variables (32/15) (too-many-locals)
backgammon/pygame_ui/ui.py:325:4: R0912: Too many branches (15/12) (too-many-branches)
backgammon/pygame_ui/ui.py:325:4: R0915: Too many statements (62/50) (too-many-statements)
backgammon/pygame_ui/ui.py:523:12: W0612: Unused variable 'color' (unused-variable)
backgammon/pygame_ui/ui.py:649:29: W0212: Access to a protected member _generar_movimientos_posibles of a client class (protected-access)
backgammon/pygame_ui/ui.py:687:29: W0212: Access to a protected member _generar_movimientos_posibles of a client class (protected-access)
backgammon/pygame_ui/ui.py:772:15: W0212: Access to a protected member _generar_movimientos_posibles of a client class (protected-access)
backgammon/pygame_ui/ui.py:837:12: R1705: Unnecessary "elif" after "return", remove the leading "el" from "elif" (no-else-return)
backgammon/pygame_ui/ui.py:898:4: R0913: Too many arguments (7/5) (too-many-arguments)
backgammon/pygame_ui/ui.py:898:4: R0917: Too many positional arguments (7/5) (too-many-positional-arguments)
backgammon/pygame_ui/ui.py:1041:4: R0912: Too many branches (14/12) (too-many-branches)
backgammon/pygame_ui/ui.py:50:0: R0903: Too few public methods (1/2) (too-few-public-methods)
backgammon/pygame_ui/ui.py:2:0: C0411: standard import "sys" should be placed before third party import "pygame" (wrong-import-order)
backgammon/pygame_ui/ui.py:3:0: C0411: standard import "time" should be placed before third party import "pygame" (wrong-import-order)
backgammon/pygame_ui/ui.py:4:0: C0411: standard import "random" should be placed before third party import "pygame" (wrong-import-order)
backgammon/pygame_ui/ui.py:6:0: W0611: Unused PasoMovimiento imported from backgammon.core.player (unused-import)
backgammon/pygame_ui/ui.py:6:0: W0611: Unused SecuenciaMovimiento imported from backgammon.core.player (unused-import)

-----------------------------------
Your code has been rated at 9.30/10


```
