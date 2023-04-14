from globalvar import *
import globalvar2
from random import *
def kumpul():
    pasir = randint(0, 5)
    batu = randint(0, 5)
    air = randint(0, 5)
    listbahan[0] += pasir
    listbahan[1] += batu
    listbahan[2] += air 
    print(f"Jin menemukan {pasir} pasir, {batu} batu, dan {air} air.")
    

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


def bangun():
    reqpasir = randint(1, 5)
    reqbatu = randint(1, 5)
    reqair = randint(1, 5)
    print(f"Men-generate bahan bangunan ({reqpasir} pasir, {reqbatu} batu, dan {reqair} air)")
    if(listbahan[0] >= reqpasir and listbahan[1] >= reqbatu and listbahan[2] >= reqair):
        listbahan[0] -= reqpasir
        listbahan[1] -= reqbatu
        listbahan[2] -= reqair
        if(cekjmlcandi==100):
            pass
        else:
            idxkosong = caricandikosong()
            listcandi[idxkosong][0] = cariidkosong()
            listcandi[idxkosong][1] = globalvar2.useractive
            listcandi[idxkosong][2] = reqpasir
            listcandi[idxkosong][3] = reqbatu
            listcandi[idxkosong][4] = reqair

        print("Candi berhasil dibangun.")
        print(f"Sisa candi yang perlu dibangun: {100-cekjmlcandi()}")
        
    else:
        print(f"Memiliki {listbahan[0]} pasir, {listbahan[1]} batu, dan {listbahan[2]} air.")
        print("Bahan bangunan tidak mencukupi")
        print("Candi gagal dibangun.")

    print(globalvar2.useractive,"tes")
    print(roleactive,"tes2")
    print(listcandi)
def batchbangun():
    if(cekjmlrole("pembangun") == 0):
        print("Tidak ada jin pembangun. Silahkan summon jin pembangun terlebih dahulu.")
    else:
        jmlpembangun = cekjmlrole("pembangun")
        tempcandi = [['' for i in range(5)]for j in range(jmlpembangun)]
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
            print(f"Jin berhasil membangun {jmlpembangun} candi.")
            listbahan[0] -= jmlpasir
            listbahan[1] -= jmlbatu
            listbahan[2] -= jmlair
            for i in range (jmlpembangun):
                idx = caricandikosong()
                listcandi[idx] = tempcandi[i]

        else:
            
            print(f"Memiliki {listbahan[0]} pasir, {listbahan[1]} batu, dan {listbahan[2]} air.")
            print(f"Bangun gagal. Kurang { jmlpasir - listbahan[0]} pasir, {jmlbatu - listbahan[1]} batu, dan {jmlair - listbahan[2]} air.")
            print("Jin gagal membangun candi.")
        print(listcandi)

def cekjmlrole(role):
    count = 0
    for i in range (102):
        if(listrole[i] == role):
            count+=1
    return count

def cekjmlcandi():
    count = 0
    for i in range (100):
        if(listcandi[i][0] != ''):
            count+=1
    return count

def caricandikosong():
    for i in range (100):
        if(listcandi[i][0] == ''):
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

def cariidkosongtwithtemp(tempcandi,jmlpembangun):
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

