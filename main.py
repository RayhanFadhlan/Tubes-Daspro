# File: main.py

from login import *
from csvparser import *
from jin import *
from globalvar import *
# Anggap semua fungsi yang dipanggil merupakan fungsi yang sudah dibuat sendiri pada modul lain
users = [] # Matriks data user
candi = [] # Matriks data candi
bahan_bangunan = [] # Data bahan bangunan

# load("file/user.csv", users)
# load("file/candi.csv", candi)
# load("file/bahan_bangunan.csv", bahan_bangunan)

while True:
  masukan = input(">>> ")
  # call a function on tubes.py based on masukan
  if masukan == "login": 
    login()
  elif masukan == "logout":
    logout()
  elif masukan == "summonjin":
    summonjin()