from os import system, getcwd, chdir, makedirs
from time import sleep as delay
from socket import gethostname, gethostbyname

import glob

__version__ = "1.0"
__author__ = "Felipe Souza"


class Tenaya:
    def __init__(self):
        self.clear()
        self.welcome()
        self.command()
   
    def welcome(self):
        print(f"Welcome to Tardis {__version__}")
        print(f"Build version Tardis https://github.com/TenayaOS/OSystem")
        print("")
    
    def command(self):
        chdir("home")
        while True:
            try:
                cmd: str = input("$ ").strip()
                if cmd == "exit":
                    break
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
                    else:
                        self.enter_in_dir(dir_name=cmd)
                elif cmd == "pwd":
                    print(getcwd())
                elif cmd == "ls":
                    self.dirs_os()
                elif cmd == "":
                    continue
                else:
                    self.cannot()
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
            