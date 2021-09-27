import sudoku_solver


def is_solved_button_pressed(gui):
    is_solved = gui.game.is_solved()
    text = "Sudoku is correctly solved!" if is_solved else "Solution is incorrect"
    gui.is_solved_label.configure(text=text)


def solve_button_pressed(gui):
    solver = sudoku_solver.sudoku_solver(gui.game)
    if gui.game.is_solved():
        return
    if solver.solve():
        gui.update()
    else:
        gui.solve_label.configure(text="There is no solution to this state of the Sudoku!")


def generate_button_pressed(gui):
    gui.solve_label.configure(text="")
    gui.is_solved_label.configure(text="")
    gui.game.randomize()
    gui.update()
    gui.repaint_background()
    gui.update()
