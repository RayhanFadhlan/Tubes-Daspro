from globalvar import *
import globals

def help():
    if(globals.sudahlogin==False):
        print("=========== HELP ===========")
        print("1. login") #Fungsi login
        print("   Untuk masuk menggunakan akun")
        print("2. load") #Fungsi load
        print("   memuat data yang sesuai dengan struktur data eksternal")
        print("   Prosedur ini hanya akan dijalankan sekali saat pertama kali program dijalankan,")
        print("   dengan cara memberikan parameter nama folder yang berisi file penyimpanan.")
        print("3. save") #Fungsi save
        print("   untuk menjalankan prosedur menyimpan data yang berada di program sesuai dengan struktur data eksternal.")
        print("   Berikut ketentuan :")
        print("   -  Jika nama folder tidak ditemukan, program akan membuat folder sesuai dengan")
        print("      masukan dan memberikan pesan ketika membuat folder")
        print("   -  Jika nama folder sudah ada, program akan menaruh file baru pada folder tersebut")
        print("   -  Jika nama folder dan file sudah ada, program akan mengganti file pada folder tersebut")
        print("      dengan yang lebih baru dan tidak perlu memberikan pesan tambahan")
        print("4. exit") #Fungsi exit
        print("   Untuk keluar dari program dan kembali ke terminal")
    if(globals.roleactive=="bandung_bondowoso"):
        print("=========== HELP ===========")
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. summon jin") #Fungsi Summon Jin
        print("   untuk memanggil jin")
        print("3. hapusjin") #Fungsi Hapus Jin
        print("   untuk menghapus jin")
        print("   note : candi yang dibangun jin juga ikut terhapus")
        print("4. ubahjin") #Fungsi Uban Jin
        print("   untuk mengubah tipe jin")
        print("   Jin yang sudah disummon dapat diubah tipenya")
        print("5. batchkumpul") #Fungsi batch kumpul
        print("   mengerahkan jin pengumpul untuk mengumpulkan bahan bangunan")
        print("   setiap jin mengumpulkan bahan bangunan secara random lalu dijumlahkan")
        print("6. batchbangun") #Fungsi batch bangun
        print("   mengerahkan jin pembangun untuk membangun candi")
        print("   setiap jin membangun candi dengan jumlah bahan bangunan secara random")
        print("7. laporanjin") #Fungsi laporan jin
        print("   mengambil laporan jin untuk mengetahui kinerja dari para jin")
        print("   laporan yang keluar berupa total jin, jin terajin, jin termalas")
        print("   jumlah bahan bangunan")
        print("8. laporancandi") #Fungsi laporan candi
        print("   mengambil laporan candi untuk mengetahui progress pembangunan candi")
        print("   laporan yang keluar berupa total candi, total penggunaan bahan bangunan")
        print("   ID candi termahal, ID candi termurah")
    if(globals.roleactive=="roro_jonggrang"):
        print("=========== HELP ===========")
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. hancurkancandi") #Fungsi Hancurkan Candi
        print("   Untuk menghancurkan candi yang tersedia")
        print("3. ayamberkokok") #Fungsi Ayam Berkokok
        print("   Menyelesaikan permainan dengan memalsukan pagi hari.")
        print("   Jika jumlah candi yang dibangun lebih atau sama dengan 100")
        print("   Bandung Bondowoso memenangkan permainan.")
        print("   Jika jumlah candi yang dibangun kurang dari 100")
        print("   Roro Jonggrang memenangkan permainan.")
    if(globals.roleactive=="pengumpul"):
        print("=========== HELP ===========")
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. kumpul") #Fungsi Kumpul Bahan Bangunan
        print("   Untuk mengumpulkan resource candi secara random")
    if(globals.roleactive=="pembangun"):
        print("=========== HELP ===========")
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. bangun") #Fungsi Bangun Candi
        print("   Untuk membangun candi dengan jumlah bahan bangunan secara random")


