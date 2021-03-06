import tkinter as tk

import ButtonHandlers as bh
import Util as util


class Gui:

    def __init__(self, game):
        self.game = game
        self.selected_cell = None
        self.t = tk.Tk()
        self.cnv = tk.Canvas(self.t, bg='#3b2275')
        self.solve_label = tk.Label(self.cnv, text="", bg='#3b2275')
        self.t.resizable(False, False)
        self.t.title('Sudoku')
        self.cells = [[None for i in range(self.game.width)]
                      for j in range(self.game.height)]
        self.create_widgets()

    def create_widgets(self):
        self.cnv.grid(columnspan=9, rowspan=9)
        self.init_grid()
        solve_button = tk.Button(self.cnv, text="Solve Sudoku!", command=lambda: bh.solve_button_pressed(self))
        solve_button.grid(column=10, row=0, columnspan=3)
        self.solve_label.grid(column=10, row=1)

        generate_button = tk.Button(self.cnv, text="Generate new Game!",
                                    command=lambda: bh.generate_button_pressed(self))
        generate_button.grid(column=10, row=3, columnspan=3)

        is_solved_button = tk.Button(self.cnv, text="Check if Sudoku is solved",
                                     command=lambda: bh.is_solved_button_pressed(self))
        is_solved_button.grid(column=10, row=5, columnspan=3)
        self.is_solved_label = tk.Label(self.cnv, text="", bg='#3b2275')
        self.is_solved_label.grid(column=10, row=6)

        note_message = tk.Message(self.cnv, bg='#3b2275', text="Note: the states are generated randomly and are not "
                                                               "necessarily solvable. "
                                                               "A bad state can lead to a long loop which can make "
                                                               "the program crash.")
        note_message.grid(column=10, row=7, rowspan=3)

    def init_grid(self):

        for i in range(3):
            for j in range(3):
                c = tk.Canvas(self.cnv, width=150, height=150, highlightbackground='#000000',
                              highlightcolor='#000000', bg='#000000', bd=0)
                c.grid(row=i * 3, column=j * 3, columnspan=3, rowspan=3, ipadx=0, pady=0)
                for k in range(3):
                    for l in range(3):
                        d = self.cells[i * 3 + k][j * 3 + l] = tk.Canvas(self.cnv, width=50,
                                                                         highlightbackground='#000000',
                                                                         highlightcolor='#000000', height=50,
                                                                         bg='#FFFFFF')
                        d.grid(row=i * 3 + k, column=l + 3 * j, rowspan=1, columnspan=1)
        self.update()
        self.repaint_background()
        self.add_bindings()

    def add_bindings(self):
        for i in range(self.game.height):
            for j in range(self.game.width):
                d = self.cells[i][j]

                def handler(event, cells=self.cells, i=i, j=j, gui=self):
                    return util.cell_clicked(event, cells, i, j, gui)

                d.bind('<ButtonPress-1>', handler)

                def handler_b(event, gui=self):
                    return util.number_clicked_handler(event, gui)

                d.focus_force()
                d.bind('<KeyPress>', handler_b)

    def update(self):
        for i in range(self.game.height):
            for j in range(self.game.width):
                d = self.cells[i][j]
                d.delete("all")
                d.create_text(25, 25, fill="#000000", font="Times 20 italic bold",
                              text="" if self.game.board[i][j] == 0 else str(self.game.board[i][j]))

    def repaint_background(self):
        for i in range(self.game.height):
            for j in range(self.game.width):
                d = self.cells[i][j]
                d.configure(bg="#FFFFFF")
                if self.game.preset[i][j]:
                    d.configure(bg="#faf1a5")
