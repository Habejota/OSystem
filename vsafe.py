from time import sleep
from os import system, getcwd, chdir, makedirs, startfile

diretory = chdir()
def start():
    mensage()
    install()
    mensage()
    install()
    
def install():
    system("git clone https://github.com/TenayaOS/Vsafe.git")
    print("")
    
def mesage():
    system("cls")
    print("================================")
    print("           Vsafe (TM)           ")
    print("    Copyright (C) 2020-2021     ")
    print(" Github Inc. Apache License 2.0 ")
    print("      \033[36mHotkey:    <CTRL><C>\033[m     ")
    print("================================")
    print("")

