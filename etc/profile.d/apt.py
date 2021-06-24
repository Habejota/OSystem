from os import system, chdir
import sys

chdir(fr"..")
chdir(fr"etc/profile.d")

try:
    program = sys.argv[0]
except:
    program = None
else:
    pass
try:
    parameter = sys.argv[1]
except:
    parameter = None
else:
    pass
try:
    pkg_name = sys.argv[2]
except:
    parameter = None
else:
    pass

if parameter == None or pkg_name == None:
    print("BASH: apt [parameters](packageName)")
    print("    install     Install packages")
    print("    ")
elif parameter == "install":
    if pkg_name is not None:
        system("git clone https://github.com/Habejota/{}.git".format(pkg_name))
        try:
            a = open(f"{pkg_name}\main.py")
        except FileNotFoundError:
            installed = False
        else:  
            installed = True
        if installed == True:
            with open("git-prompt.sh")
            init.write(f'alias {pkg_name}="/etc/profile.d/{pkg_name}/main.py"')
            print("Package installed with sucessfuly!")
        else:
            print("Cannot install this package!")
    else:
        print("INSERT PACKAGE NAME!")