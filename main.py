# TUBES DASPRO ----------------------------------------------------------------------------------
import os
import sys
import time
import math
import argparse
import datetime

from src.csv import *
from src.register import *
from src.login import *
from src.logout import *
from src.help import *
from src.inventories import *
from src.shopcurrency import *
from src.battle import *
from src.rng import *
from src.overwrite import *

print("SELAMAT DATANG PADA PROGRAM YANG SEDANG DALAM PERCOBAAN INI!!!")
login = False
while True:
    pilihan = input(">>> ")
    if pilihan.upper() == "REGISTER":
        if login:
            print("Register gagal!")
            print(f"Anda telah login dengan username {currentUser[1]}, silahkan lakukan “LOGOUT” sebelum melakukan register.")
            print()
        else:
            userpas = REGISTER(cnt)
    if pilihan.upper() == "LOGIN":
        if login:
            print("Login gagal!")
            print(f"Anda telah login dengan username {currentUser[1]}, silahkan lakukan “LOGOUT” sebelum melakukan login kembali.")
            print()
        else:
            login = LOGIN(loginBool, wrongUsername, wrongPassword, userpas)
    if pilihan.upper() == "LOGOUT":
        login = LOGOUT(currentUser, login)
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
            userpas = BATTLE(mons, mInv, rngEnemy, currentUser, rngLevel)
        else:
            print("Anda belum login. Silahkan login terlebih dahulu..")
            print()
    if pilihan.upper() == "SHOP":
        if login:
            if currentUser[3] == "admin":
                SHOP(currentUser, mShop, iShop, mons)
            if currentUser[3] == "agent":
                SHOP(currentUser, mShop, iShop, mons)
        else:
            print("Anda belum login. Silahkan login terlebih dahulu..")
            print()
    if pilihan.upper() == "SAVE":
        SAVE(userpas, mons, mShop, mInv, iShop, iInv)
    if pilihan.upper() == "LOAD":
        break
    if pilihan.upper() == "EXIT":
        break

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
# lINEAR CONGRUENTIAL GENERATOR (RNG)
# def seedLCG(initVal):
#     global rand
#     rand = initVal

# def lcg():
#     a = 1140671485
#     c = 128201163
#     m = 2**24
#     global rand
#     rand = (a*rand + c) % m
#     return rand

# seedLCG(5)

# for i in range(10):
#     print(lcg())

# --------------------------------------------------------------------------------------

# MONSTER
# print("""                              __")
# print("                            .d$$b")
# print("                          .' TO$;'")
# print("                         /  : TP._;")
# print("                        / _.;  :Tb|")
# print("                       /   /   ;j$j")
# print("                   _.-'       d$$$$")
# print("                 .' ..       d$$$$;")
# print("                /  /P'      d$$$$P. |'")
# print("               /   "      ".d$$$P |\^")
# print("             .'           `T$P^""   :;")
# print("         ._.'      _.'              ;;")
# print("      `-.-.-'-' ._.       _.-    .-")
# print("    `.-' _____  ._   '           .-")
# print("   -(.g$$$$$$$b.              .'")
# print("     ""^^T$$$P^)            .(:")
# print("       _/  -"  '         /:/;'"")
# print("    ._.'-'`-'  /         /;/;'")
# print(" `-.-'..--''   '' /         /  ;")
# print(".-' ..--'       -'          :")
# print("..--'--.-''                 :")
# print("  ..--""              `-\(\/;`")
# print("    _.                      :")
# print("                            ;`-""")
