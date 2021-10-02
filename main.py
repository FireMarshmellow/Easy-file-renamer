"""
Code by
  __  __      _ _                 _____ _          
 |  \/  | ___| | | _____      __ |  ___(_)_ __ ___ 
 | |\/| |/ _ \ | |/ _ \ \ /\ / / | |_  | | '__/ _ \
 | |  | |  __/ | | (_) \ V  V /  |  _| | | | |  __/
 |_|  |_|\___|_|_|\___/ \_/\_/   |_|   |_|_|  \___|
check out my stuff on https://linktr.ee/Mellowfire
"""

import os, sys
from typing import NamedTuple

Path_to_folder = input("path to folder:")
name_of_file = input("name:")
number = int(input("Number to start:"))


def rename_files(path, name, num):
    files = os.listdir(path)
    files.sort()
    for i in range(len(files)):
        os.rename(
            os.path.join(path, files[i]),
            os.path.join(path, name + str(num + i) + "." + files[i].split(".")[-1]),
        )


rename_files(Path_to_folder, name_of_file, number)
