from globalvar import *
import globals
import os

def csvparse():
    namafolder = globals.loadfolder
    with open(f'save/{namafolder}/user.csv',) as f:
        jml = -1
        for line in f:
            if(jml==-1):
                jml+=1
            else:
                arr = splitmanual(line)
                listuser[jml] = arr[0]
                listpassword[jml] = arr[1]
                listrole[jml] = stripmanual(arr[2])
                jml+=1
        f.close()

    with open(f'save/{namafolder}/candi.csv') as f:
        jml = -1
        for line in f:
            if(jml==-1):
                jml+=1
            else:
                arr = splitmanual(line)
                listcandi[jml][0] = int(arr[0])
                listcandi[jml][1] = arr[1]
                listcandi[jml][2] = int(arr[2])
                listcandi[jml][3] = int(arr[3])
                listcandi[jml][4] = int(stripmanual(arr[4]))
                jml+=1
        f.close()

    with open(f'save/{namafolder}/bahan_bangunan.csv') as f:
        jml = -1
        for line in f:
            if(jml==-1):
                jml+=1
            else:
                arr = splitmanual(line)
                listbahan[jml] = int(stripmanual(arr[2]))
                jml+=1
        f.close()

def stripmanual(line):
    temp = ''
    for i in range (len (line)):
        if(line[i] != '\n'):
            temp+=line[i]
    return temp

def splitmanual(line):
    count = 0
    for i in range(len(line)):
        if(line[i] == ';'):
            count+=1
    arr = ['' for i in range (count+1)]
    temp = ''
    count = 0
    for i in range (len (line)):
        if(line[i] == ';'):
            arr[count] = temp
            count+=1
            temp = ''
        else:
            temp+=line[i]
    arr[count] = temp
    return arr