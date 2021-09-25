def cell_clicked(evt, cells, i,j, gui):
    gui.update()
    gui.selected_cell = cells[i][j]
    for k in range(0,len(cells)):
        cells[i][k].configure(bg='#67d5db')
        cells[k][j].configure(bg='#67d5db')
    canvas = cells[i][j]
    canvas.configure(bg='#16adb5')