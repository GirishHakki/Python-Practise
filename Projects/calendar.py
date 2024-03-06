from tkinter import ttk
import ttkbootstrap

#setup the window
root = ttkbootstrap.Window(themename='cyborg')
root.title('Calendar')

#function to get the date
def see_date():
    date = cal.entry.get()
    date_label.config(text=date)

#this is the DateEntry widget
cal = ttkbootstrap.DateEntry(root,dateformat='%d/%m/%Y', bootstyle='info')
cal.pack(padx=40, pady=40)

#button to get the selected date
btn = ttk.Button(root, text='Show Date', bootstyle='light-outline', command=see_date)
btn.pack(padx=40, pady=45)

date_label = ttk.Label(root,text="No date Selected")
date_label.pack(padx=40, pady=50)

root.mainloop()