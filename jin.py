from globalvar import *
def summonjin():
    if(cekisiarray(listuser) ==102):
        print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
    else:
        print("Jenis jin yang dapat dipanggil:")
        print(" (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print(" (2) Pembangun - Bertugas membangun candi")

        pilihan = input("Masukkan nomor jenis jin yang ingin dipanggil: ")
        if(pilihan == "1"):
            role = "pengumpul"
            cetakjin(role)
        elif(pilihan == "2"):
            role = "pembangun"
            cetakjin(role)
        else:
            print(f"Tidak ada jenis jin bernomor {pilihan}!")
            

def hapusjin():
    username = input("Masukkan username jin :")
    if(usertersedia(username)):
        pilihan = input("Apakah anda yakin ingin menghapus jin dengan username Jin1 (Y/N)?")
        if(pilihan == "Y"):
            hapususer(username)
            print(f"Jin {username} berhasil dihapus")
        elif(pilihan == "N"):
            print("Tidak ada jin dengan username tersebut.")


def cetakjin(role):
    print(f"Memilih jin “{role}”.")
    username = input("Masukkan username jin: ")
    if(not usertersedia(username)):
        print("Username sudah terdaftar!")
        return
    else:
        password = input("Masukkan password jin:")
        lenpass = len(password)
        while(lenpass<5 or lenpass>25):
            print("password panjangnya harus 5-25 karakter!")
            password = input("Masukkan password jin:")
            lenpass = len(password)
        print(f"Jin {username} berhasil didaftarkan")
        catat(username, password, role)
    
def ubahjin():
    username = input("Masukkan username jin: ")
    if(usertersedia):
        index = cariidxuser(username)
        if(listrole[index] == "pengumpul"):
            roleubahke = "pembangun"
        else:
            roleubahke = "pengumpul"
        print(f"Jin ini bertipe “{listrole[index]}”. Yakin ingin mengubah ke tipe “{roleubahke}” (Y/N)? Y ")
        listrole[index] = roleubahke
        print("Jin telah berhasil diubah.")
    
    else:
        print("Tidak ada jin dengan username tersebut.")

def usertersedia(username):
    global user
    for i in range (102):
        if(username == user[i]):
            return False
    return True

def catat(username, password, role):
    for i in range (102):
        if(user[i] == ''):
            listuser[i] = username
            listpassword[i] = password
            listrole[i] = role
            return

def cekisiarray(arr):
    count = 0
    for i in range (102):
        if(arr[i] != ''):
            count+=1
    return count

def hapususer(username):
    for i in range (102):
        if(username == user[i]):
            listuser[i] = ''
            listpassword[i] = ''
            listrole[i] = ''
            return
        
def cariidxuser(username):
    for i in range (102):
        if(username == user[i]):
            return i
    return -1
