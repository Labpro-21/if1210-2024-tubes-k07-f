from src.login import *
import os

from src.csv import *
from src.register import *
from src.inventories import *

mons = read_csv(monster_filepath())
mShop = read_csv(monster_shop_filepath())
iShop = read_csv(item_shop_filepath())

def mShopList(shopCount, mShop, mons, msTemp):
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

def notmShopList(shopCount, mShop, mons, nmsTemp):
    processed_ids = set()
    shopCount = len(mShop) - 1
    print("ID | Type          | ATK Power | DEF Power | HP   |")
    for i in range(1, len(mons)): 
        is_in_shop = False
        for j in range(1, len(mShop)):
            if mons[i][0] == mShop[j][0]:
                is_in_shop = True
                break
        if not is_in_shop and mons[i][0] not in processed_ids:
            print(
                f"{shopCount+1} | {mons[i][1]}          | {mons[i][2]} | {mons[i][3]} | {mons[i][4]}")
            shopCount += 1
            stats = [shopCount, mons[i][1], int(mons[i][2]),
                     int(mons[i][3]), int(mons[i][4])]
            id_mons_to_shop = mons [i][0]
            nmsTemp.append(stats)
            processed_ids.add(mons[i][0])
    shopCount = 0
    return nmsTemp, shopCount, id_mons_to_shop

def iShopList(shopCount,iShop, isTemp):
    print ("ID | Type                | Stok | Harga")
    for i in range(1,len(iShop)):
        print(
            f"{shopCount+1} | {iShop[i][0]}                | {iShop[i][1]} | {iShop[i][2]}")
        shopCount += 1
        potInfo = [shopCount, iShop[i][1], int(iShop[i][2])]
    shopCount = 0
    isTemp.append(potInfo)
    return isTemp, shopCount

def notiShopList(shopCount, iShop, nisTemp):
    processed_ids = set()
    shopCount = len(iShop) - 1
    print("ID | Type                |")
    for i in range(1, len(iShop)):
        if iShop[i][0] not in processed_ids:
            print(f"{shopCount+1} | {iShop[i][0]}")
            shopCount += 1
            potInfo = [shopCount, iShop[i][1], int(iShop[i][2])]
            nisTemp.append(potInfo)
            processed_ids.add(iShop[i][0])
    shopCount = 0
    return nisTemp, shopCount

def SHOP_MANAGEMENT (currentUser, mShop, iShop, mons) :
    action = "lihat"
    shopCount = 0
    id_mons_to_shop = 0
    msTemp = []
    nmsTemp = []
    isTemp = []
    nisTemp = []
    mons_to_shop = []
    item_to_shop = []
    print (f"안녕하세요! Selamat datang kembali, {currentUser [1]}")
    while action != "keluar" :
        action = str(input("Pilih aksi (lihat/tambah/ubah/hapus/keluar): "))
        if action == "lihat" :
            jenis = str(input("Mau lihat apa? (monster/potion): "))
            if jenis == "monster" :
                mShopList(shopCount, mShop, mons, msTemp)
            elif jenis == "potion" :
                iShopList(shopCount,iShop, isTemp)
        elif action == "tambah" :
            jenis_tambah = str(input("Mau nambahin apa? (monster/potion): "))
            if jenis_tambah == "monster" :
                notmShopList(shopCount, mShop, mons, nmsTemp)
                id_mons = int(input("Masukkan id monster: "))
                stok_mons = int(input("Masukkan stok awal: "))
                price_mons = int(input("Masukkan harga: "))
                print (f"{nmsTemp [id_mons-len(mShop)][1]} telah berhasil ditambahkan ke dalam shop! ")
                mons_to_shop.append (id_mons_to_shop)
                mons_to_shop.append (stok_mons)
                mons_to_shop.append (price_mons)
                mShop.append (mons_to_shop)
            elif jenis_tambah == "potion" :
                notiShopList (shopCount,iShop, nisTemp)
                id_pot = int(input("Masukkan id potion: "))
                stok_pot = int(input("Masukkan stok awal: "))
                price_pot = int(input("Masukkan harga: "))
                print (f"{nisTemp [id_pot-len(iShop)][1]} telah berhasil ditambahkan ke dalam shop! ")