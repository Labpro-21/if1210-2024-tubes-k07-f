import os

from src.isInteger import *


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

def cekItem (iShop, iInv, id_item, currentUser):
    Bool = True
    for i in range (1, len(iInv)-1) :
        if str(iShop [id_item][0]) == str(iInv [i][1] ) and int(currentUser[0]) == int(iInv [i][0]):
            Bool = False
    return Bool
    

def SHOP (currentUser, mShop, iShop, mons, mInv, iInv) :
    aksi = "lihat"
    shopCount = 0
    msTemp = []
    isTemp = []
    print (f"안녕하세요! Selamat Datang di SHOP!!!")
    while aksi != "keluar" :
        aksi = str(input("Pilih aksi (lihat/beli/keluar): "))
        if aksi == "lihat" :
            jenis = str(input("Mau lihat apa? (monster/item): "))
            print()
            if jenis == "monster" :
                mShopList(shopCount, currentUser, mShop, mons, msTemp)
            elif jenis == "item" :
                iShopList(shopCount, currentUser, iShop, isTemp)
            print()
        elif aksi == "beli" :
            print (f"Jumlah O.W.C.A. Coin-mu sekarang {currentUser[4]}")
            print ()
            beli = str(input("Mau beli apa? (monster/item): "))
            if beli == "monster" :
                id_monster = (input("Masukkan id monster: "))
                if is_integer(id_monster):
                    id_monster = int(id_monster)
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
                else:
                    print("Input harus berupa integer.")
                    print()
            
            elif beli == "item" :
                id_item = (input("Masukkan id item: "))
                if is_integer(id_item):
                    id_item = int(id_item)
                    jumlah_item = (input("Masukkan jumlah item: "))
                    if is_integer(jumlah_item):
                        jumlah_item = int(jumlah_item)
                        if id_item > len(iShop)-1 : 
                            print ("Pilihan item tidak valid.")
                            print ()
                        else :
                            itemCek = cekItem (iShop, iInv, id_item, currentUser) 
                            if int(iShop [id_item][1]) < jumlah_item :
                                print ("Pembelian gagal, stok item kurang.")
                                print ()
                            elif int(iShop [id_item][2])*jumlah_item > currentUser[4] :
                                print ("OC-mu tidak cukup.")
                                print ()
                            elif itemCek:
                                print(f"Berhasil membeli item: {jumlah_item} {iShop [id_item][0]}. Item sudah masuk ke inventory-mu!")
                                print()
                                currentUser [4] -= int(iShop [id_item][2])*jumlah_item
                                iShop [id_item][1] = int(iShop [id_item][1]) - jumlah_item
                                item_to_inv = [currentUser[0], iShop [id_item][0], jumlah_item]
                                iInv.append (item_to_inv)
                                isTemp.clear()
                            else :
                                print(f"Berhasil membeli item: {jumlah_item} {iShop [id_item][0]}. Item sudah masuk ke inventory-mu!")
                                print()
                                currentUser [4] -= int(iShop [id_item][2])*jumlah_item
                                iShop [id_item][1] = int(iShop [id_item][1]) - jumlah_item
                                for i in range (len(iInv)) :
                                    if str(currentUser[0]) == str(iInv[i][0]):
                                        if iShop [id_item][0] == iInv [i][1] :
                                            iInv[i][2] = int(iInv[i][2])
                                            iInv[i][2] += jumlah_item
                    else:
                        print("Input harus berupa integer")
                        print()
                else:
                    print("Input harus berupa integer")
                    print()

    print("Mr. Yanto bilang makasih, belanja lagi ya nanti!!!")