from base import *
from random import choice

keys = ["everythink", "kernel.py", "bootloader", "isinstance", "lambda", "anythink", 
         " ", "recv", "install"]

responces = []

for i in range(0, 12):
    r = keys.choice()
    try:
        rss = open(r, "r")
        rss.close()
    except FileNotFoundError:
        
        