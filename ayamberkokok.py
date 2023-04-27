from globalvar import *
import globals


def ayamberkokok():
    print("Kukuruyuk.. Kukuruyuk")
    print(f"Jumlah candi : {cekjmlcandi()}")
    if(cekjmlcandi()<100):
        print("Selamat, Roro Jonggrang memenangkan permainan!")
    else:
        print("Yah, Bandung Bondowoso memenangkan permainan!")


def cekjmlcandi():
    count = 0
    for i in range (100):
        if(listcandi[i][0] != 0):
            count+=1
    return count