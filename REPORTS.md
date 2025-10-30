# Automated Reports
## Coverage Report
```text
........................................................................ [ 77%]
.....................                                                    [100%]
================================ tests coverage ================================
_______________ coverage: platform linux, python 3.10.18-final-0 _______________

Name                            Stmts   Miss Branch BrPart  Cover   Missing
---------------------------------------------------------------------------
backgammon/core/backgammon.py      55      0     24      1    99%   110->117
backgammon/core/board.py          338     29    198     33    87%   316->315, 318, 319->315, 348, 352, 358, 364, 403-404, 409->408, 421->429, 454-455, 469->464, 503-504, 530->537, 545-548, 558-567, 579, 624, 635, 663, 730, 755->754, 771->782, 775->782, 777->782, 778->777, 784, 788-789, 797->exit, 869
backgammon/core/checker.py         44      0      0      0   100%
backgammon/core/dice.py            13      0      0      0   100%
backgammon/core/move.py            18      0      4      0   100%
backgammon/core/player.py          80      0      2      0   100%
---------------------------------------------------------------------------
TOTAL                             548     29    228     34    91%
Coverage XML written to file cobertura.xml
93 passed in 0.60s

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
