import Gui
import Game
import sudoku_solver

game = Game.Game(9)
game.visualize()
gui = Gui.Gui(game)
solver = sudoku_solver.sudoku_solver(game)
gui.t.mainloop()

