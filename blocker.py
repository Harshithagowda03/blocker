# Importing required library
from tkinter import *

# Creating GUI Window
window = Tk()
window.geometry('650x400')
window.minsize(650, 400)
window.maxsize(650, 400)
window.title("DataFlair Website Blocker")

# Host Path and IP Address
host_path = r'C:\Windows\System32\drivers\etc\hosts'  # Use raw string or escape backslashes
ip_address = '127.0.0.1'

# Block Function
def Blocker():
    website_lists = enter_Website.get(1.0, END)
    Website = list(website_lists.strip().split(","))
    with open(host_path, 'r+') as host_file:
        file_content = host_file.read()
        for web in Website:
            if web.strip() in file_content:
                display = Label(window, text='Already Blocked', font='arial')
                display.place(x=200, y=250)
            else:
                host_file.write(ip_address + " " + web.strip() + '\n')
                Label(window, text="Blocked", font='arial').place(x=230, y=250)

# Unblock Function
def Unblock():
    website_lists = enter_Website.get(1.0, END)
    Website = list(website_lists.strip().split(","))
    with open(host_path, 'r+') as host_file:
        lines = host_file.readlines()
        host_file.seek(0)
        for line in lines:
            if not any(web.strip() in line for web in Website):
                host_file.write(line)
        host_file.truncate()
        Label(window, text="UnBlocked", font='arial').place(x=350, y=250)

# UI Components
heading = Label(window, text='Website Blocker', font='arial 20 bold')
heading.pack()

label1 = Label(window, text='Enter Website(s):', font='arial 13 bold')
label1.place(x=5, y=60)

enter_Website = Text(window, font='arial', height=2, width=40)
enter_Website.place(x=140, y=60)

block_button = Button(window, text='Block', font='arial', pady=5, command=Blocker, width=6, bg='royal blue1', activebackground='grey')
block_button.place(x=230, y=150)

unblock_button = Button(window, text='UnBlock', font='arial', pady=5, command=Unblock, width=6, bg='royal blue1', activebackground='grey')
unblock_button.place(x=350, y=150)

# Start the GUI loop
window.mainloop()
