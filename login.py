# import csv
# listlistuser = ['' for i in range (102)]
# listpassword = ['' for i in range (102)]
# role = ['' for i in range (102)]

# count = 0
# with open('listuser.csv') as f:
#     reader = csv.reader(f, delimiter=';')
#     for row in reader:
#         listuser[count] = row[0]
#         listpassword[count] = row[1]
#         role[count] = row[2]
#         count+=1
from globalvar import *
import globalvar2
sudahlogin = False

def login():
    global sudahlogin
    global roleactive
    global useractive
    if(sudahlogin):
        print("Login gagal!")
        print(f"Anda telah login dengan username {useractive}, silahkan lakukan “logout” ")
        print("sebelum melakukan login kembali.")
        return
    else:
        checkusername = input("username: ")
        checkpassword = input("password: ")
        for i in range (102):
            if(checkusername == listuser[i]):
                if(checkpassword == listpassword[i]):
                    print(f"Selamat datang, {checkusername}!")
                    print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
                    globalvar2.useractive = checkusername
                    roleactive = listrole[i]
                    sudahlogin = True
                    
                    return
                else:
                    print("password salah!")
                return
        print("username tidak terdaftar!")
        return
        

def logout():
    global roleactive
    global useractive
    global sudahlogin
    if(sudahlogin==True):
        roleactive = False
        useractive = False
        sudahlogin = False
    else:
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")

# def summonjin():
#     print("Jenis jin yang dapat dipanggil: \n(1) Pengumpul - Bertugas mengumpulkan bahan bangunan \n(2) Pembangun - Bertugas membangun candi")
#     masukan = input("Masukkan nomor jenis jin yang ingin dipanggil: ")

#     if(masukan == "1"):

# def carielemenkosong(arr):
#     for i in range (102):
        