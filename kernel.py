from os import system, getcwd, chdir
from time import sleep
from socket import gethostname, gethostbyname
from random import randint
import glob, socket

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
print("│Welcome to OSystem v1.12.8 - Update Other Modules                   │")
print("│OSystem: https://github.com/Habejota/OSystem.git                    │")
print("│                                                                    │")
print("└───────────────────────────[OSystem Bash]───────────────────────────┘")
system(fr"{path}\bin\bash.exe")
