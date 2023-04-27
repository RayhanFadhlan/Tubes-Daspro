from globalvar import *

def hapusjin():
    username = input("Masukkan username jin : ")
    if(not usertersedia(username)):
        pilihan = input(f"Apakah anda yakin ingin menghapus jin dengan username {username} (Y/N)?")
        if(pilihan == "Y"):
            hapususer(username)
            hapuscandi(username)
            print(f"Jin {username} berhasil dihapus")
        elif(pilihan == "N"):
            print("Jin tidak jadi dihapus.")
    else:
        print("Tidak ada jin dengan username tersebut.")


def usertersedia(username):
    for i in range (102):
        if(username == listuser[i]):
            return False
    return True

def hapususer(username):
    for i in range (102):
        if(username == listuser[i]):
            listuser[i] = ''
            listpassword[i] = ''
            listrole[i] = ''
            return
        
def hapuscandi(username):
    for i in range(100):
        if(username==listcandi[i][1]):
            listcandi[i][0]=0
            listcandi[i][1]=''
            listcandi[i][2]=0
            listcandi[i][3]=0
            listcandi[i][4]=0