# Python Modules
from os import system, getcwd, chdir, makedirs, startfile, removedirs, listdir, rename
from time import sleep
from socket import gethostname, gethostbyname
from random import randint
import glob, socket
from version import *
from kernel import *
try:
    from tqdm import tqdm
except ModuleNotFoundError:
    startShellKernelSetting = False
else:
    startShellKernelSetting = True

# Informations
version = "1.12.8"
author = "Felipe Souza"

# Functions
def choice(msg):
    responce = str(input(fr"{msg} [Y/N]?")).upper()
    if responce == "Y":
        return True
    elif responce == "N":
        return False
def beep():
    system(fr"usr\bin\beep.exe")
def Progressbar():
    for i in tqdm(range(120)):
        sleep(0.010)
def main_function():
    print("This is a main implemented function!")
    print("You cannot acess this function if you dont tell for kernel main password:")
    password_inputadonocudales: str = input("Kernel Password: ")
    if password_inputadonocudales == "0x800-1x300":
        return True
    else:
        print("Acess diened!")
        return False




