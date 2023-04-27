from globalvar import *
import globals
def logout():

    if(globals.sudahlogin==True):
        globals.roleactive = False
        globals.useractive = False
        globals.sudahlogin = False
        print("Logout berhasil!")
    else:
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
