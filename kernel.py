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
        self.version = "2.0"
        self.subversion = "OSystem Distribuition: version-2.0"
        
        system("cls")
        self.changelog()
        system(r"{}\bin\bash.exe".format(path))
    def changelog(self):
        print(f"Welcome to \033[32mOSystem {self.version}\033[m (GNU\Linux - {self.subversion})")
        print("")
        print(" * Documentation:  \033[4mhttps://github.com/Habejota/OSystem/blob/main/docs.txt\033[0m")
        print(" * Support:        \033[4mmailto:kiudokima@gmail.com\033[0m")
        print(" * Management:     \033[4mhttps://github.com/Habejota/OSystem\033[0m")
        print("")
        print("  Ethernet WebSocket Setting:")
        print("   IPv6 address for eth4:  2001:0:2877:7aa:14d1:e090:7cff:c309")
        print(f"   IPv4 address for wifi0: \033[31m{self.host}\033[m: \033[35m{self.hostname}\033[m")
        print("")
        print(f"Operational System: \033[33mWindows NT\033[m")
        print("Disks Firmware Devices Status on:")
        print(f"     PS/1:  \033[33mWindows NT\033[m")
        print(f"     PS/2:  \033[32mOSystem {self.version}\033[m")
        print("\033[36m=======================================\033[38m[\033[34mOSystem Bash\033[m\033[36m]=================================\033[m")
    
Kernel()
