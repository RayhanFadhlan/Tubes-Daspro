from globalvar import *
from save import *
import globals
import sys 

def exit():
    save_exit=input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    while (save_exit!="y")and(save_exit!="Y")and(save_exit!="n")and(save_exit!="N"):
        save_exit=input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    if (save_exit=="y")or(save_exit=="Y"):
        save()
        sys.exit(1)
    elif (save_exit=="n")or(save_exit=="N"):
        sys.exit()
