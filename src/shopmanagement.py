from src.login import *
import os

from src.register import *
from src.inventories import *


def mShopList(shopCount, mShop, mons, msTemp):
    print("ID | Type          | ATK Power | DEF Power | HP   | Stok | Harga")
    for i in range(1, len(mShop)):
        print(
            f"{shopCount+1} | {mons[int(mShop[i][0])][1]}          | {mons[int(mShop[i][0])][2]} | {mons[int(mShop[i][0])][3]} | {mons[int(mShop[i][0])][4]}   | {mShop [i][1]} | {mShop [i][2]}")
        shopCount += 1
        stats = [shopCount, mons[int(mShop[i][0])][1], int(mons[int(mShop[i][0])][2]),
                 int(mons[int(mShop[i][0])][3]), int(mons[int(mShop[i][0])][4]), int(mShop[i][2])]
        msTemp.append(stats)
    shopCount = 0
    return msTemp, shopCount


def notmShopList(shopCount, mShop, mons, nmsTemp):
    if len(mons) == len(mShop):
        print("Semua monster sudah ada di shop")
    else:
        id_mons_to_shop = 0
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
                id_mons_to_shop = mons[i][0]
                nmsTemp.append(stats)
                processed_ids.add(mons[i][0])
        shopCount = 0
    return nmsTemp, shopCount, id_mons_to_shop


def iShopList(shopCount, iShop, isTemp):
    print("ID | Type                | Stok | Harga")
    for i in range(1, len(iShop)):
        print(
            f"{shopCount+1} | {iShop[i][0]}                | {iShop[i][1]} | {iShop[i][2]}")
        shopCount += 1
        potInfo = [shopCount, iShop[i][1], int(iShop[i][2])]
    shopCount = 0
    isTemp.append(potInfo)
    return isTemp, shopCount


def notiShopList(shopCount, iShop, nisTemp, item):
    if len(iShop) == len(item):
        print("Semua item tersedia di shop.")
    else:
        processed_ids = set()
        shopCount = len(iShop) - 1
        print("ID | Type                |")
        for i in range(1, len(item)):
            is_in_shop = False
            for j in range(1, len(iShop)):
                if item[i][1] == iShop[j][0]:
                    is_in_shop = True
                    break
            if not is_in_shop and item[i][1] not in processed_ids:
                print(
                    f"{shopCount+1}  | {item[i][1]}")
                shopCount += 1
                stats = [shopCount, item[i][1]]
                nisTemp.append(stats)
                processed_ids.add(item[i][1])
        shopCount = 0
    return nisTemp, shopCount


