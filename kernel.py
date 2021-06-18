from himem import *
from smartdrv import command_line

version = "1.12.4"
author = "Felipe Souza"
license__ = open("LICENSE").read()
changelog = open("CHANGELOG.txt").read()
SubVersionTAGS = "Bug fix: PRE-HIMEM UPDATE"
class mirror:
    def mirror():
        print("This Operational System is hospeded in:")
        print("https://github.com/TenayaOS/OSystem.git (URL Github System)\n")
        system(f'git commit -a -m "{SubVersionTAGS}"')
        system("git push origin main")
    def mirror_pull():
        print("This Operational System is hospeded in:")
        print("https://github.com/Habejota/OSystem.git (URL Github System)\n")
        system("git pull")

system("cls")
system(fr"title OSystem {version}")
system("color 07")
globalEnv = getcwd()             
msys = mirror
forge = None
forge_installed = None
try:
    forge = open(r"Forge\version.txt").read()
except FileNotFoundError:
    pass
else:
    forge_installed = True

class Tenaya:
    def __init__(self):
        Tenaya.welcome()
        Tenaya.command()
    def welcome():
        system("cls")
        print(f"\033[1;37;40mStarting OSystem {version}. . ."), sleep(randint(2, 5))
        print("")
        print("")
        testExtendedMemory(disk_partition)
    def command():
        print("")
        chdir("home")
        print(fr"{command_line}{globalEnv}\smartdrv.py")
        while True:
            try:
                cmd_input: str = input(command_line).strip()  
                def cat_command(cmd):
                    if cmd == "shutdown":
                        Progressbar()
                        return True 
                    elif cmd == "changelog":
                        print(__changelog__)
                    elif cmd == "version":
                        print(version)
                        print(SubVersionTAGS)
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
                            elif cmd == "mirror -s":
                                system("git status")
                            else:
                                print("Use: mirror [args][datas]")
                                print("mirror:")
                                print("  mirror -p: Pull and update code")
                                print("  mirror -s: Print OSystem git status")
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
                         system(fr"{globalEnv}\root\Far\far.exe")
                         system("cls")
                    elif cmd.startswith("edit"):
                         system(fr"{globalEnv}\root\Far\{cmd}")
                         system("cls")
                    elif cmd.startswith("fdisk"):
                        system("diskpart")
                    elif cmd == "osav":
                        system(fr"{globalEnv}\antivirus.exe")
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
                        system("python {}\graphics.py".format(globalEnv))    
                    elif cmd == "connect":
                        system("python {}\connect.py".format(globalEnv))
                    elif cmd == "himem":   
                        himem(disk_partition, port_session)
                    elif cmd == "prompt":
                        prompt_titleWindowBoard: str = input("Prompt wndows title name: ")
                        system(fr"title {prompt_titleWindowBoard}")
                    elif cmd == disk_partition:
                        print(fr"{disk_partition}: this is the disc signature!")
                    elif cmd == "download --mirror":
                        system("git clone https://github.com/Habejota/OSystem.git")
                    elif cmd == "drivers":
                        chdir("..")
                        system(fr"os\root\far\far.exe drive os\home")
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
                    elif cmd == "pwd":
                        print(getcwd())
                    elif cmd.startswith("ping"):
                        system(cmd)
                    elif cmd.startswith("cd"):
                        cmd = cmd.replace("cd ", "")
                        cmd = cmd.replace("cd", "")
                        cmd = cmd.strip()
                        try:
                            chdir(cmd)
                        except OSError:
                            print("bash: {}: Diretory not found".format(cmd))
                        else:
                            pass
                    elif cmd.startswith("mkdir"):
                        cmd = cmd.replace("mkdir", "")
                        cmd = cmd.replace("mkdir ", "")
                        cmd = cmd.strip()
                        try:
                            makedirs(cmd)
                        except:
                            print("Sorry! This diretory already exists!")
                        else:
                            print("Diretory created with sucessfuly!")
                    elif cmd.startswith("rmdir"):
                        cmd = cmd.replace("rmdir", "")
                        cmd = cmd.replace("rmdir ", "")
                        try:
                            removedirs(cmd.strip())
                        except:
                            print("Sorry! This diretory not exists to remove!")
                        else:
                            print("Diretory removed with sucessfuly")
                    elif cmd == "ls" or cmd == "dir":
                        print(getcwd())
                        dirs = listdir()
                        for file in dirs:
                            print(file)
                    elif cmd.startswith("python"):
                        system(fr"{globalEnv}\root\{cmd}")
                    elif cmd == "status":
                        system("git status")
                    elif cmd == "branch":
                        print("OSystem {}".format(version))
                        print("Github Repository: https://github.com/Habejota/OSystem")
                        print("Code Page Informations: ")
                        print("")
                        print("     To see if have updates on github that you dont have ")
                        print("installed on your computer, but is loaded in Github, dont use")
                        print("mirror inside other git repositories or forge folder 'cause")
                        print("found OSError in OSystem git and others code!")
                        
                    
                    
                    
                    elif cmd == "help":
                        print("shutdown        changelog        version")
                        print("source          disk             clear")
                        print("ifconfig        hostname         echo")
                        print("mirror          command          mem")
                        print("license         banner           winget")
                        print("far             edit             fdisk")
                        print("osav            roaming          forge")
                        print("pwd             ping             help")
                        print("assing          graphics         connect")
                        print("drivers         himem            label")
                        print("prompt          cd               mkdir")
                        print("rmdir           dir              branch")
                        print("status           ")
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
