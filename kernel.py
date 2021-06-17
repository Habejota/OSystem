from os import system, getcwd, chdir, makedirs, startfile
from time import sleep
from socket import gethostname, gethostbyname
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

system("cls")
system(fr"PATH=%path%;{getcwd()}\root")
system("title OSystem {}".format(__version__))
system("color 07")

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
                    
msys = mirror
correct_simbol = ["✔", "✘"]
forge = None
forge_installed = None
hostname = gethostname()
ifconfig = gethostbyname(hostname)
distibuition = fr"OSystem Distuibuition {__version__}" 
source = fr"https://github.com/Habejota/OSystem (Free Source Code)"
language = fr"Englesh (United States of America"
disk_partition = "0x800-1x300"
start_msg = fr"""Installed PS/2 port.
Readed and Loaded files in: ({disk_partition})

┌───────────────────────────────────────────────────────────────────────┐
│                     ∙OSystem Dostribuition 1.12∙                      │
│        (TENAYA CONTROL, Interatives Interfaces with USB Ports)        │
│                                                                       │
│ ➤ Your DISPLAY is set to 192.168.0.104:0.0                            │
│ ➤ For use beta version use This git repo use git branch: (beta)       │
│ ➤ This is OSystem version oficial:                                    │          
│                                                                       │
│ ∙ Important:                                                          │
│ This Software is based in Linux/UNIX Operational Systems, You         │
│ have a applications and a varietes of Tools. The Free source code     │
│ being in: (https://github.com/Habejota/OSystem), You can see          │
│ informations and codes, distribuitions and new updates and versions.  │
└───────────────────────────────────────────────────────────────────────┘
"""
try:
    forge = open(r"Forge\version.txt").read()
except FileNotFoundError:
    pass
else:
    forge_installed = True

