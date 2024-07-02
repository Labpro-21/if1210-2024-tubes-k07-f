from time import sleep
from src.login import *


def MONSTER(currentUser, userpas, mons, mInv):
    pengulangan = True
    print("SELAMAT DATANG DI DATABASE PARA MONSTER !!!")
    while pengulangan == True:
        if currentUser[3] == "admin":
            print("Available actions :")
            print("1. Tampilkan semua Monster")
            print("2. Tambah Monster baru")
            print("3. Keluar dari Monster Management")
            Aksi = int(input(">>> Pilih aksi : "))

            if Aksi == 3:
                print("Anda keluar dari monster management.")
                pengulangan = False
                return mons
            
            elif Aksi == 1:
                print("Loading database monster...")
                sleep(1.5)
                print("Database Monster")
                for i in range(len(mons)):
                    print(f"{mons[i][0]:<2} | {mons[i][1]:<14} | {mons[i][2]:<9} | {mons[i][3]:<9} | {mons[i][4]:<2}")
                print()
            elif Aksi == 2:
                print("Memulai pembuatan monster baru")

                nama_baru = input(">>> Masukkan Type / Nama : ")
                for i in range(len(mons)):
                    while nama_baru == mons[i][1]:
                        print("Nama sudah terdaftar, coba lagi!")
                        nama_baru = input(">>> Masukkan Type / Nama : ")

                atk_power = int(input(">>> Masukkan ATK Power : "))
                while atk_power != int(atk_power):
                    print("Masukkan input bertipe Integer, coba lagi!")
                    atk_power = int(input(">>> Masukkan ATK Power : "))

                def_power = int(input(">>> Masukkan DEF Power (0-50) : "))
                while def_power > 50 or def_power < 0:
                    print("DEF Power harus bernilai 0-50, coba lagi!")
                    def_power = int(input(">>> Masukkan DEF Power (0-50) : "))
                
                hp = int(input(">>> Masukkan HP : "))

                print("Monster baru berhasil dibuat!")
                print("Type : ", nama_baru)
                print("ATK Power : ", atk_power)
                print("DEF Power : ",def_power)
                print("HP : ", hp)

                add_mons = input(">>> Tambahkan Monster ke database (Y/N) : ")
                if add_mons == "Y":
                    mons.append([len(mons), nama_baru, atk_power, def_power, hp])
                    print("Monster baru telah ditambahkan!")

                elif add_mons == "N":
                    print("Monster gagal ditambahkan!")

# MONSTER(currentUser)

