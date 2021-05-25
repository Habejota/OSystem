from os import system, getcwd, chdir, makedirs, startfile
from time import sleep
from socket import gethostname, gethostbyname
import glob

__version__ = "1.0"
__author__ = "Felipe Souza"

def loadMemory(file, statment=0):
    with open(file, "wt") as memory:
        memory = memory.read()
        memory.write(hostname, ifconfig, "logic.py", "python.exe", "os, time, socket, logic, glob")
        
system("cls")
hostname = gethostname()
ifconfig = gethostbyname(hostname)
class Tenaya:
    def __init__(self):
        print("[x] Loading Himem-X Exetended memory.")
        print("starting boot kernel is loading. . ."), sleep(1.68)
        print("Hardware drive Keyboard.sys and FD12SH.zip")
        print("mirror_1: https://github.com/TenayaOS/OSystem")
        print("mirror_2: https://github.com/TenayaOS/OSystem.git (Git Files)")
        print("[x] System kernel wmemory rom. . ."), sleep(2)
        print("[x] Install database github updates. . ."), sleep(2.999)
        print("[ ] Calling self.command( __version__)")
        print("")
        print("")
        self.prompt = "$ "
        self.welcome()
        self.command()
   
    def welcome(self):
        print(f"\033[36mWelcome to Tardis Operational System {__version__}\033[m")
        print(f"Build version Tardis {__version__}: https://github.com/TenayaOS/OSystem")
        print("")
    
    def command(self):
        chdir("home")
        rds = False
        while True:
            try:
                cmd: str = input(self.prompt).strip()
                try:
                    rss = open(cmd)
                    rss.close()
                except FileNotFoundError:
                    if cmd == "exit":
                        break
                    elif cmd == "clear":
                        system("cls")
                    elif cmd == "ifconfig":
                        print(f"IP: {ifconfig} (Hostname: {hostname})")
                    elif cmd == "hostname":
                        print(f"Hostname: {hostname}")
                    
                    elif cmd.startswith("mkdir"):
                        cmd = cmd.replace("mkdir", "")
                        cmd = cmd.replace("mkdir ", "")
                        if cmd == "":
                            continue
                        else:
                            self.dir_name(cmd)
                    elif cmd.startswith("cd"):
                        cmd = cmd.replace("cd", "")
                        cmd = cmd.replace("cd ", "")
                        if cmd == "":
                            continue
                        elif cmd == "drive":
                            chdir("..")
                            chdir("..")
                            chdir("drive")
                        else:
                            self.enter_in_dir(dir_name=cmd)
                    elif cmd == "pwd":
                        print(getcwd())
                    elif cmd == "if":
                        self.dirs_os()
                    elif cmd == "":
                        continue
                    else:
                        self.cannot()   
                else:
                    system(cmd)
            except KeyboardInterrupt:
                break
    def make_dir(self, dir_name):
        makedirs(dir_name)
    def enter_in_dir(self, dir_name):
        try:    
            chdir(dir_name)
        except:
            print("Sorry! Cannot open this diretory!")       
    def dirs_os(self):
        for f in glob.glob('*.*'):
            print(f)
    def clear(self):
        system('cls')     
    def cannot(self):
        print("Sorry! Cannot execute this Command!")
        return True
            