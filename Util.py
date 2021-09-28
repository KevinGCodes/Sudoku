def cell_clicked(evt, cells, i, j, gui):
    gui.repaint_background()
    if gui.selected_cell == (i, j):
        gui.selected_cell = None
        return
    gui.selected_cell = (i, j)

    for k in range(len(cells)):
        cells[i][k].configure(bg='#67d5db')
        cells[k][j].configure(bg='#67d5db')
    cell = cells[i][j]
    cell.configure(bg='#16adb5')


def number_clicked_handler(event, gui):
    code = int(event.keycode)
    if gui.selected_cell is None:
        return
    i, j = gui.selected_cell
    if gui.game.preset[i][j]:
        return
    elif code == 8:
        gui.game.board[i][j] = 0
        gui.update()
    elif code > 57 or code < 49:
        return
    else:
        gui.game.enter_number(i, j, code - 48)
        gui.update()
