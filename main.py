import os

folder=input("Path of Folder to Hide: ")
os.system("attrib +h " + folder)
