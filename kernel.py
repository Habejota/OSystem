# Importing Kernel Python modules
from os import system, getcwd, chdir
from socket import gethostname, gethostbyname

# Directory definitions
chdir("os")
path = getcwd()
chdir("home")

class Kernel:
    def __init__(self):
        # Global values
        self.hostname = gethostname()
        self.ifconfig = gethostbyname(self.hostname)
        self.disk_partition = "0x800-1x300"

        # Nactive kernel started bash
        self.__init_mensage()
        self.execBash()
    def __init_mensage(self):
        print("┌────────────────────────────────────────────────────────────────────┐")
        print("│Welcome to OSystem v1.13 - Opossite Position Texts                  │")
        print("│OSystem: https://github.com/Habejota/OSystem.git                    │")
        print("│                                                                    │")
        print("│                 GNU\Bash OSystem Free Source Code                  │")
        print("│        Source library free code Firmware Apache License 2.0        │")
        print("│            Binary Systems auto-compiled in scr/builtdin            │")
        print("└───────────────────────────[OSystem Bash]───────────────────────────┘")
    def execBash(self):
        system(fr"{path}\bin\bash.exe")


Kernel()