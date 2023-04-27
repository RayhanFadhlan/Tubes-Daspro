from globalvar import *
import globals

def hancurkancandi():
    pilihan = int(input("Masukkan ID candi yang ingin dihancurkan: "))
    if(canditersedia(pilihan)==False):
        print("Tidak ada candi dengan ID tersebut.")
        return
    else:
        yesorno = input(f"Apakah anda yakin ingin menghancurkan candi ID: {pilihan} (Y/N)? ")
        if(yesorno=='Y'):
            for i in range(100):
                if(listcandi[i][0]==pilihan):
                    listcandi[i][0]=0
                    listcandi[i][1]=''
                    listcandi[i][2]=0
                    listcandi[i][3]=0
                    listcandi[i][4]=0
                    print("Candi berhasil dihancurkan.")
        
        elif(yesorno=='N'):
            print("Candi tidak jadi dihancurkan.")
        

def canditersedia(idcandi):
    for i in range(100):
        if(listcandi[i][0]==idcandi):
            return True
    return False