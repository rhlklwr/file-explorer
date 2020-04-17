import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()
root.title('Easy Open')

root.iconbitmap(r'icon.ico')

apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as apps_list:
        temp_apps = apps_list.read()
        temp_apps = temp_apps.split(',')
        apps = [x for x in temp_apps if x.strip()]


def add_app():
    for widget in frame.winfo_children():
        widget.destroy()
        
    filename = filedialog.askopenfilename(initialdir='/', title='Select File',
                                          filetypes=(('Executables', '*.exe'), ('All Files', '*.*')))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg='grey')
        label.pack()


def run_apps():
    for app in apps:
        os.startfile(app)


canvas = tk.Canvas(root, height=400, width=400, bg="blue")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

open_file = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg='grey', command=add_app)
open_file.pack()

run_apps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg='green', command=run_apps)
run_apps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open('save.txt', 'w') as apps_list:
    for app in apps:
        apps_list.write(app + ',')