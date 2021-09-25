import Gui
import Game
import sudoku_solver

game = Game.Game(9)
game.visualize()
gui = Gui.Gui(game)
gui.t.mainloop()

