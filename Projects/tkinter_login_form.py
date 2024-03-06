import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.title("Login Form")
window.geometry('340x440')
window.configure(bg='#333333')

def login():
    username = "girishhakki"
    passsword = "12345"
    if username_entry.get()==username and password_entry.get()==passsword:
        messagebox.showinfo(title="Login Success", message="You Seccussfully logged in")
    else:
        messagebox.showerror(title="Error", message="Invalid login")

frame = tkinter.Frame(bg='#333333')

# creating Widgets
login_label = tkinter.Label(frame, text="Login", bg='#333333', fg='#86efac', font=("Arial", 30))
username_label = tkinter.Label(frame, text="Username", bg='#333333', fg='#bbf7d0',font=("Arial", 16))
username_entry = tkinter.Entry(frame,font=("Arial", 16))
password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))
password_label = tkinter.Label(frame, text="Password", bg='#333333', fg='#bbf7d0', font=("Arial", 16))
login_button = tkinter.Button(frame, text="Login", bg='#86efac', fg='#000', font=("Arial", 16), command=login)

# placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2,pady=30)

frame.pack()




window.mainloop()