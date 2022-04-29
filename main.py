from tkinter import *
from turtle import left
import settings
import utils

root = Tk()
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper Game")
root.resizable(False, False)

top_frame = Frame(root, bg="black", width=settings.WIDTH, height=utils.height_percentage(25))
top_frame.place(x=0, y=0)

left_frame = Frame(root, bg="black", width=utils.width_percentage(25), height= utils.height_percentage(75))
left_frame.place(x=0, y=utils.height_percentage(25))

center_frame = Frame(root, bg= "black", width= utils.width_percentage(75), height= utils.height_percentage(75))
center_frame.place(x= utils.width_percentage(25), y= utils.height_percentage(25))
root.mainloop()