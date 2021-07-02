from os import system, chdir
import sys

chdir(fr"..")
chdir(fr"etc/profile.d")

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
            """) 
        else:
            if arguments == "install":
                try:
                    package = cmd[2]
                except:
                    print("Shell: Insert package name!")
                else:
                    self.install(package.lower())
            elif arguments == "search":
                try:
                    package = cmd[2]
                except:
                    print("Shell: Insert package name!")
                else:
                    self.search(package)

    def install(self, pack_name):
        system("git clone https://github.com/Habejota/{}.git".format(pack_name))
        a = pack_name.replace("habejota/", "")
        try:
            bache = open(fr"{a}\{a}.exe", "rb")
            bache.close()
        except Exception as e:
            print("Shell: Fail to install Packages!")
            print(e)
        else:
            system(fr"move {a}\{a}.exe ")
            bache = open("git-prompt.sh",  "a+")
            bache.write(f'alias {a}="/etc/profile.d/{a}.exe"')
            print("Shell: Package installed with sucessfuly!")
        print(a)
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