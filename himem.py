from os import system, getcwd, chdir, makedirs, startfile
from time import sleep
from socket import gethostname, gethostbyname
from random import randint
import glob, socket
try:
    from tqdm import tqdm
except ModuleNotFoundError:
    startShellKernelSetting = False
else:
    startShellKernelSetting = True

__version__ = "1.12"
__author__ = "Felipe Souza"
__license__ = open("LICENSE").read()
__changelog__ = open("CHANGELOG.txt").read()

def choice(msg):
    responce = str(input(fr"{msg} [Y/N]?")).upper()
    if responce == "Y":
        return True
    elif responce == "N":
        return False
def beep():
    system(fr"root\beep.exe")
def Progressbar():
    for i in tqdm(range(1000)):
        sleep(0.001)
def main_function():
    print("This is a main implemented function!")
    print("You cannot acess this function if you dont tell for kernel main password:")
    password_inputadonocudales: str = input("Kernel Password: ")
    if password_inputadonocudales == "0x800-1x300":
        return True
    else:
        print("Acess diened!")
        return False
class mirror:
    def mirror():
        print("This Operational System is hospeded in:")
        print("https://github.com/TenayaOS/OSystem.git (URL Github System)\n")
        name: str = input("Commit NAME: ")
        system(f'git commit -a -m "{name}"')
        system("git push origin main")
    def mirror_pull():
        print("This Operational System is hospeded in:")
        print("https://github.com/Habejota/OSystem.git (URL Github System)\n")
        system("git pull")

hostname = gethostname()
ifconfig = gethostbyname(hostname)
port_session = randint(500, 65535)
simbols = ["✔", "✘"]
distibuition = fr"OSystem Distuibuition {__version__}" 
source = fr"https://github.com/Habejota/OSystem (Free Source Code)"
language = fr"Englesh (United States of America"
disk_partition = "0x800-1x300"

def testExtendedMemory(partition):
    print("HIMEM is testing extended memory.", end=""), sleep(1)
    print(".", end=""), sleep(1)
    print(".", end=""), sleep(1)
    print("done.")
