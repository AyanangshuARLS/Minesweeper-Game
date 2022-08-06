from tkinter import *
from cell import Cell
import settings
import util

root = Tk()
# OVERRIDE THE SETTINGS OF THE WINDOW
root.configure(bg="orange")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper Game")
root.resizable(False,False)

top_frame = Frame(
    root,
    bg='orange', # Change later to Orange
    width = settings.WIDTH,
    height = util.height_prct(25),
)
top_frame.place(x=0,y=0)

game_title = Label(
    top_frame,
    bg='orange',
    fg = 'black',
    text = 'Minesweeper Game',
    font = ('',48)
)
game_title.place(
    x=util.width_rct(25), y=0
)

left_frame = Frame(
    root,
    bg = 'orange', # Change later to Orange
    width = util.width_rct(25),
    height = settings.HEIGHT - util.height_prct(25),
)
left_frame.place(x=0, y=util.height_prct(25))

center_frame = Frame(
    root,
    bg = 'orange', # Change to Orange later
    width = util.width_rct(75),
    height = util.height_prct(75)
)

center_frame.place(
    x=util.width_rct(25),
    y=util.height_prct(25)
)

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column =x, row=y
        )
# Call the label from the Cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(
    x=0, y=0
)

Cell.randomize_mines()






#RUN THE WINDOW
root.mainloop()

