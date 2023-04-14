# File: main.py

from login import *
from csvparser import *
from jin import *
from globalvar import *
from jincandi import *
from laporan import *
import globalvar2
# Anggap semua fungsi yang dipanggil merupakan fungsi yang sudah dibuat sendiri pada modul lain
listuser = ['' for i in range (102)]
listpassword = ['' for i in range (102)]
listrole = ['' for i in range (102)]
listbahan = [0 for i in range (3)]
listcandi = [['' for i in range(5)]for j in range(100)]

# load("file/user.csv", users)
# load("file/candi.csv", candi)
# load("file/bahan_bangunan.csv", bahan_bangunan)
csvparse()
print(listuser,listpassword,listrole)
while True:
  masukan = input(">>> ")
  # call a function on tubes.py based on masukan
  if masukan == "login": 
    login()
  elif masukan == "logout":
    logout()
  elif masukan == "summonjin":
    summonjin()
  elif masukan == "hapusjin":
    hapusjin()
  elif masukan == "ubahjin":
    ubahjin()
  elif masukan == "kumpul":
    kumpul()
  elif masukan == "bangun":
    bangun()
  elif masukan == "batchkumpul":
    batchkumpul()
  elif masukan == "batchbangun":
    batchbangun()
  elif masukan == "laporanjin":
    laporanjin()
