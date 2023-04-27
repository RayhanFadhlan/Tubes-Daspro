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

    jincandi = sort(listcandi)
    jumlahjincandi = countelementberbeda(jincandi)

    
    leaderboard = [['',0]for j in range(jumlahjincandi)]
    leaderboard = bikinarraypembangun(leaderboard)
    leaderboard = sortpair(leaderboard,jumlahjincandi)
    print(leaderboard)
    jinterajin = leaderboard[0][0]
    jintermalas = leaderboard[jumlahjincandi-1][0]
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

def sort(listcandi):
    for i in range (100):
        for j in range (100):
            if(listcandi[i][1]>listcandi[j][1]):
                temp = listcandi[i]
                listcandi[i] = listcandi[j]
                listcandi[j] = temp
    return listcandi

def countelementberbeda(listcandi):
    count = 0
    for i in range (100):
        if(listcandi[i][0]!=0):
            if(listcandi[i][1]!=listcandi[i-1][1]):
                count+=1
    return count

def countuser(username):
    count = 0
    for i in range (100):
        if(listcandi[i][1] == username):
            count+=1
    return count

def bikinarraypembangun(leaderboard):
    count = 0
    for i in range(102):
        if(countuser(listuser[i])!=0 and listuser[i]!=""):
            leaderboard[count][0] = listuser[i]
            leaderboard[count][1] = countuser(listuser[i])
            count+=1
            print(leaderboard)
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


