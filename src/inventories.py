from src.login import *  # MASIH PERLU DI FIX INVENTORY
import os

from src.csv import *
from src.register import *

mons = read_csv(monster_filepath())
iInv = read_csv(item_inventory_filepath())


def mInvList(invCount, currentUser, mInv, mons, mTemp):
    for i in range(len(mInv)):
        for j in range(len(mons)):
            if str(mInv[i][0]) == str(currentUser[0]):
                if str(mInv[i][1]) == str(mons[j][0]):
                    print(
                        f"{invCount+1}. Monster       (Name: {mons[j][1]}, Lvl: {mInv[j][2]}, HP: {mons[j][4]})")
                    invCount += 1
                    stats = [invCount, mons[j][1], int(mons[j][2]),
                             int(mons[j][3]), int(mons[j][4]), int(mInv[i][2])]
                    mTemp.append(stats)
    return mTemp


def iInvList(invCount, currentUser, iInv, mons, iTemp):
    for i in range(len(iInv)):
        if str(iInv[i][0]) == str(currentUser[0]):
            print(
                f"{invCount+1}. Potion        (Type: {iInv[i][1]}, Qty: {iInv[i][2]})")
            invCount += 1
            potInfo = [invCount, iInv[i][1], int(iInv[i][2])]
            iTemp.append(potInfo)
    return iTemp


def INVENTORY(currentUser, mInv, iInv, mons):
    print(
        f"============ INVENTORY LIST (User ID: {currentUser[0]}) ============")
    print(f"Jumlah O.W.C.A. Coin-mu sekarang {currentUser[4]}")
    invCount = 0
    mTemp = []
    iTemp = []

    mInvList(invCount, currentUser, mInv, mons, mTemp)
    invCount += len(mTemp)
    iInvList(invCount, currentUser, iInv, mons, iTemp)
    invCount += len(iTemp)

    if len(mTemp) == 0 and len(iTemp) == 0:
        inventoryBool = False
    else:
        inventoryBool = True
    print()

    if inventoryBool:
        while True:
            print("Masukkan pilihan sesuai angka diatas atau 'KELUAR'")
            pilihanInv = input(">> ")
            try:
                pilihanInv = int(pilihanInv)
                if pilihanInv == 0:
                    print()
                elif invCount == 1 and pilihanInv > 1:
                    print("Pilihan hanyalah 1 dan 'KELUAR'")
                    print()
                elif int(pilihanInv) > invCount:
                    print(f"Pilihan hanyalah 1-{invCount} dan 'KELUAR'")
                    print()
                elif int(pilihanInv) <= int(len(mTemp)):
                    for i in range(len(mTemp)):
                        if int(pilihanInv) == mTemp[i][0]:
                            print("Monster")
                            print(f"Name      : {mTemp[i][1]}")
                            print(f"ATK Power : {mTemp[i][2]}")
                            print(f"Def Power : {mTemp[i][3]}")
                            print(f"HP        : {mTemp[i][4]}")
                            print(f"Level     : {mTemp[i][5]}")
                            print()
                            break
                elif int(pilihanInv) > int(len(mTemp)):
                    for i in range(len(iTemp)):
                        if int(pilihanInv) == iTemp[i][0]:
                            print("Potion")
                            print(f"Type      : {iTemp[i][1]}")
                            print(f"Quantity  : {iTemp[i][2]}")
                            print()
                            break
            except ValueError:
                if pilihanInv.upper() == "KELUAR":
                    print()
                    break
                else:
                    print()

# INVENTORY(currentUser, mInv, iInv, mons)
