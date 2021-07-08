import sys
class Services:
    def __init__(self, args):
        from os import system
        try:
            service_name = args[1]
        except:
            print("OSystem bash:")
            print("Service ps Manager Controller - service (args**)[name][start/stop]")
        else:
            try:
                    what = args[2]
            except:
                    print("service:  Insert what i will do with {}".format(service_name))
            else:
                    if what == "start":
                        system(service_name)
                    elif what == "stop":
                        system("taskkill {}".format(service_name))
                    else:
                        print("service:    CommandNotFoundError")  
Services(sys.argv) 