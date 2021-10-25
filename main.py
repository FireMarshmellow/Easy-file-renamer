"""
Code by
  __  __      _ _                 _____ _          
 |  \/  | ___| | | _____      __ |  ___(_)_ __ ___ 
 | |\/| |/ _ \ | |/ _ \ \ /\ / / | |_  | | '__/ _ \
 | |  | |  __/ | | (_) \ V  V /  |  _| | | | |  __/
 |_|  |_|\___|_|_|\___/ \_/\_/   |_|   |_|_|  \___|
check out my stuff on https://linktr.ee/Mellowfire
i make ugly code but it works :)
"""

import os, sys
from typing import NamedTuple, Text
import tkinter
from tkinter import Tk, filedialog

root = tkinter.Tk()
root.title("Easy File Renamer")


name_entry = tkinter.Entry(root)
name_entry.insert(0, "")

number_entry = tkinter.Entry(root)
number_entry.insert(0, "")


def start():
    print(Path_to_folder)
    hellow = str(name_entry.get())
    hello = int(number_entry.get())
    rename_files(Path_to_folder, hellow, hello)


start_button = tkinter.Button(
    root,
    text="Start",
    command=start,
)


def Path_to_folder():
    global Path_to_folder
    Path_to_folder = filedialog.askdirectory()
    change_sorter_in(Path_to_folder)


def change_sorter_in(Path_to_folder):
    sorter_in_path["text"] = Path_to_folder


sorter_in_path = tkinter.Button(
    root, height=3, width=50, text="path to folder:", command=Path_to_folder
)

name_label = tkinter.Label(root, text="Name:")
Num_label = tkinter.Label(root, text="Number to start:")


def rename_files(path, name, num):
    files = os.listdir(path)
    files.sort()
    for i in range(len(files)):
        os.rename(
            os.path.join(path, files[i]),
            os.path.join(path, name + str(num + i) + "." + files[i].split(".")[-1]),
        )


sorter_in_path.grid(row=0, column=0, columnspan=2)
name_entry.grid(row=1, column=1)
name_label.grid(row=1, column=0)

number_entry.grid(row=2, column=1)
Num_label.grid(row=2, column=0)

start_button.grid(row=100, column=0, columnspan=2)
root.mainloop()
