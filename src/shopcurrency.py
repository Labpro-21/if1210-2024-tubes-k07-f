from src.login import *
import os

from src.register import *
from src.inventories import *


def mShopList(shopCount, currentUser, mShop, mons, msTemp):
    print ("ID | Type          | ATK Power | DEF Power | HP   | Stok | Harga")
    for i in range(1,len(mShop)):
        print(
            f"{shopCount+1} | {mons[int(mShop[i][0])][1]}          | {mons[int(mShop[i][0])][2]} | {mons[int(mShop[i][0])][3]} | {mons[int(mShop[i][0])][4]}   | {mShop [i][1]} | {mShop [i][2]}")
        shopCount += 1
        stats = [shopCount, mons[int(mShop[i][0])][1], int(mons[int(mShop[i][0])][2]),
                    int(mons[int(mShop[i][0])][3]), int(mons[int(mShop[i][0])][4]), int(mShop[i][2])]
        msTemp.append(stats)
    shopCount = 0
    return msTemp, shopCount

def iShopList(shopCount, currentUser, iShop, isTemp):
    print ("ID | Type                | Stok | Harga")
    for i in range(1,len(iShop)):
        print(
            f"{shopCount+1} | {iShop[i][0]}                | {iShop[i][1]} | {iShop[i][2]}")
        shopCount += 1
        potInfo = [shopCount, iShop[i][1], int(iShop[i][2])]
    shopCount = 0
    isTemp.append(potInfo)
    return isTemp, shopCount

def cekMonster (mShop, mInv, id_monster, currentUser):
    for i in range (1,len(mInv)-1) :
        if int(mShop [id_monster][0]) == int(mInv [i][1]) and int(currentUser[0]) == int(mInv [i][0]):
            return True
    return False

def cekItem (iShop, iInv, id_potion, currentUser):
    for i in (1, len(iInv)-1) :
        if iShop [id_potion][0] == iInv [i][1] and int(currentUser[0]) == int(iInv [i][0]):
            return False
    return True

def SHOP (currentUser, mShop, iShop, mons, mInv, iInv) :
    aksi = "lihat"
    shopCount = 0
    msTemp = []
    isTemp = []
    print (f"안녕하세요! Selamat Datang di SHOP!!!")
    while aksi != "keluar" :
        aksi = str(input("Pilih aksi (lihat/beli/keluar): "))
        if aksi == "lihat" :
            jenis = str(input("Mau lihat apa? (monster/potion): "))
            print()
            if jenis == "monster" :
                mShopList(shopCount, currentUser, mShop, mons, msTemp)
            elif jenis == "potion" :
                iShopList(shopCount, currentUser, iShop, isTemp)
            print()
        elif aksi == "beli" :
            print (f"Jumlah O.W.C.A. Coin-mu sekarang {currentUser[4]}")
            print ()
            beli = str(input("Mau beli apa? (monster/potion): "))
            if beli == "monster" :
                id_monster = int(input("Masukkan id monster: "))
                if id_monster > (len(mShop)-1) : 
                    print ("Pilihan monster tidak valid.")
                    print ()
                else :
                    if mShop [id_monster][1] == 0 :
                        print ("Pembelian gagal, stok monster kurang.")
                        print ()
                    elif int(mShop [id_monster][2]) > currentUser[4] :
                        print ("OC-mu tidak cukup.")
                        print ()
                    elif cekMonster (mShop, mInv, id_monster, currentUser) :
                        print (f"Monster {mons[int(mShop[id_monster][0])][1]} sudah ada dalam inventory-mu! Pembelian dibatalkan.")
                    else :
                        print (f"Berhasil membeli item: {mons[int(mShop[id_monster][0])][1]}. Item sudah masuk ke inventory-mu!")
                        print ()
                        currentUser[4] -= int(mShop [id_monster][2])
                        mShop [id_monster][1] = int(mShop [id_monster][1]) - 1
                        mons_to_inv = [currentUser [0], mons[int(mShop[id_monster][0])][0], 1]
                        mInv.append (mons_to_inv)
            
            elif beli == "potion" :
                id_potion = int(input("Masukkan id potion: "))
                jumlah_potion = int(input("Masukkan jumlah potion: "))
                if id_potion > len(iShop)-1 : 
                    print ("Pilihan item tidak valid.")
                    print ()
                else :
                    if int(iShop [id_potion][1]) < jumlah_potion :
                        print ("Pembelian gagal, stok item kurang.")
                        print ()
                    elif int(iShop [id_potion][2])*jumlah_potion > currentUser[4] :
                        print ("OC-mu tidak cukup.")
                        print ()
                    elif cekItem (iShop, iInv, id_potion, currentUser) :
                        print(f"Berhasil membeli item: {jumlah_potion} {iShop [id_potion][0]}. Item sudah masuk ke inventory-mu!")
                        print()
                        currentUser [4] -= int(iShop [id_potion][2])*jumlah_potion
                        iShop [id_potion][1] = int(iShop [id_potion][1]) - jumlah_potion
                        item_to_inv = [currentUser[0], iShop [id_potion][0], jumlah_potion]
                        iInv.append (item_to_inv)
                        isTemp.clear()
                    else :
                        print(f"Berhasil membeli item: {jumlah_potion} {iShop [id_potion][0]}. Item sudah masuk ke inventory-mu!")
                        print()
                        currentUser [4] -= int(iShop [id_potion][2])*jumlah_potion
                        iShop [id_potion][1] = int(iShop [id_potion][1]) - jumlah_potion
                        for i in range (len(iInv)) :
                            if iShop [id_potion] == iInv [i][1] :
                                iInv [i][2] += jumlah_potion

    print("Mr. Yanto bilang makasih, belanja lagi ya nanti!!!")