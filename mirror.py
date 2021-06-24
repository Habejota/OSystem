from version import *
from os import system
from kernel import *
chdir("..")
print("This Operational System is hospeded in:")
print("https://github.com/TenayaOS/OSystem.git (URL Github System)\n")
system(fr'{path}\bin\git commit -a -m "{SubVersionTAGS}"')
system(fr"{path}\bin\git push origin main")
print(fr'{path}\bin\git commit -a -m "{SubVersionTAGS}"')
print(fr"{path}\bin\git push origin main")