from tkinter import *

root = Tk()
root.configure(bg = "lightgray")
root.geometry('1440x720')
root.title("OOP2_MineSweeper")
root.resizable(False, False)

def framing():
    top_frame = Frame(
        root,
        bg='grey',
        width = '1440',
        height = '144'
    )
    left_frame = Frame(
        root,
        bg='grey',
        width = '288',
        height = '720'
    )
    bottom_frame = Frame(
        root,
        bg='grey',
        width = '1440',
        height = '144'
    )
    right_frame = Frame(
        root,
        bg='grey',
        width = '288',
        height = '720'
    )

    top_frame.place(x=0, y=0)
    left_frame.place(x=0, y=0)
    bottom_frame.place(x=288, y=576)
    right_frame.place(x=1152, y=0)
framing()
root.mainloop()
