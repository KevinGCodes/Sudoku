import tkinter as tk
import Util as util

class Gui:

    def __init__(self, game):
        self.game = game
        self.t = tk.Tk()
        self.selected_cell = None
        self.t.title('Sudoku')
        self.cnv = tk.Canvas(self.t, width=450, height=450, bg='#000000')
        self.cnv.grid(columnspan=9, rowspan=9)
        self.cells = [[None for i in range(0, self.game.width)]
                      for j in range(0, self.game.height)]
        self.init_grid()

    def init_grid(self):

        for i in range(0, 3):
            for j in range(0, 3):
                c = tk.Canvas(self.cnv, width=150, height=150,highlightbackground='#000000',
                                                                     highlightcolor ='#000000', bg='#000000', bd=0)
                c.grid(row=i * 3, column=j * 3, columnspan=3, rowspan=3, ipadx=0, pady=0)
                for k in range(0, 3):
                    for l in range(0, 3):
                        d = self.cells[i * 3 + k][j*3+l] = tk.Canvas(self.cnv, width=50,
                                                                     highlightbackground='#000000',
                                                                     highlightcolor='#000000',height=50, bg='#FFFFFF')
                        d.grid(row=i * 3 + k, column=l + 3 * j, rowspan=1, columnspan=1)
        self.update()
        self.repaint_background()
        self.add_bindings()


    def add_bindings(self):
        for i in range(0, self.game.height):
            for j in range(0, self.game.width):
                d = self.cells[i][j]

                def handler(event, cells=self.cells, i=i, j=j, gui=self):
                    return util.cell_clicked(event, cells, i, j, gui)
                d.bind('<ButtonPress-1>', handler)

                def handler_b(event, gui=self):
                    return util.number_clicked_handler(event, gui)

                d.focus_force()
                d.bind('<KeyPress>', handler_b)

    def update(self):
        for i in range(0, self.game.height):
            for j in range(0, self.game.width):
                d = self.cells[i][j]
                d.delete("all")
                d.create_text(25, 25, fill="#000000", font="Times 20 italic bold",
                                   text="" if self.game.board[i][j] == 0 else str(self.game.board[i][j]))

    def repaint_background(self):
        for i in range(0, self.game.height):
            for j in range(0, self.game.width):
                d = self.cells[i][j]
                d.configure(bg="#FFFFFF")
                if self.game.preset[i][j]:
                    d.configure(bg="#faf1a5")
