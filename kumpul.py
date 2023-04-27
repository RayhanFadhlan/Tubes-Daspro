from globalvar import *
import globals
from random import *

def kumpul():
    pasir = randint(0, 5)
    batu = randint(0, 5)
    air = randint(0, 5)
    listbahan[0] += pasir
    listbahan[1] += batu
    listbahan[2] += air 
    print(f"Jin menemukan {pasir} pasir, {batu} batu, dan {air} air.")