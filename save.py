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
