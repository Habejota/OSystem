from os import system, chdir
import sys
from kernel import path

chdir("..")

class Package:
    def __init__(self, cmd):
        try:
            command = cmd[0]
            arguments = cmd[1]
        except:
            print("""                         
            Usage: apt [options] command

            list - list packages based on package names
            search - search in package descriptions
            install - install packages
            update - update list of packages
            upgrade - update OSystem
            """) 
        else:
            if arguments == "install":
                try:
                    package = cmd[2]
                except:
                    print("Shell: Insert package name!")
                else:
                    self.install(package.lower())
            elif arguments == "update" or "upgrade":
                system(r"bin\git pull")
                system(r"bin\git fetch")
            elif arguments == "search":
                try:
                    package = cmd[2]
                except:
                    print("Shell: Insert package name!")
                else:
                    self.search(package)

    def install(self, pack_name):
        a = pack_name
        system(r"bin\git clone https://github.com/Habejota/{}.git ".format(pack_name))
        try:
            bache = open(fr"{a}\{a}.exe", "rb")
            bache.close()
        except Exception as e:
            print("Shell: Fail to install Packages!")
            print(e)
        else:
            system(fr"move {a}\{a}.exe etc\profile.d")
            system(fr"RD/s/q {a}")
            bache = open(r"etc\profile.d\git-prompt.sh",  "a+")
            bache.write(f'\nalias {a}="/etc/profile.d/{a}.exe"')
            print("Shell: Package installed with sucessfuly!")
            print("To apply the new package restart the bash")
    def search(self, pack_name):
        print("Package Name:                    Tag:")
        print("──────────────────────────────────────────────────────────────")
        if pack_name == "kernel":
            print("Kernel Source                    Kernel")    
        elif pack_name == "Console" or pack_name == "Application" or pack_name == "Tardis":
            print("Tardis Console Application        TardisProject")

        else:
            print("Nothink Packages match with {}".format(pack_name))
Package(sys.argv)

