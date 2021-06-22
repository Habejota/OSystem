# Importing modules
from himem import *
import shutil

# Global Evorronment
chdir("os")
globalEnv = getcwd()  

# Informations of Version
version = "1.12.6"
author = "Felipe Souza"
license__ = open("LICENSE").read()
SubVersionTAGS = "Compatibilit TenayaOS" # SubVersion Tag

# Mirror Functions
class mirror:
    def mirror():
        print("This Operational System is hospeded in:")
        print("https://github.com/TenayaOS/OSystem.git (URL Github System)\n")
        system(fr'{globalEnv}\bin\git commit -a -m "{SubVersionTAGS}"')
        system("git push origin main")
    def mirror_pull():
        print("This Operational System is hospeded in:")
        print("https://github.com/Habejota/OSystem.git (URL Github System)\n")
        system(f"{globalEnv}\bin\git pull")

# Start Definitions
chdir("home")
system("cls")
system(fr"title OSystem {version}")
system("color 07")

# local variables           
msys = mirror
forge = None
forge_installed = None

# Verify if FORGE is installed
try:
    forge = open(fr"{globalEnv}\Forge\version.txt").read()
except FileNotFoundError:
    pass
else:
    forge_installed = True

# Kernel Object
class Tenaya: # Main class
    # Kenel Starter
    def __init__(self):
        Tenaya.welcome() # Execute initial mensage
        Tenaya.command() # Start Kernel shell
    
    # Kernel welcome mensage
    def welcome():
        print("Installed at PS/2 port!")
        print("     Tasks: \033[37m/kernel.py /usr/bin/bash.exe ")
        print("     Kernel Device controller SATA[1]")
        print(f"\033[1;37;40mStarting OSystem {version}. . ."), sleep(randint(2, 5))
        print("")
        print("")
        testExtendedMemory(disk_partition) # Test himem
        
    # Kernel Shell
    def command():
        print("") # Add a broken line
        
        # Start forge if be installed
        if forge_installed == True:
            print(forge)
        
        command_line = f"\033[35m[\033[32m~\033[35m]\033[m " # Define Commandline
        print(fr"{command_line}{globalEnv}\bin\smartdrv.py") # Execute smart drive
        # Select Osystem Shell or UNIX Bash
        try: # Timeout setup
            sleep(2) # Wait three seconds to select shell/bash
        except KeyboardInterrupt: # Start in selected Main Bash
            system(fr"{globalEnv}\bin\bash.exe") # Starts with UNIX Bash
        else: # OSystem shell
            # Kernel Shell interpret
            while True:
                try:
                    cmd_input: str = input(command_line).strip()  
                    def cat_command(cmd):
                        # Shutdown function
                        if cmd.startswith("shutdown"):
                            if cmd == "shutdown":
                                Progressbar()
                                return True 
                            elif cmd == "shutdown -c":
                                system("shutdown -s")
                        # Version installed
                        elif cmd == "version":
                            print(version)
                            print(SubVersionTAGS)
                        # Git source repository
                        elif cmd == "source":
                            print(source)
                        # Disk partition of room
                        elif cmd == "disk":
                            print(disk_partition)
                        # Clear display comand
                        elif cmd == "clear" or cmd == "cls":
                            system("cls")
                        # Print codec of network setting up
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
                        # Print host name
                        elif cmd == "hostname":
                            print(f"Hostname: {hostname}")
                        # Echo driver
                        elif cmd.startswith("echo"):
                            cmd = cmd.replace("echo ", "")
                            cmd = cmd.replace("echo",  "")
                            if cmd == "":
                                print("Echo driver is loaded in memory {}".format(disk_partition))
                            else:
                                print(cmd)
                        # Mirror function
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
                        # Command Function
                        elif cmd == "command":
                            Tenaya.welcome()
                            Tenaya.command()
                        # Print license
                        elif cmd == "license":
                                print(license__)
                        # Banner
                        elif cmd.startswith("banner"):
                                cmd = cmd.replace("banner",  "")
                                cmd = cmd.replace("banner ", "")
                                system(fr"{globalEnv}\usr\bin\banner.exe {cmd}")
                        # Windows Package Manager "WINGET"
                        elif cmd.startswith("winget"):
                            if cmd == "winget install --update":
                                startfile("usr\bin\winget.appxbundle")
                            else:
                                system(cmd)
                        # Far Commander
                        elif cmd == "far":
                             system(fr"{globalEnv}\usr\bin\Far\far.exe")
                             system("cls")
                        # Edit-or Application
                        elif cmd.startswith("edit"):
                             system(fr"{globalEnv}\usr\bin\Far\{cmd}")
                             system("cls")
                        # Disk partition Manager
                        elif cmd.startswith("fdisk"):
                            system("diskpart")
                        # Label disk set up
                        elif cmd == "label":
                            system("label")
                        # Assingments of disk Bootloader
                        elif cmd == "assing":
                            print("Drive:                  Assing:            Partition:")
                            print("-------------           ---------------    ---------------")
                            print("System Hard disk        C9-D3-8D-23-9D     0x800-1x300")
                            print("CD-Rom Drive            DS-K9-X7-11-3D     0x800-2x300")
                        # Graphics function
                        elif cmd == "graphics":    
                            system(r"python {}\bin\graphics.py".format(globalEnv))    
                        # Connect function
                        elif cmd == "connect":
                            system(r"python {}\bin\connect.py".format(globalEnv))
                        # Reboot himem
                        elif cmd == "himem":   
                            himem(disk_partition, port_session)
                        # Rename title window head
                        elif cmd == "prompt":
                            prompt_titleWindowBoard: str = input("Prompt wndows title name: ")
                            system(fr"title {prompt_titleWindowBoard}")
                        # Verify disk
                        elif cmd == disk_partition:
                            print(fr"{disk_partition}: this is the disc signature!")
                        # Open dirs pagination
                        elif cmd == "drivers":
                            chdir(globalEnv)
                            system(fr"{globalEnv}\usr\bin\Far\far.exe home")    
                        # Update network driver
                        elif cmd == "roaming":
                            Progressbar()
                            print("Network driver is update!")
                        # Forge function
                        elif cmd.startswith("forge"):
                            if cmd == "forge --install":
                                print("Searching last versions of forge. . ."), sleep(1.983)
                                print("\nDownload Started. . .")
                                chdir(globalEnv)
                                system("git clone https://github.com/Habejota/Forge.git")
                                Progressbar()
                                print("\n\nForge installed with sucess!")
                                print("Is required reboot to apply updates!")
                                input("Press ENTER to shutdown SYSTEM. . .")
                                return True
                            elif cmd == "forge --update":
                                try:
                                    chdir(globalEnv)
                                    chdir("Forge")
                                except FileNotFoundError:
                                    print("Try first install Forge to update him!")
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
                        # Path window diretory
                        elif cmd == "pwd":
                            print(getcwd())
                        # Ping main function
                        elif cmd.startswith("ping"):
                            system(cmd)
                        # Cingwin Drive
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
                        # Make dirs
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
                        # Remove dirs
                        elif cmd.startswith("rmdir"):
                            cmd = cmd.replace("rmdir", "")
                            cmd = cmd.replace("rmdir ", "")
                            try:
                                removedirs(cmd.strip())
                            except:
                                print("Sorry! This diretory not exists to remove!")
                            else:
                                print("Diretory removed with sucessfuly")
                        # list dirs and objects
                        elif cmd == "ls" or cmd == "dir":
                            dirs = listdir()
                            for file in dirs:
                                print(file)
                        # Status of installed
                        elif cmd == "status":
                            system("git status")
                        # Code Pages Informations
                        elif cmd == "branch" or cmd == "cpi":
                            print("OSystem {}".format(version))
                            print("Github Repository: https://github.com/Habejota/OSystem")
                            print("Code Page Informations: ")
                            print("")
                            print("     To see if have updates on github that you dont have ")
                            print("installed on your computer, but is loaded in Github, dont use")
                            print("mirror inside other git repositories or forge folder 'cause")
                            print("found OSError in OSystem git and others code!")
                        # Port settings
                        elif cmd == "port":
                            print("  OSystem System Pagination format Disk Partition:")
                            print(fr"  {ifconfig}@{hostname}: {port_session}")
                        # Executable Packages
                        elif cmd.endswith(".exe"):
                            try:
                                startfile(cmd)
                            except FileNotFoundError:
                                print("Sorry! Cannot Execute this Executable Package")
                            else:
                                print("It's Amazing! The {} Executable Package was started!".format(cmd))
                        # Binary Packages
                        elif cmd.endswith(".lib"):
                            try:
                                open(cmd)
                            except:
                                print("This System Package is invalid!")
                            else:
                                system(fr"{globalEnv}\usr\bin\lua.exe {cmd}")
                        # Lua module
                        elif cmd == "lib":
                            system(r"{}\usr\bin\lua.exe".format(globalEnv))
                        # Binary Luarocks
                        elif cmd.startswith("luarocks"):
                            system(fr"{globalEnv}\usr\bin\{cmd}")
                        # Print display setup
                        elif cmd == "display":
                            print("=============================")
                            print("OSystem Display Configuration")
                            print("Hostpot: {192.168.1.1:0000}")
                            print("=============================")
                        # Print Engine Configuration
                        elif cmd == "engine":
                            print("OSystem Engine Device")
                            print("====================================")
                            print("Engine System Controller:")
                            print("SATA1: C9-D3-8D-23-9D")
                            print("SATA2: {}".format(disk_partition))
                            print("====================================")
                            print("")
                            print("Main kernel Library System")
                            print("iExecuter System Function Packages")
                        # All updates managed
                        elif cmd == "supdate":
                            print("All versions update:")
                            print("")
                            print("MIRROR Update")
                            print("Kernel Update")
                            print("Socket Update")
                            print("Desktop Update")
                            print("HIMEM Update")
                            print("Evorronment Update")
                            print("Engine Update")
                            print("Console Update")
                        # Executer shell script
                        elif cmd.endswith(".sh") and cmd.startswith("./"):
                            cmd = cmd.replace("./", "")
                            system(rf"{globalEnv}\bin\bash.exe {cmd}")
                        # Nano edit-or
                        elif cmd.startswith("nano"):
                            system(fr"{globalEnv}\usr\bin\{cmd}")
                        # Bash
                        elif cmd == "bash":
                            system(fr"{globalEnv}\bin\bash.exe")
                        # Print Date 
                        elif cmd == "date":
                            system(fr"{globalEnv}\usr\bin\date.exe")
                                                
                        
                        
                        # Print help
                        elif cmd == "help":
                            print(f"OSystem v{version} - Command List:")
                            print("=============================================")
                            print("shutdown        display          version")
                            print("source          disk             clear")
                            print("ifconfig        hostname         echo")
                            print("mirror          command          engine")
                            print("license         banner           winget")
                            print("far             edit             fdisk")
                            print("supdate         roaming          forge")
                            print("pwd             ping             help")
                            print("assing          graphics         connect")
                            print("drivers         himem            label")
                            print("prompt          cd               mkdir")
                            print("rmdir           dir              branch")
                            print("status          port             cpi")
                            print("lib             luarocks         nano")
                            print("bash            date")
                            print("=============================================")
                        # Broken up lines
                        elif cmd == "":
                            print()
                        # Unknow command
                        else:
                            try:
                                sxtp_fudido = open(fr"{globalEnv}\usr\bin\{cmd}", "rb")
                            except FileNotFoundError:
                                if forge_installed == None:
                                    print("Sorry! Cannot execute this Command in shell!") 
                                elif forge_installed == True:
                                    print("FORGE: {} Invalid Command or Package name!".format(cmd))                
                            else:
                                system(fr"{globalEnv}\usr\bin\{cmd}")
                    # If forge is installed
                    if forge_installed == True:
                        try:
                            scr_file = open(fr"Forge\packs\{cmd_input}.py")
                        except FileNotFoundError:
                            s = cat_command(cmd_input)
                            if s == True:
                                break
                            elif s == "REBOOT":
                                chdir(globalEnv)
                                chdir("..")
                                system("Execute.exe")
                                break
                            else:
                                continue
                        else:
                            print(fr"{cmd_input}: Is starting. . .")
                            system(fr"python Forge\packs\{cmd_input}.py")
                    # Else not installed
                    else:
                            s = cat_command(cmd_input)
                            if s == True:
                                break
                            elif s == "REBOOT":
                                chdir("..")
                                system("Exe.exe")
                                break
                            else:
                                continue
                # Except KeyboardInterrupt
                except KeyboardInterrupt:
                    chdir(globalEnv)
                    chdir("..")
                    system("Executer.exe")
                    break
                # Other exceptions
                except TypeError:
                    print("Sorry! This is a internal error in main code!")
                except EOFError:
                    continue
        
# Startup Kernel
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
            system("Executer.exe")
except KeyboardInterrupt:
    chdir("..")
    chdir("..")
    system("Executer.exe")