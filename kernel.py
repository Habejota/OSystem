# Importing Kernel Python modules
from os import system, getcwd, chdir
from socket import gethostname, gethostbyname

# Directory definitions
chdir("os")
path = getcwd()
chdir("home")

class Kernel:
    def __init__(self):
        self.hostname = gethostname()
        self.host = gethostbyname(self.hostname)
        self.disk_partition = "0x800-1x300"
        
        self.PrintFirmwareSettings()
        print("┌────────────────────────────────────────────────────────────────────┐")
        print("│Welcome to OSystem v1.13 - Compile Source Code Firmware             │")
        print("│OSystem: https://github.com/Habejota/OSystem.git                    │")
        print("│                                                                    │")
        print("│                 GNU\Bash OSystem Free Source Code                  │")
        print("│        Source library free code Firmware Apache License 2.0        │")
        print("│            Binary Systems auto-compiled in scr/builtdin            │")
        print("└───────────────────────────[OSystem Bash]───────────────────────────┘")
        system(r"{}\bin\bash.exe".format(path))
    def PrintFirmwareSettings(self):
        print("")
        system("echo Configurations firmware (%username%@{}) ({}:80)".format(self.hostname, self.host))
        
Kernel()