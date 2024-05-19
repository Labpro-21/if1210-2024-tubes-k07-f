# TUBES DASPRO ----------------------------------------------------------------------------------
import os
import sys
import time
import math
import argparse
import datetime

from src.save import *
from src.load import *
from src.rng import *
from src.register import *
from src.login import *
from src.logout import *
from src.help import *
from src.monster import *
from src.potion import *
from src.inventories import *
from src.battle import *
from src.arena import *
from src.shopcurrency import *
from src.monster_management import *
from src.shopmanagement import *
from src.laboratory import *
from src.save import *
from src.load import *

# Fungsi validasi input berbentuk integer atau tidak
def is_integer(input):
    is_integer = True
    for char in input:
        # Mengecek input menggunakan ascii number (0-9 : 48-57)
        if not (48 <= ord(char) <= 57):
            is_integer = False
    return is_integer

userpas, mons, iInv, mInv, iShop, mShop, valid_load = start()
print("Selamat datang di program OWCA!")
print("Ketik HELP untuk memunculkan bantuan dari The Mighty God.")
print()
print(mShop)
login = False
while True:
    pilihan = input(">>> ")
    if pilihan.upper() == "REGISTER":
        if login:
            print("Register gagal!")
            print(
                f"Anda telah login dengan username {currentUser[1]}, silahkan lakukan “LOGOUT” sebelum melakukan register.")
            print()
        else:
            REGISTER(userpas, mInv)
            print()
    if pilihan.upper() == "LOGIN":
        if login:
            print("Login gagal!")
            print(
                f"Anda telah login dengan username {currentUser[1]}, silahkan lakukan “LOGOUT” sebelum melakukan login kembali.")
            print()
        else:
            login, currentUser = LOGIN(userpas)
    if pilihan.upper() == "LOGOUT":
        login, currentUser = LOGOUT(currentUser, login)
    if pilihan.upper() == "HELP":
        HELP(currentUser)
    if pilihan.upper() == "INVENTORY":
        if login:
            INVENTORY(currentUser, mInv, iInv, mons)
        else:
            print("Anda belum login. Silahkan login terlebih dahulu..")
            print()
    if pilihan.upper() == "BATTLE":
        if login:
            if currentUser[3] == "agent":
                userpas, mInv, iInv = BATTLE(
                    mons, mInv, iInv, rngEnemy, currentUser, rngLevel, userpas)
            else:
                print("Anda tidak bisa battle.")
                print()
        else:
            print("Anda belum login. Silahkan login terlebih dahulu..")
            print()
    if pilihan.upper() == "ARENA":
        if login:
            if currentUser[3] == "agent":
                ARENA(mons, mInv, rngEnemy, currentUser, iInv)
                print()
            else:
                print("Anda tidak bisa memasuki Arena.")
                print()
        else:
            print("Anda belum login. Silahkan login terlebih dahulu..")
            print()
    if pilihan.upper() == "SHOP":
        if login:
            if currentUser[3] == "admin":
                SHOP_MANAGEMENT(currentUser, mShop, iShop, mons, potion)
                print()
            if currentUser[3] == "agent":
                SHOP(currentUser, mShop, iShop, mons, mInv, iInv)
                print()
        else:
            print("Anda belum login. Silahkan login terlebih dahulu..")
            print()
    if pilihan.upper() == "MONSTER":
        if login:
            if currentUser[3] == "admin":
                MONSTER(currentUser, userpas, mons, mInv)
                print()
            else:
                print("Anda bukanlah admin..")
                print()
        else:
            print("Anda belum login. Silahkan login terlebih dahulu..")
            print()
    if pilihan.upper() == "LABORATORY":
        if login:
            LABORATORY(userpas, mInv, mons, currentUser)
            print()
        else:
            print("Anda belum login. Silahkan login terlebih dahulu..")
            print()
    if pilihan.upper() == "SAVE":
        save_data(userpas, mons, mShop, mInv, iShop, iInv)
    if pilihan.upper() == "LOAD":
        load()
    if pilihan.upper() == "EXIT":
        while True:
            response = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ").lower()
            if response == 'y':
                save_data(userpas, mons, mShop, mInv, iShop, iInv)
                print("Data telah disimpan. Selamat tinggal!")
                break
            elif response == 'n':
                print("Selamat tinggal!")
                break
            else:
                print("Input tidak valid. Silahkan coba lagi.")
        break