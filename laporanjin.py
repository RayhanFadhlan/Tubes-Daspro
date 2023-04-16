from globalvar import *
import globals
def laporanjin():
    totaljin = 0
    totalpembangun = 0
    totalpengumpul = 0

    for i in range(102):
        if(listrole[i] == 'pembangun'):
            totalpembangun+=1
        elif(listrole[i] == 'pengumpul'):
            totalpengumpul+=1
    totaljin = totalpembangun + totalpengumpul
    leaderboard = [['',0]for j in range(totalpembangun)]
    leaderboard = bikinarraypembangun(leaderboard)
    leaderboard = sortpair(leaderboard,totalpembangun)
    jinterajin = leaderboard[0][0]
    jintermalas = leaderboard[totalpembangun-1][0]
    jumlahpasir = listbahan[0]
    jumlahbatu = listbahan[1]
    jumlahair = listbahan[2]

    if(leaderboard==[[]]or leaderboard[0][1]==0):
        jinterajin = "-"
        jintermalas = "-"

    print(f"Total Jin: {totaljin}")
    print(f"Total Jin Pengumpul: {totalpengumpul}")
    print(f"Total Jin Pembangun: {totalpembangun}")
    print(f"jin terajin: {jinterajin}")
    print(f"jin termalas: {jintermalas}")
    print(f"Jumlah pasir: {jumlahpasir} unit")
    print(f"Jumlah batu: {jumlahbatu} unit")
    print(f"Jumlah air: {jumlahair} unit")



def countuser(username):
    count = 0
    for i in range (100):
        if(listcandi[i][1] == username):
            count+=1
    return count

def bikinarraypembangun(leaderboard):
    count = 0
    for i in range(102):
        if(listrole[i] == 'pembangun'):
            leaderboard[count][0] = listuser[i]
            leaderboard[count][1] = countuser(listuser[i])
            count+=1
    return leaderboard

def sortpair(leaderboard,totalpembangun):
    for i in range (totalpembangun):
        for j in range (totalpembangun):
            if(leaderboard[i][1] > leaderboard[j][1]):
                temp = leaderboard[i]
                leaderboard[i] = leaderboard[j]
                leaderboard[j] = temp
            if(leaderboard[i][1] == leaderboard[j][1]):
                if(leaderboard[i][0] < leaderboard[j][0]):
                    temp = leaderboard[i]
                    leaderboard[i] = leaderboard[j]
                    leaderboard[j] = temp
    return leaderboard



# leaderboard = [['d',3],['a',1],['b',3],['c',3],['d',2]]
# print(sortpair(leaderboard,4))

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
        if(listcandi[i][0]!=''):
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
        
