from globalvar import *
import globalvar2
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
    print(leaderboard)

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
    return leaderboard

print(globalvar2.useractive)