def SHOP_MANAGEMENT(currentUser, mShop, iShop, mons, item):
    item = [[1, "strength"], [2, "resilience"], [3, "healing"], [4, "monster_ball"], [1,1]]
    action = "lihat"
    shopCount = 0
    id_mons_to_shop = 0
    msTemp = []
    nmsTemp = []
    isTemp = []
    nisTemp = []
    mons_to_shop = []
    item_to_shop = []
    print(f"안녕하세요! Selamat datang kembali, {currentUser [1]}")

    while action != "keluar":
        action = str(
            input(">>> Pilih aksi (lihat/tambah/ubah/hapus/keluar): "))

        if action == "lihat":
            jenis = str(input(">>> Mau lihat apa? (monster/item): "))
            if jenis == "monster":
                msTemp, shopCount = mShopList(shopCount, mShop, mons, msTemp)
            elif jenis == "item":
                isTemp, shopCount = iShopList(shopCount, iShop, isTemp)

        elif action == "tambah":
            jenis_tambah = str(
                input(">>> Mau nambahin apa? (monster/item): "))

            if jenis_tambah == "monster":
                nmsTemp, shopCount, id_mons_to_shop = notmShopList(
                    shopCount, mShop, mons, nmsTemp)
                id_mons = int(input(">>> Masukkan id monster: "))
                stok_mons = int(input(">>> Masukkan stok awal: "))
                price_mons = int(input(">>> Masukkan harga: "))
                print(
                    f"{nmsTemp [id_mons-len(mShop)][1]} telah berhasil ditambahkan ke dalam shop! ")
                mons_to_shop.append(id_mons_to_shop)
                mons_to_shop.append(stok_mons)
                mons_to_shop.append(price_mons)
                mShop.append(mons_to_shop)

            elif jenis_tambah == "item":
                nisTemp, shopCount = notiShopList(
                    shopCount, iShop, nisTemp, item)
                id_pot = int(input(">>> Masukkan id item: "))
                stok_pot = int(input(">>> Masukkan stok awal: "))
                price_pot = int(input(">>> Masukkan harga: "))
                print(
                    f"{nisTemp [id_pot-len(iShop)][1]} telah berhasil ditambahkan ke dalam shop! ")
                item_to_shop.append(nisTemp[id_pot-len(iShop)][1])
                item_to_shop.append(stok_pot)
                item_to_shop.append(price_pot)
                iShop.append(item_to_shop)

        elif action == "ubah":
            jenis_ubah = str(input(">>> Mau ubah apa? (monster/item): "))

            if jenis_ubah == "monster":
                mShopList(shopCount, mShop, mons, msTemp)
                id_mons_new = int(input(">>> Masukkan id monster: "))
                stok_mons_new = input(">>> Masukkan stok baru: ")
                price_mons_new = input(">>> Masukkan harga baru: ")
                for i in range(len(mons)):
                    if mons[i][1] == msTemp[id_mons_new][1]:
                        selectedMons = mons[i-1][1]
                        if stok_mons_new != "" and price_mons_new != "":
                            mShop[id_mons_new][1] = int(stok_mons_new)
                            mShop[id_mons_new][2] = int(price_mons_new)
                            print(
                                f"{selectedMons} telah berhasil diubah dengan stok baru sejumlah {stok_mons_new} dan dengan harga baru {price_mons_new}!")
                        elif stok_mons_new != "" and price_mons_new == "":
                            mShop[id_mons_new][1] = int(stok_mons_new)
                            print(
                                f"{selectedMons} telah berhasil diubah dengan stok baru sejumlah {stok_mons_new}!")
                        elif stok_mons_new == "" and price_mons_new != "":
                            mShop[id_mons_new][2] = int(price_mons_new)
                            print(
                                f"{selectedMons} telah berhasil diubah dengan harga baru {price_mons_new}!")

            if jenis_ubah == "item":
                iShopList(shopCount, iShop, isTemp)
                id_pot_new = int(input(">>> Masukkan id item: "))
                stok_pot_new = input(">>> Masukkan stok baru: ")
                price_pot_new = input(">>> Masukkan harga baru: ")
                for i in range(len(item)):
                    if item[i][1] == iShop[id_pot_new][0]:
                        selectedPot = item[i][1]
                        if stok_pot_new != "" and price_pot_new != "":
                            iShop[id_pot_new][1] = int(stok_pot_new)
                            iShop[id_pot_new][2] = int(price_pot_new)
                            print(
                                f"{selectedPot} telah berhasil diubah dengan stok baru sejumlah {stok_pot_new} dan dengan harga baru {price_pot_new}!")
                        elif stok_pot_new != "" and price_pot_new == "":
                            iShop[id_pot_new][1] = int(stok_pot_new)
                            print(
                                f"{selectedPot} telah berhasil diubah dengan stok baru sejumlah {stok_pot_new}!")
                        elif stok_pot_new == "" and price_pot_new != "":
                            iShop[id_pot_new][2] = int(price_pot_new)
                            print(
                                f"{selectedPot} telah berhasil diubah dengan harga baru {price_pot_new}!")

        elif action == "hapus":
            jenis_hapus = str(input(">>> Mau hapus apa? (monster/item): "))

            if jenis_hapus == "monster":
                mShopList(shopCount, mShop, mons, msTemp)
                id_mons_delete = int(input(">>> Masukkan id monster: "))
                selectedmShopid = int(mShop[id_mons_delete][0])
                selectedMons = mons[selectedmShopid][1]
                mons_confirm = input(
                    f">>> Apakah anda yakin ingin menghapus {selectedMons} dari shop (y/n)? ")
                if mons_confirm == "y":
                    mShop.pop(selectedmShopid-1)
                elif mons_confirm == "n":
                    print(f"Gagal menghapus {selectedMons} dari shop")

            if jenis_hapus == "item":
                iShopList(shopCount, iShop, isTemp)
                id_pot_delete = int(input(">>> Masukkan id item: "))
                for i in range(len(item)):
                    if item[i][1] == iShop[id_pot_delete][0]:
                        selectedPot = item[i][1]
                pot_confirm = input(
                    f">>> Apakah anda yakin ingin menghapus {selectedPot} dari shop (y/n)? ")
                if pot_confirm == "y":
                    for i in range(len(iShop)):
                        if iShop[i][0] == selectedPot:
                            iShop.pop(id_pot_delete)
                    print(f"Item telah berhasil dihapus dari shop!")
                elif pot_confirm == "n":
                    print(f"Gagal menghapus {selectedPot} dari shop")