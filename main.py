# File: main.py

from login import *
from csvparser import *
from jin import *
from globalvar import *
from jincandi import *
from laporanjin import *
from laporancandi import *
from roropower import *
import sys
import argparse
import os


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
# print(listuser,listpassword,listrole)
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
  elif masukan == "laporancandi":
    laporancandi()
  elif masukan == "save":
    save()
  elif masukan == "ayamberkokok":
    ayamberkokok()
  elif masukan == "hancurkancandi":
    hancurkancandi()
  elif masukan == "tes":
    print(listcandi)