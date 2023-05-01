# File: main.py

from login import *
from logout import *
from summonjin import *
from hapusjin import *
from ubahjin import *
from bangun import *
from kumpul import *
from batch import *
from laporanjin import *
from laporancandi import *
from hancurkancandi import *
from ayamberkokok import *
from load import *
from save import *
from help import *
from exit import *
from globalvar import *
import sys
import argparse
import os
import globals

parser = argparse.ArgumentParser()
parser.add_argument("namafolder", help="nama folder yang akan dibuat", type=str)
if len(sys.argv)==1:
    print("Tidak ada nama folder yang diberikan!")
    print("Usage: python main.py <nama_folder>")
    print("gunakan 'python main.py testing' jika ini adalah permainan pertama")
    sys.exit(1)
args=parser.parse_args()
globals.loadfolder = args.namafolder
if(os.path.isdir(f"save/{args.namafolder}")):
  print("Loading...")
  print("Selamat datang di program Manajerial Candi")
  print("Silahkan melakukan login")
  print("ketik 'help' untuk melihat daftar command yang dapat dipanggil")

else:
  print(f"Folder '{args.namafolder}' tidak ditemukan!")
  sys.exit(1)



csvparse()

while True:
  masukan = input(">>> ")
  if globals.sudahlogin == False:
    if masukan == "login": 
      login()
    elif masukan == "logout":
      logout()
    elif masukan == "help":
      help()
    elif masukan == "save":
      save()
    elif masukan == "exit":
      exit()
    else:
      print("Command tidak tersedia! ketik 'help' untuk melihat daftar command yang dapat dipanggil")
  
  elif globals.roleactive == "bandung_bondowoso":
    if masukan == "logout":
      logout()
    elif masukan == "login":
      login()
    elif masukan == "summonjin":
      summonjin()
    elif masukan == "hapusjin":
      hapusjin()
    elif masukan == "ubahjin":
      ubahjin()
    elif masukan == "batchkumpul":
      batchkumpul()
    elif masukan == "batchbangun":
      batchbangun()
    elif masukan == "laporanjin":
      laporanjin()
    elif masukan == "laporancandi":
      laporancandi()
    elif masukan == "save":
      save()
    elif masukan == "exit":
      exit()
    elif masukan == "help":
      help()
    else:
      print("Command tidak tersedia! ketik 'help' untuk melihat daftar command yang dapat dipanggil")
  elif globals.roleactive == "roro_jonggrang":
    if(masukan == "hancurkancandi"):
      hancurkancandi()
    elif(masukan == "ayamberkokok"):
      ayamberkokok()
    elif masukan == "login":
      login()
    elif masukan == "logout":
      logout()
    elif masukan == "save":
      save()
    elif masukan == "exit":
      exit()
    elif masukan == "help":
      help()     
    else:
      print("Command tidak tersedia! ketik 'help' untuk melihat daftar command yang dapat dipanggil")
  elif globals.roleactive == "pengumpul":
    if(masukan == "kumpul"):
      kumpul()
    elif masukan == "login":
      login()
    elif masukan == "logout":
      logout()
    elif masukan == "save":
      save()
    elif masukan == "exit":
      exit()
    elif masukan == "help":
      help()      
    else:
      print("Command tidak tersedia! ketik 'help' untuk melihat daftar command yang dapat dipanggil")
  elif globals.roleactive == "pembangun":
    if(masukan == "bangun"):
      bangun()
    elif masukan == "login":
      login()
    elif masukan == "logout":
      logout()
    elif masukan == "save":
      save()
    elif masukan == "exit":
      exit()
    elif masukan == "help":
      help()
    else:
      print("Command tidak tersedia! ketik 'help' untuk melihat daftar command yang dapat dipanggil")