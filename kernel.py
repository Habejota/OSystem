# Import Python modules
from os import system, getcwd, chdir, makedirs, startfile, removedirs, listdir, rename
from time import sleep
from socket import gethostname, gethostbyname
from random import randint
import glob, socket

# define PATH and evorronment:
path = getcwd()

# Cyngwin Drivers
try:
    chdir("os")
except:
    pass
else:
    pass

# Machine network informations
hostname = gethostname() # Get host name
ifconfig = gethostbyname(hostname) # Get machine Ip

# Disk patition on OSystem being installed
disk_partition = "0x800-1x300" # Disk Partition
port_session = randint(500, 65535) # Session Port

# Path go to user folder
chdir("home")

# Terminal Bash
print("") # A broken line
print("┌────────────────────────────────────────────────────────────────────┐") # Terminal desainer
print("│Welcome to OSystem v1.12.8 - Command Update: Bug fix                │") # Version Informations
print("│OSystem: https://github.com/Habejota/OSystem.git                    │") # Source code
print("│                                                                    │")
print("└───────────────────────────[OSystem Bash]───────────────────────────┘") # Terminal desaine
system(fr"{path}\os\bin\bash.exe")
