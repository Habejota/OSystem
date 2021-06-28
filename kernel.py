# Importing Kernel Python modules
from os import system, getcwd, chdir
from socket import gethostname, gethostbyname
from time import sleep

# Directory definitions
chdir("os")
path = getcwd()
chdir("home")

class Kernel:
    def __init__(self):
        self.hostname = gethostname()
        self.host = gethostbyname(self.hostname)
        self.disk_partition = "0x800-1x300"
        self.version = "Command Objectives"

        self.FetchUpdates()
        self.PrintFirmwareSettings()
        self._init__mensage()  
        system(r"{}\bin\bash.exe".format(path))
    def _init__mensage(self):
        print("┌────────────────────────────────────────────────────────────────────┐")
        print("│Welcome to OSystem v1.13 - QuickBasic Update                        │")
        print("│OSystem: https://github.com/Habejota/OSystem.git                    │")
        print("│                                                                    │")
        print("│                 GNU\Bash OSystem Free Source Code                  │")
        print("│        Source library free code Firmware Apache License 2.0        │")
        print("│            Binary Systems auto-compiled in scr/builtdin            │")
        print("└───────────────────────────[OSystem Bash]───────────────────────────┘")
    def PrintFirmwareSettings(self):
        print("")
        system("echo Configurations firmware (%username%@{}) ({}:80)".format(self.hostname, self.host))
    def FetchUpdates(self):
        system(fr"{path}\bin\git.exe pull")


Kernel()