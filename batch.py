from globalvar import *
import globals
from random import *

def batchkumpul():
    if(cekjmlrole("pengumpul") == 0):
        print("Tidak ada jin pengumpul. Silahkan summon jin pengumpul terlebih dahulu.")
    else:
        temppasir = listbahan[0]
        tempbatu = listbahan[1]
        tempair = listbahan[2]
                
        for i in range (102):
            if(listrole[i] == "pengumpul"):
                
                pasir = randint(0, 5)
                batu = randint(0, 5)
                air = randint(0, 5)
                listbahan[0] += pasir
                listbahan[1] += batu
                listbahan[2] += air 

        jmlpasir = listbahan[0] - temppasir
        jmlbatu = listbahan[1] - tempbatu
        jmlair = listbahan[2] - tempair
        print(f"Mengerahkan {cekjmlrole('pengumpul')} jin pengumpul untuk mengumpulkan bahan.")
        print(f"jin menemukan total {jmlpasir} pasir, {jmlbatu} batu, dan {jmlair} air.")
        print(f"jumlah bahan saat ini: {listbahan[0]} pasir, {listbahan[1]} batu, dan {listbahan[2]} air.")

def batchbangun():
    if(cekjmlrole("pembangun") == 0):
        print("Tidak ada jin pembangun. Silahkan summon jin pembangun terlebih dahulu.")
    else:
        jmlpembangun = cekjmlrole("pembangun")
        tempcandi = [['','',0,0,0]for j in range(jmlpembangun)]
        idx = 0
        jmlpasir = 0
        jmlbatu = 0
        jmlair = 0
        for i in range (102):
            if(listrole[i] == "pembangun"):
                reqpasir = randint(1, 5)
                reqbatu = randint(1, 5)
                reqair = randint(1, 5)
                tempcandi[idx][0] = cariidkosongtwithtemp(tempcandi,jmlpembangun)
                tempcandi[idx][1] = listuser[i]
                tempcandi[idx][2] = reqpasir
                tempcandi[idx][3] = reqbatu
                tempcandi[idx][4] = reqair

                jmlpasir += reqpasir
                jmlbatu += reqbatu
                jmlair += reqair
                idx+=1

        print(f"Mengerahkan {jmlpembangun} jin pembangun untuk membangun candi dengan total {jmlpasir} pasir, {jmlbatu} batu, dan {jmlair} air.")
        if(listbahan[0] >= jmlpasir and listbahan[1] >= jmlbatu and listbahan[2] >= jmlair):
            
            listbahan[0] -= jmlpasir
            listbahan[1] -= jmlbatu
            listbahan[2] -= jmlair
            candifull = 0
            for i in range (jmlpembangun):
                idx = caricandikosong()
                if idx == -1:
                    candifull+=1
                else:
                    listcandi[idx] = tempcandi[i]
            print(f"Jin berhasil membangun {jmlpembangun - candifull} candi.")
            print(f"Sisa candi yang perlu dibangun: {100-cekjmlcandi()}")
        else:
            if(jmlpasir - listbahan[0]<0):
                kurangpasir = 0
            else:
                kurangpasir = jmlpasir - listbahan[0]
            if(jmlbatu - listbahan[1]<0):
                kurangbatu = 0
            else:
                kurangbatu = jmlbatu - listbahan[1]
            if(jmlair - listbahan[2]<0):
                kurangair = 0
            else:
                kurangair = jmlair - listbahan[2]
            print(f"Memiliki {listbahan[0]} pasir, {listbahan[1]} batu, dan {listbahan[2]} air.")
            print(f"Bangun gagal. Kurang {kurangpasir} pasir, {kurangbatu} batu, dan {kurangair} air.")
            print("Jin gagal membangun candi.")



def cekjmlrole(role):
    count = 0
    for i in range (102):
        if(listrole[i] == role):
            count+=1
    return count

def cariidkosong():
    for i in range(1,101):
        nemu = False
        for j in range (100):
            if(listcandi[j][0] == i):
                nemu = True
                break
        if(nemu == False):
            return i
        
def caricandikosong():
    for i in range (100):
        if(listcandi[i][0] == 0):
            return i
    return -1


def cariidkosongtwithtemp(tempcandi,jmlpembangun): # mencari id kosong untuk tempcandi
    for i in range(1,101):
        nemu = False
        for j in range (100):
            if(listcandi[j][0] == i):
                nemu = True
                break
        for j in range (jmlpembangun):
            if(tempcandi[j][0] == i):
                nemu = True
                break
        if(nemu == False):
            return i

def cekjmlcandi():
    count = 0
    for i in range (100):
        if(listcandi[i][0] != 0):
            count+=1
    return count