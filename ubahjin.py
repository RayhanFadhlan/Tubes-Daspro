from globalvar import *

def ubahjin():
    username = input("Masukkan username jin: ")
    if(usertersedia):
        index = cariidxuser(username)
        if(listrole[index] == "pengumpul"):
            roleubahke = "pembangun"
        else:
            roleubahke = "pengumpul"
        masukan = input(f"Jin ini bertipe “{listrole[index]}”. Yakin ingin mengubah ke tipe “{roleubahke}” (Y/N)? ")
        if(masukan == "Y"):
            listrole[index] = roleubahke
            print("Jin telah berhasil diubah.")
        elif(masukan == "N"):
            print("Jin tidak jadi diubah.")
    
    else:
        print("Tidak ada jin dengan username tersebut.")


def usertersedia(username):
    for i in range (102):
        if(username == listuser[i]):
            return False
    return True

def cariidxuser(username):
    for i in range (102):
        if(username == listuser[i]):
            return i
    return -1