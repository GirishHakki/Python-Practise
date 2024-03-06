from tkinter import *

# Create the main window
root = Tk()
root.title("Digital Whiteboard")

# Create a canvas widget
canvas = Canvas(root, width=800, height=600, bg="white")
canvas.pack()

# Store the starting position of the mouse
start_x = None
start_y = None

# Store the selected color
current_color = "black"

# Function to handle mouse button press
def on_button_press(event):
    global start_x, start_y
    start_x = event.x
    start_y = event.y

# Function to handle mouse motion
def on_move(event):
    global start_x, start_y
    if start_x and start_y:
        canvas.create_line(start_x, start_y, event.x, event.y, fill=current_color, width=2)
        start_x = event.x
        start_y = event.y

# Function to handle mouse button release
def on_button_release(event):
    global start_x, start_y
    start_x = None
    start_y = None

# Function to change the selected color
def change_color(new_color):
    global current_color
    current_color = new_color

# Function to clear the canvas
def clear_canvas():
    canvas.delete("all")

# Create a color palette
color_palette = Frame(root)
color_palette.pack(pady=10)

colors = ["black", "red", "green", "blue", "yellow"]
for color in colors:
    button = Button(color_palette, bg=color, width=5, command=lambda c=color: change_color(c))
    button.pack(side="left", padx=5)

# Create an eraser button
eraser_button = Button(root, text="Eraser", command=lambda: change_color("white"))
eraser_button.pack(pady=5)

# Create a clear button
clear_button = Button(root, text="Clear", command=clear_canvas)
clear_button.pack(pady=5)

# Bind the mouse events to the canvas
canvas.bind("<ButtonPress-1>", on_button_press)
canvas.bind("<B1-Motion>", on_move)
canvas.bind("<ButtonRelease-1>", on_button_release)

# Run the application
root.mainloop()
