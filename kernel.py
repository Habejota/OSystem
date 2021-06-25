# Importing Kernel Python modules
from os import system, getcwd, chdir # Importing "os" module to: execute system functions, get path, entry in dir
from time import sleep # Get a system delay
from socket import gethostname, gethostbyname # Importing "socket" module: Get host name and get IP machine
from random import randint # Get randomic [Numbers and Choices]
import glob, socket # Import all from "glob" and "socket"

# Path definitions
chdir("os") # Entry in operational bash system folder of >>>0x800-1x300<<<
path = getcwd() # Save actually path
chdir("home") # Entry in user home folder

# Machine network informations
hostname = gethostname() # Get host name
ifconfig = gethostbyname(hostname) # Get machine Ip

# Disk patition on OSystem being installed
disk_partition = "0x800-1x300" # Disk Partition
port_session = randint(500, 65535) # Session Port

print("┌────────────────────────────────────────────────────────────────────┐")
print("│Welcome to OSystem v1.13 - Native Osystem Kernel modules            │")
print("│OSystem: https://github.com/Habejota/OSystem.git                    │")
print("│                                                                    │")
print("└───────────────────────────[OSystem Bash]───────────────────────────┘")
system(fr"{path}\bin\bash.exe") 
