
from globalvar import *
import globals
sudahlogin = False

def login():

    if(globals.sudahlogin):
        print("Login gagal!")
        print(f"Anda telah login dengan username {globals.useractive}, silahkan lakukan “logout” ")
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
                    globals.useractive = checkusername
                    globals.roleactive = listrole[i]
                    globals.sudahlogin = True
                    
                    return
                else:
                    print("password salah!")
                return
        print("username tidak terdaftar!")
        return
        

def logout():

    if(globals.sudahlogin==True):
        globals.roleactive = False
        globals.useractive = False
        globals.sudahlogin = False
    else:
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")

