from tkinter import *
from OOP2_cell import Cell
import OOP2_settings as settings
import OOP2_utils as utils
root = Tk()
# root.configure(bg = "lightgray")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("OOP2_MineSweeper")
root.resizable(False, False)

def framing():
    top_frame  = Frame(
        root,
        bg='gray',
        width = utils.width_prct(60),
        height = utils.height_prct(20)
    )
    left_frame = Frame(
        root,
        bg='grey',
        width = utils.width_prct(20),
        height = settings.HEIGHT
    )
    bottom_frame = Frame(
        root,
        bg='grey',
        width = utils.width_prct(60),
        height = utils.height_prct(20)
    )
    right_frame = Frame(
        root,
        bg='grey',
        width = utils.width_prct(20),
        height = settings.HEIGHT
    )
    main_frame = Frame(
        root,
        bg='white',
        width = utils.width_prct(60),
        height = utils.height_prct(60)
    )

    top_frame.place(x=288, y=0)
    left_frame.place(x=0, y=0)
    bottom_frame.place(x=288, y=576)
    right_frame.place(x=1152, y=0)
    main_frame.place(x=utils.width_prct(20), y=utils.height_prct(20))
framing()

c1 = Cell()
root.mainloop()
