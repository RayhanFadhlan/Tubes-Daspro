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

def cekisiarray(arr):
    count = 0
    for i in range (102):
        if(arr[i] != ''):
            count+=1
    return count

def cetakjin(role):
    print(f"Memilih jin “{role}”.")
    username = input("Masukkan username jin: ")
    if(not usertersedia(username)):
        print("Username sudah terdaftar!")
        return
    else:
        password = input("Masukkan password jin: ")
        lenpass = len(password)
        while(lenpass<5 or lenpass>25):
            print("password panjangnya harus 5-25 karakter!")
            password = input("Masukkan password jin: ")
            lenpass = len(password)
        print(f"Jin {username} berhasil didaftarkan")
        catat(username, password, role)


def catat(username, password, role):
    for i in range (102):
        if(listuser[i] == ''):
            listuser[i] = username
            listpassword[i] = password
            listrole[i] = role
            return
        
def usertersedia(username):
    for i in range (102):
        if(username == listuser[i]):
            return False
    return True