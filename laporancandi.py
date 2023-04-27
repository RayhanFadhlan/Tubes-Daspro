from globalvar import *
import globals

def laporancandi():
    hargamax = float('-inf')
    hargamin = float('inf')
    candimax = '-'
    candimin = '-'
    sumcandi = 0
    sumpasir = 0
    sumbatu = 0
    sumair = 0

    for i in range(100):
        if(listcandi[i][0]!=0):
            sumcandi+=1
            sumpasir+=listcandi[i][2]
            sumbatu+=listcandi[i][3]
            sumair+=listcandi[i][4]
            hargacandi = 10000*listcandi[i][2]+15000*listcandi[i][3]+7500*listcandi[i][4]
            if(hargacandi>hargamax):
                hargamax = hargacandi
                candimax = listcandi[i][0]
            if(hargacandi<hargamin):
                hargamin = hargacandi
                candimin = listcandi[i][0]
    print(f"Total candi: {sumcandi}")
    print(f"Total pasir yang digunakan: {sumpasir}")
    print(f"Total batu yang digunakan: {sumbatu}")
    print(f"Total air yang digunakan: {sumair}")
    if(sumcandi==0):
        print("ID Candi termahal: -")
        print("ID Candi termurah: -")
    else:
        print(f"ID Candi termahal: {candimax} (Rp {hargamax:,}))")
        print(f"ID Candi termurah: {candimin} (Rp {hargamin:,}))")
        