class Tenaya:
    def __init__(self):
        self.prompt = "\033[32m$\033[m "
        Tenaya.welcome()
        Tenaya.command()
    def welcome():
        system("cls")
        print(start_msg)
        if forge == None:
            pass
        else:
            print(forge)
            
    def command():
        for i in range(0, 6):
            beep()
        while True:
            try:
                cmd_input: str = input("\033[32m$\033[m ").strip()  
                def cat_command(cmd):
                    if cmd == "shutdown":
                        Progressbar()
                        return True 
                    elif cmd == "changelog":
                        print(__changelog__)
                    elif cmd == "version":
                        print(__version__)
                    elif cmd == "source":
                        print(source)
                    elif cmd == "disk":
                        print(disk_partition)
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

                        python(cmd)
                    elif cmd.startswith("echo"):
                        cmd = cmd.replace("echo ", "")
                        cmd = cmd.replace("echo",  "")
                        if cmd == "":
                            print("Echo driver is loaded in memory {}".format(disk_partition))
                        else:
                            print(cmd)
                    elif cmd.startswith("mirror"):
                            if cmd == "mirror":
                                msys.mirror()
                            elif cmd == "mirror -p":
                                msys.mirror_pull()
                            else:
                                print("Use: mirror [args][datas]")
                                print("mirror:")
                                print("  mirror -p: Pull and update code")
                    elif cmd == "command":
                        Tenaya.welcome()
                        Tenaya.command()
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
                            system(fr"root\banner.exe {cmd}")
                    elif cmd.startswith("winget"):
                        if cmd == "winget install --update":
                            startfile("root\winget.appxbundle")
                        else:
                            system(cmd)
                    elif cmd == "far":
                         system(fr"root\far\far.exe")
                    elif cmd == "edit":
                        system(fr"root\far\edit.exe")
                    elif cmd.startswith("fdisk"):
                        system("diskpart")
                    elif cmd == "osav":
                        system(fr"antivirus.exe")
                    elif cmd == "label":
                        system("label")
                    elif cmd == "kernel":
                        if main_function() == True:
                            system("cls")
                            print("Kernel is building in 0x800-1x300. . .")
                            Progressbar()
                            chdir("..")
                            system("boot.exe")
                            return True
                    elif cmd == "assing":
                        print("Drive:                  Assing:            Partition:")
                        print("-------------           ---------------    ---------------")
                        print("System Hard disk        C9-D3-8D-23-9D     0x800-1x300")
                        print("CD-Rom Drive            DS-K9-X7-11-3D     0x800-2x300")
                    elif cmd == "graphics":    
                        system("python graphics.py")    
                    elif cmd == "connect":
                        system("python connect.py")
                    elif cmd == "himem":    
                        system("python himem.py")
                        
                        
                    elif cmd == "drivers":
                        chdir("..")
                        system(fr"os\root\far\far.exe drive os")
                        chdir("os")            
                    elif cmd == "roaming":
                        Progressbar()
                        print("Network driver is update!")
                    elif cmd.startswith("forge"):
                        if cmd == "forge --install":
                            print("Searching last versions of forge. . ."), sleep(1.983)
                            print("\nDownload Started. . .")
                            system("git clone https://github.com/Habejota/Forge.git")
                            Progressbar()
                            print("\n\nForge installed with sucess!")
                            print("Is required reboot to apply updates!")
                            input("Press ENTER to shutdown SYSTEM. . .")
                            return True
                        elif cmd == "forge --update":
                            try:
                                chdir("Forge")
                            except FileNotFoundError:
                                print("Try first install Forge!")
                            else:
                                system("git pull")
                                print("System will reboot. . ."), sleep(1.276)
                                return True
                                
                        else:
                            if forge == None:
                                print("You dont have FORGE installed!")
                            else:
                                print("OSystem Forge:")
                                print(forge)
                    elif cmd == "chdir":
                        print(getcwd())
                    elif cmd.startswith("ping"):
                        system(cmd)
                    elif cmd == "help":
                        print("shutdown        changelog        version")
                        print("source          disk             clear")
                        print("ifconfig        hostname         echo")
                        print("mirror          command          mem")
                        print("license         banner           winget")
                        print("far             edit             fdisk")
                        print("osav            roaming          forge")
                        print("chdir           ping             help")
                        print("assing          graphics         connect")
                        print("mirror          command          label")
                        print("drivers         himem")
                    elif cmd == "":
                        print()
                    else:
                        if forge_installed == None:
                            print("Sorry! Cannot execute this Command in shell!") 
                        elif forge_installed == True:
                            print("FORGE: {} Invalid Command or Package name!".format(cmd))                
                
                if forge_installed == True:
                    try:
                        scr_file = open(fr"Forge\packs\{cmd_input}.py")
                    except FileNotFoundError:
                        s = cat_command(cmd_input)
                        if s == True:
                            break
                        elif s == "REBOOT":
                            chdir("..")
                            system("boot.exe")
                            break
                        else:
                            continue
                    else:
                        print(fr"{cmd_input}: Is starting. . .")
                        system(fr"python Forge\packs\{cmd_input}.py")
                else:
                        s = cat_command(cmd_input)
                        if s == True:
                            break
                        elif s == "REBOOT":
                            chdir("..")
                            system("boot.exe")
                            break
                        else:
                            continue
            except KeyboardInterrupt:
                chdir("..")
                system("boot.exe")
                break
            except TypeError:
                print("Sorry! This is a internal error in main code!")
            except EOFError:
                continue
    def clear():
        system('cls')


try:
    if startShellKernelSetting == True:
        input("")
        Tenaya()
    else:
        system("cls")
        print(""), sleep(3.968)
        system("color 17")
        print("Kernel Python modules isn't installed!")
        input("Kernel Setup will install dependences in your computer\nPress ENTER to install tqdm. . .")
        system("pip install tqdm")
        chdir("..")
        system("color 07")
        system("boot.exe")
except KeyboardInterrupt:
    chdir("..")
    system("boot.exe")