from globalvar import *
import globals

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
