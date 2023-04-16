from globalvar import *
import globals
import os


def save():
    folder = input("Masukkan nama folder: ")
    print("Saving...")
    if(not(os.path.isdir("save"))):
        os.makedirs("save")
        print(f"membuat folder save ...")
    if(not(os.path.isdir(f"save/{folder}"))):
        os.makedirs(f"save/{folder}")
        print(f"membuat folder save/{folder} ....")

    f = open(f"save/{folder}/user.csv", "w")
    f.write("username;password;role\n")
    for i in range(102):
        if(listuser[i] != ''):
            f.write(f"{listuser[i]};{listpassword[i]};{listrole[i]}\n")
    f.close()


    f = open(f"save/{folder}/candi.csv", "w")
    f.write("id;pembuat;pasir;batu;air\n")
    for i in range(100):
        if(listcandi[i][0] != 0):
            f.write(f"{listcandi[i][0]};{listcandi[i][1]};{listcandi[i][2]};{listcandi[i][3]};{listcandi[i][4]}\n")
    f.close()


    f = open(f"save/{folder}/bahan_bangunan.csv", "w")
    f.write("nama;deskripsi;jumlah\n")
    f.write(f"pasir;pasir kaliki;{listbahan[0]}\n")
    f.write(f"batu;batu cincin;{listbahan[1]}\n")
    f.write(f"air;air putih;{listbahan[2]}\n")
    print(f"Berhasil menyimpan data di folder save/{folder}")


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

