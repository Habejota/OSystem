# Python Modules
from os import system, getcwd, chdir, makedirs, startfile, removedirs, listdir, rename
from time import sleep
from socket import gethostname, gethostbyname
from random import randint
import glob, socket
from getpass import getpass

from controll import *

try:
    from tqdm import tqdm
except ModuleNotFoundError:
    startShellKernelSetting = False
else:
    startShellKernelSetting = True

# Informations
version = "1.12.6"
author = "Felipe Souza"
license_ = open("LICENSE").read()
changelog = open("CHANGELOG.txt").read()

# Functions
def choice(msg):
    responce = str(input(fr"{msg} [Y/N]?")).upper()
    if responce == "Y":
        return True
    elif responce == "N":
        return False
def beep():
    system(fr"root\beep.exe")
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

#Kernel Modules
menu = open(r"lib\menu.lib").read()
setup = open(r"lib\setup.lib").read()
system_lib = open(r"lib\system.lib").read()
display = open(r"lib\display.lib").read()
sound_driver = open(r"lib\sound.lib")
network_lib = open(r"lib\network.lib")
date_lib = open(r"lib\date.lib")
mainDriver = open(r"lib\main.lib")

# Global WMEMORY
hostname = gethostname()
ifconfig = gethostbyname(hostname)
port_session = randint(500, 65535)
distibuition = fr"OSystem Distuibuition {version}" 
source = "https://github.com/Habejota/OSystem (Free Source Code)"
language = "Englesh (United States of America)"
disk_partition = "0x800-1x300"

# Himem Modules
def testExtendedMemory(partition_disk):
    print("HIMEM is testing extended memory.", end=""), sleep(1)
    print(".", end=""), sleep(1)
    print(".", end=""), sleep(1)
    print("done.")  
    return disk_partition, hostname
def himem(partition, port):
    depr, adress = testExtendedMemory(disk_partition)
    list_adress = [hostname, port_session, disk_partition]
    for s_config in list_adress:
        if s_config == disk_partition:
            return s_config, depr, port
        else:
            return None, None, None
    print("")
    
    