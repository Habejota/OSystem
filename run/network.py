# Python modules importations
import socket
from os import chdir, system, sync

# Local Host informations
hostname = socket.gethostname()
localhost = socket.gethostbyname(hostname)

# Socket Connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(20)
s.connect((localhost, 80))