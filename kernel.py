# Import Python modules
from os import system, getcwd, chdir, makedirs, startfile, removedirs, listdir, rename
from time import sleep
from socket import gethostname, gethostbyname
from random import randint
import glob, socket
from version import *

# Define PATH and evorronmenttry:
path = getcwd()

# Cyngwin Drivers
try:
    chdir("os")
except:
    pass
else:
    pass


# Global WMEMORY
hostname = gethostname()
ifconfig = gethostbyname(hostname)
port_session = randint(500, 65535)
disk_partition = "0x800-1x300"

# Path go to user folder
chdir("honm")

# Terminal Bash
print("===================================================")
print("Welcome to OSystem v{} - {}".format(version, SubVersionTAGS))
print("OSystem: https://github.com/Habejota/OSystem.git")
print("")
print("==================[OSystem Bash]===================")
system(fr"{path}\os\bin\bash.exe")