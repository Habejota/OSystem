from version import *
from os import system

print("This Operational System is hospeded in:")
print("https://github.com/TenayaOS/OSystem.git (URL Github System)\n")
system(fr'{globalEnv}\bin\git commit -a -m "{SubVersionTAGS}"')
system("git push origin main")