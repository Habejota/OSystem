from os import system, getcwd, chdir, makedirs, startfile, removedirs
from time import sleep
from socket import gethostname, gethostbyname
import glob, socket

__version__ = "1.10.2"
__author__ = "Felipe Souza"
__license__ = open("LICENSE").read()

class mirror:
    def mirror():
        print("This Operational System is hospeded in:")
        print("https://github.com/TenayaOS/OSystem.git (URL Github System)\n")
        name: str = input("Commit NAME: ")
        system(f'git commit -a -m "{name}"')
        system("git push origin main")
    def mirror_pull():
        print("This Operational System is hospeded in:")
        print("https://github.com/TenayaOS/OSystem.git (URL Github System)\n")
        system("git pull")
    def mirror_charge():
        system("git branch -a beta")

system("cls")

def python(args):
    system(f"{args}")



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
msys = mirror
hostname = gethostname()
ifconfig = gethostbyname(hostname)
class sdk:
    def __init__(self):
        self.file_name = self.get_sdkFIleNAME()
        self.text_File = self.openFileToSDK()
        self.Load_in_MEMORY(partition=self.file_name, rangeLoad=-312785364)

    def get_sdkFIleNAME(self):
        return str(input("Filename to Open in Sdk: /"))

    def openFileToSDK(self):
        with open(self.file_name) as arq:
            return arq

    def Load_in_MEMORY(self, partition, rangeLoad):
        disk_partition = partition
        while_Value = rangeLoad
        asp = 0
        while asp != 20:
            asp =+1
            for i in range(0, 2):
                try:
                    spt = open(disk_partition, "rt")
                    spt = spt.read()
                except FileNotFoundError:
                    print("Dont have a instance_name on this partition readed")
                    print("Please Load a new partition on 0x800-1x300")
                else:
                    print("[ ]This cicle was completed.")
                    break
                    
class Tenaya:
    def __init__(self):
        try:
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
        except KeyboardInterrupt:
            system("cls")
            print("Fail in Load Files in Memory: MemoryError")
            print("HIMEM is trying repair WMemory. . ."), sleep(1.287)
            print("")
            print("Clearing Ram partition disk: 0x800-1x300"), sleep(3.999)
        else:
            self.prompt = "\033[32m$\033[m "
            Tenaya.welcome()
            Tenaya.command()

    def welcome():
        print(f"\033[36mWelcome to Tardis Operational System {__version__}\033[m")
        print(f"Build version Tardis {__version__}: https://github.com/TenayaOS/OSystem")
        print("")
    def command():
        for i in range(0, 10):
            system(fr"root\bin\beep.exe")
        while True:
            try:
                cmd: str = input("\033[32m$\033[m ").strip()
                try:
                    """
                    rss = open(cmd)
                    rss.close()"""
                    pass
                except FileNotFoundError:
                    if cmd == "exit":
                        print("Power off computer. . ."), sleep(4.069)
                        break
                    elif cmd == "clear" or cmd == "cls":
                        system("cls")
                    elif cmd == "ifconfig":
                        print(f"IP: {ifconfig} (Hostname: {hostname})")
                    elif cmd == "hostname":
                        print(f"Hostname: {hostname}")
                    elif cmd.startswith("python"):
                        python(cmd)
                    elif cmd.startswith("echo"):
                        cmd = cmd.replace("echo ", "")
                        cmd = cmd.replace("echo",  "")
                        if cmd == "":
                            print("Echo driver is loaded in memory 0x800-1x300")
                        else:
                            print(cmd)
                        cmd = "ECHO DIRVER"
                    elif cmd.startswith("rmdir"):
                        cmd = cmd.replace("rmdir", "")
                        cmd = cmd.replace("rmdir ", "")
                        removedirs(cmd)
                    elif cmd.startswith("mirror"):
                        if cmd == "mirror":
                            msys.mirror()
                        elif cmd == "mirror -p":
                            msys.mirror_pull()
                        elif cmd == "mirror -c":
                            msys.mirror_charge()
                        else:
                            print("Use: mirror [args][datas]")
                            print("mirror:")
                            print("  mirror -p: Pull and update code")
                            print("  mirror -c: Charge branch of System")
                    elif cmd == "sdk":
                       print("Starting SDK Api - Python SDK OSystem")
                       print("If your computer have few ram memory press CTRL+C")
                       try:
                            input("PRESS ENTER TO OPEN SDK. . .")
                       except KeyboardInterrupt:
                            print("The launcher was closed. . .")
                       else:
                            sdk()
                    elif cmd == "command":
                        chdir("..")
                        system("python command.py")
                        chdir("home")
                    elif cmd.startswith("mem"):
                        print("Reading disk partitions. . ."), sleep(1.999)
                        print("Writing strings in disk as 0x800-1x300. . .") 
                        sleep(1.023)
                        
                        cmd = cmd.replace("mem ", "")
                        cmd = cmd.replace("mem", "")
                        system(f"rem {cmd}")
                    elif cmd.startswith("mkdir"):
                        cmd = cmd.replace("mkdir", "")
                        cmd = cmd.replace("mkdir ", "")
                        if cmd == "":
                            continue
                        else:
                            Tenaya.make_dir(cmd)
                    elif cmd == "license":
                        print(__license__)
                    elif cmd.startswith("banner"):
                        cmd = cmd.replace("banner",  "")
                        cmd = cmd.replace("banner ", "")
                        system(fr"root\bin\banner.exe {cmd}")
                    elif cmd == "ctris":
                        system("root\bin\ctris.exe")
                    elif cmd.startswith("nano"):
                        cmd = cmd.replace("nano ", "")
                        cmd = cmd.replace("nano",  "")
                        system(fr"root\bin\nano.exe {cmd}")
                    elif cmd == "nimesweeper":
                        system(fr"root\bin\nimesweeper.exe")
                    elif cmd.startswith("nc"):
                        system(fr"root\bin\{cmd}")
                    elif cmd == "sudoku":
                        system(fr"root\bin\sudoku.exe")
                    elif cmd.startswith("telnet"):
                         system(fr"root\bin\{cmd}")
                    elif cmd.startswith("wget"):
                        system(fr"root\bin\{cmd}")
                    elif cmd.startswith("scp"):
                        system(fr"root\bin\{cmd}")
                        
                    elif cmd == "pwd":
                        print(getcwd())
                    elif cmd == "if" or cmd == "dir":
                        Tenaya.dirs_os()
                    elif cmd == "":
                        print()
                        continue
                    else:
                        Tenaya.cannot()
                else:
                    Tenaya.cannot()
                print("")
            except KeyboardInterrupt:
                break
    def make_dir(dir_name):
        makedirs(dir_name)
    def dirs_os():
        for f in glob.glob('*.*'):
            print(f)
    def clear():
        system('cls')
    def cannot():
        print("Sorry! Cannot execute this Command in shell!")
        return True

