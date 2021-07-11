# Importing Kernel Python modules
from os import system, getcwd, chdir
from socket import gethostname, gethostbyname
from time import sleep

# Directory definitions
path = getcwd()
class Kernel:
    def __init__(self):
        self.hostname = gethostname()
        self.host = gethostbyname(self.hostname)
        self.disk_partition = "0x800-1x300"
        self.version = "1.13"
        self.subversion = "Terminal Update: Linux be near... I can hear You"

        self.PrintFirmwareSettings()
        try:
            self.changelog() 
        except KeyboardInterrupt:
            system("python Firmware.py")
        else:
            system(r"{}\bin\bash.exe".format(path))
    def changelog(self):
        print(f"""==================================================================
Welcome to OSystem {self.version} (GNU\Linux - {self.subversion})

 * Documentation:  https://github.com/Habejota/OSystem/blob/main/docs.txt
 * Management:     https://github.com/Habejota/OSystem
 * Support:        https://github.com/Felipe-Souza-Pereira-Lima (mailto:kiudokima@gmail.com)
  
  Ethernet WebSocket Setting:
  IPv6 address for eth4:  2001:0:2877:7aa:14d1:e090:7cff:c309
  IPv4 address for wifi0: {self.host}: {self.hostname}

OS Installed at PS/1: \033[33mWindows NT\033[m
Disks Firmware devices status:
    PS/1:  \033[33mWindows NT\033[m
    PS/2:  \033[32mOSystem {self.version}\033[m
    PS/3:  \033[36mOSystem Resources\033[m
""")
        system(rf"{path}\bin\git.exe status")
    def PrintFirmwareSettings(self):
        print("")
        system("echo Configurations firmware (%username%@{}) ({}:80)".format(self.hostname, self.host))

try:    
    chdir("home")
except FileNotFoundError:
    pass
else:
    try:
        Kernel()
    except KeyboardInterrupt:
        chdir(path)
        chdir("..")
        system("python network.py")
        exit()
