from globalvar import *
import globals
from random import *

def bangun():
    reqpasir = randint(1, 5)
    reqbatu = randint(1, 5)
    reqair = randint(1, 5)
    print(f"Men-generate bahan bangunan ({reqpasir} pasir, {reqbatu} batu, dan {reqair} air)")
    if(listbahan[0] >= reqpasir and listbahan[1] >= reqbatu and listbahan[2] >= reqair):
        listbahan[0] -= reqpasir
        listbahan[1] -= reqbatu
        listbahan[2] -= reqair
        if(cekjmlcandi==100): #jika jml sudah 100 maka candi tidak dicatat di array
            pass
        else:
            idxkosong = caricandikosong()
            listcandi[idxkosong][0] = cariidkosong()
            listcandi[idxkosong][1] = globals.useractive
            listcandi[idxkosong][2] = reqpasir
            listcandi[idxkosong][3] = reqbatu
            listcandi[idxkosong][4] = reqair

        print("Candi berhasil dibangun.")
        print(f"Sisa candi yang perlu dibangun: {100-cekjmlcandi()}")
        
    else:
        print(f"Memiliki {listbahan[0]} pasir, {listbahan[1]} batu, dan {listbahan[2]} air.")
        print("Bahan bangunan tidak mencukupi")
        print("Candi gagal dibangun.")

def cekjmlcandi():
    count = 0
    for i in range (100):
        if(listcandi[i][0] != 0):
            count+=1
    return count

def caricandikosong():
    for i in range (100):
        if(listcandi[i][0] == 0):
            return i
    return -1

def cariidkosong():
    for i in range(1,101):
        nemu = False
        for j in range (100):
            if(listcandi[j][0] == i):
                nemu = True
                break
        if(nemu == False):
            return i