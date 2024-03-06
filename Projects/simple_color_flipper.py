# Project Componenets:

# Tkinter
# ttkthemes
# Tk()= to create main window
# button = to generate random colors
# label = displays the current color in hex
# style = customize the button/label style
# place() = to position the button/label
# mainloop() = to start the event loop

from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
import random

#function to change background color and update label text
def change_color():
    color = random_color()
    root.config(bg=color)
    label.config(text=f"Background Color: {color}")

# functon to generate random color in hexadecimal format
def random_color():
    r = lambda : random.randint(0,255)
    return ('#%02X%02X%02X' % (r(), r(), r()))

# create main window
root = ThemedTk(theme='yaru')
root.config(bg='white')
root.geometry('700x500')
root.title('ColorFlipper')

# create a string variable to store the color code
color_var = StringVar()

# create and configure button
btn = ttk.Button(root, text='Change Color', command=change_color)

# create and configure label
label = Label(root, text="Background Color: ", bg='white', foreground='black')
label.pack()

#place widgets in the middle of the application
label.place(relx=0.5, rely=0.5, anchor=CENTER)
btn.place(relx=0.5, rely=0.4, anchor=CENTER)

root.mainloop()