# TUBES DASPRO ----------------------------------------------------------------------------------
import os
import sys
import time
import math
import argparse
import datetime

from src.csv import *
from src.rng import *
from src.register import *
from src.login import *
from src.logout import *
from src.help import *
from src.inventories import *
from src.shopcurrency import *
from src.shopmanagement import *
from src.battle import *
from src.arena import *
from src.monster import *

print("SELAMAT DATANG PADA PROGRAM YANG SEDANG DALAM PERCOBAAN INI!!!")
while True:
    pilihan = input(">>> ")
    if pilihan.upper() == "REGISTER":
        REGISTER(cnt)
    if pilihan.upper() == "LOGIN":
        LOGIN(loginBool, wrongUsername, wrongPassword, userpas)
    if pilihan.upper() == "LOGOUT":
        LOGOUT(currentUser)
    if pilihan.upper() == "HELP":
        HELP(currentUser)
    if pilihan.upper() == "INVENTORY":
        INVENTORY(currentUser, mInv, iInv, mons)
    if pilihan.upper() == "SHOP":
        SHOP(currentUser, mShop, iShop, mons)
    if pilihan.upper() == "SHOP MANAGEMENT" :
        SHOP_MANAGEMENT (currentUser, mShop, iShop, mons)
    if pilihan.upper() == "BATTLE" :
        BATTLE(mons, mInv, rngEnemy, currentUser, rngLevel, iInv)
    if pilihan.upper() == "ARENA" :
        ARENA(mons, mInv, rngEnemy, currentUser, rngLevel)
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