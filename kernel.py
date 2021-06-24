# Import Python modules
from os import system, getcwd, chdir, makedirs, startfile, removedirs, listdir, rename
from time import sleep
from socket import gethostname, gethostbyname
from random import randint
import glob, socket

# Define PATH and evorronment:
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
version = "1.12.8" # OSystem version
SubVersionTAGS = "Found Systems" # SubVersion Tag

# Path go to user folder
chdir("home")
 
# Terminal Bash
print("") # A broken line
print("===================================================") # Terminal desainer
print("Welcome to OSystem v{} - {}".format(version, SubVersionTAGS)) # Version Informations
print("OSystem: https://github.com/Habejota/OSystem.git") # Source code
print("")
print("==================[OSystem Bash]===================") # Terminal desaine
try:
    system(fr"{path}\os\bin\bash.exe")
except KeyboardInterrupt:
    chdir(path)
    chdir("..")
    system("Executer.exe")
    exit()
# End of code kernel