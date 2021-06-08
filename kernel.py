from os import system, getcwd, chdir, makedirs, startfile
from time import sleep
from socket import gethostname, gethostbyname
import glob, socket

__version__ = "1.10.6"
__author__ = "Felipe Souza"
__license__ = open("LICENSE").read()

class mirror:
    def mirror():
        print("This Operational System is hospeded in:")
        print("https://github.com/TenayaOS/OSystem.git (URL Github System)\n")
        name: str = input("Commit NAME: ")
        system(f'bin\git.exe commit -a -m "{name}"')
        system("bin\git.exe push origin main")
    def mirror_pull():
        print("This Operational System is hospeded in:")
        print("https://github.com/TenayaOS/OSystem.git (URL Github System)\n")
        system("bin\git.exe pull")
    def mirror_charge():
        system("git branch -a beta")

system("cls")
system(fr"PATH=%path%;{getcwd()}\bin")

def python(args):
    system(fr"var\{args}")
def beep():
    system(fr"bin\beep.exe")

msys = mirror
hostname = gethostname()
ifconfig = gethostbyname(hostname)
distibuition = fr"OSystem Distuibuition {__version__}" 
source = fr"https://github.com/TenayaOS/OSystem (Free Source Code)"
language = fr"Englesh (United States of America"
disk_partition = "0x800-1x300"
error_msg = """Sorry! This is a internal error in main code!"""

class Tenaya:
    def __init__(self):
        try:
            print("Starting kernel propieties. . ."), sleep(1)
            beep()
            beep()
            print("[ ] Loading System code libraries. . ."), sleep(2)
            beep()
            beep()
            beep()
            print("[ ] DISK Configuration: USB COM Port"), sleep(3)
            beep()
            beep()
            beep()
            beep()
        except KeyboardInterrupt:
            print("")
        else:
            self.prompt = "\033[32m$\033[m "
            Tenaya.welcome()
            Tenaya.command()

    def welcome():
        system("cls")
        print("")
        print("_"*64)
        system(fr"bin\banner.exe OSYSTEM")        
        print("_"*64)
        print(f"\n\033[36mWelcome to Tardis Operational System {__version__}\033[m")
        print(f"Build version Tardis {__version__}: https://github.com/TenayaOS/OSystem")
        print(" ")
    def command():
        for i in range(0, 6):
            beep()
        while True:
            try:
                cmd: str = input("\033[32m$\033[m ").strip()    
                if __name__ == "__main__":
                    if cmd == "exit":
                        break
                    elif cmd == "source":
                        print(source)
                    elif cmd == "disk":
                        print(disk_partition)
                    elif cmd == "distribuition":
                        print(distibuition)
                    elif cmd == "language":
                        print(language)
                    elif cmd == "clear" or cmd == "cls":
                        system("cls")
                    elif cmd == "ifconfig":
                        print(f"""
Software Loopback Interface 1
        Link encap: Local loopback
        inet addr:{ifconfig} Mask: 255.0.0.0
        MTU: 1500 Speed:1073,74 Mbps
        Admin status:UP Oper status:OPERATIONAL
        RX packets:0 dropped:0 errors:0 unkown:0
        TX packets:0 dropped:0 errors:0 txqueuelen:0

Qualcomm Atheros QCA9377 Wireless Network Adapter
        Link encap: IEEE 802.11 HWaddr: 5C-C9-D3-8D-23-9D
        inet addr:{ifconfig} Mask: 255.255.255.0
        MTU: 1500 Speed:108,30 Mbps
        Admin status:UP Oper status:OPERATIONAL
        RX packets:154204 dropped:0 errors:0 unkown:0
        TX packets:106105 dropped:0 errors:0 txqueuelen:0
                                        """)
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
                    elif cmd == "command":
                            system("var\python.exe command.py")
                    elif cmd.startswith("mem"):
                            print("Reading disk partitions. . ."), sleep(1.999)
                            print("Writing strings in disk as 0x800-1x300. . .") 
                            sleep(1.023)
                            
                            cmd = cmd.replace("mem ", "")
                            cmd = cmd.replace("mem", "")
                            system(f"rem {cmd}")
                            beep()
                            beep()
                            beep()
                            beep()
                            beep()
                            beep()
                            beep()
                            beep()
                            beep()
                            beep()
                            beep()
                            beep()
                            beep()
                            beep()
                            beep()
                    elif cmd == "license":
                            print(__license__)
                    elif cmd.startswith("banner"):
                            cmd = cmd.replace("banner",  "")
                            cmd = cmd.replace("banner ", "")
                            system(fr"bin\banner.exe {cmd}")
                    elif cmd.startswith("nano"):
                            cmd = cmd.replace("nano ", "")
                            cmd = cmd.replace("nano",  "")
                            system(fr"bin\nano.exe {cmd}")
                    elif cmd == "nimesweeper":
                            system(fr"bin\nimesweeper.exe")
                    elif cmd.startswith("nc"):
                            system(fr"bin\{cmd}")
                    elif cmd == "sudoku":
                            system(fr"bin\sudoku.exe")
                    elif cmd.startswith("telnet"):
                            system(fr"bin\{cmd}")
                    elif cmd.startswith("wget"):
                            system(fr"bin\{cmd}")
                    elif cmd.startswith("scp"):
                            system(fr"bin\{cmd}")
                    elif cmd == "ctrl":
                         system(fr"bin\login.exe")
                    elif cmd.startswith("balance"):
                        system(fr"bin\{cmd}")
                    elif cmd == "2048":
                        system(fr"bin\{cmd}.exe")
                    elif cmd.startswith("pip"):
                        cmd = cmd.replace("pip",  "")
                        cmd = cmd.replace("pip ", "")
                        system(f"var\python.exe var\pip\__main__.py {cmd}")
                    elif cmd.startswith("connect"):
                        system(fr"bin\{cmd}")
                    elif cmd.startswith("./"):
                        cmd=cmd.replace("./", "")
                        system(fr"{cmd}")
                    elif cmd.startswith("ping"):
                        system(cmd)
                    elif cmd == "pwd":
                            print(getcwd())
                    elif cmd.startswith("root"):
                        if cmd == "root-cli":
                            system(r"bin\_rxvt.exe")
                        elif cmd == "root-tell":
                            system(r"bin\passwd.exe")
                        else:
                            print("Usage: root-[application]")
                    elif cmd == "greed":
                        system(fr"bin\{cmd}.exe")
                    elif cmd.startswith("httping"):
                        system(fr"bin\{cmd}")
                    elif cmd.startswith("locate"):
                        system(fr"bin\{cmd}")
                    
                    
                    elif cmd == "":
                            print()
                            continue
                    else:
                        Tenaya.cannot() 
                
            except KeyboardInterrupt:
                continue
            except TypeError:
                print(error_msg)
            except EOFError:
                continue
    def clear():
        system('cls')
    def cannot():
        print("Sorry! Cannot execute this Command in shell!")
        return True



Tenaya()