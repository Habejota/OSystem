# Importing Kernel Python modules
from os import system, getcwd, chdir
from socket import gethostname, gethostbyname
from time import sleep

# Directory definitions
path = getcwd()
chdir("home")

class Kernel:
    def __init__(self):
        self.hostname = gethostname()
        self.host = gethostbyname(self.hostname)
        self.disk_partition = "0x800-1x300"

        self.FetchUpdates()
        self.PrintFirmwareSettings()
        try:
            self.changelog() 
        except KeyboardInterrupt:
            system("python Firmware.py")
        else:
            system(r"{}\bin\bash.exe".format(path))
    def changelog(self):
        print("┌────────────────────────────────────────────────────────────────────┐"), sleep(0.111)
        print("│Welcome to OSystem v1.13 - Terminal Update: IronPython Language     │"), sleep(0.111)
        print("│OSystem: https://github.com/Habejota/OSystem.git                    │"), sleep(0.111)
        print("│                                                                    │"), sleep(0.111)
        print("│                 GNU\Bash OSystem Free Source Code                  │"), sleep(0.111)
        print("│        Source library free code Firmware Apache License 2.0        │"), sleep(0.111)
        print("│            Binary Systems auto-compiled in scr/builtdin            │"), sleep(0.111)
        print("│               Advanced Compiled Buffer Pagination                  │")
        print("└───────────────────────────[OSystem Bash]───────────────────────────┘\n"), sleep(0.111)
    def PrintFirmwareSettings(self):
        print("")
        system("echo Configurations firmware (%username%@{}) ({}:80)".format(self.hostname, self.host))
    def FetchUpdates(self):
        system(fr"{path}\bin\git.exe pull")


try:
    Kernel()
except KeyboardInterrupt:
    chdir(path)
    chdir("..")
    system("python network.py")
    exit()
