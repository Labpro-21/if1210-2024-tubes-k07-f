import os
from src.load import *
from time import sleep


def write_csv(folder_path, csv_file, array_data):
    # Membuka file csv
    with open(folder_path + "/" + csv_file, "w", newline="") as file:
        for i in range(len(array_data)):
            line = ""
            for j in range(len(array_data[i])):
                line += str(array_data[i][j])
                if j < len(array_data[i])-1:
                    line += ";"
                else:
                    line += "\n"
            file.write(line)


def save_data(userpas, mons, mShop, mInv, iShop, iInv):
    folder_name = input("Masukkan nama folder : ")
    data_directory = os.path.dirname(__file__) + "/../data/"
    folder_path = data_directory + f"/{folder_name}"
    if os.path.exists(data_directory):
        if os.path.exists(folder_path):
            print(f"Folder /data/{folder_name} sudah ada.")
            sleep(1)
        # Save CSV file
            write_csv(folder_path, "user.csv", userpas)
            write_csv(folder_path, "monster.csv", mons)
            write_csv(folder_path, "monster_shop.csv", mShop)
            write_csv(folder_path, "monster_inventory.csv", mInv)
            write_csv(folder_path, "item_shop.csv", iShop)
            write_csv(folder_path, "item_inventory.csv", iInv)
            print(f"Data berhasil disimpan ke folder /data/{folder_name}.")

        else:  # Pembuatan folder baru karena nama folder tidak ada
            os.makedirs(folder_path)
            print(f"Membuat folder /data/{folder_name}...")
            sleep(1)

            write_csv(folder_path, "user.csv", userpas)
            write_csv(folder_path, "monster.csv", mons)
            write_csv(folder_path, "monster_shop.csv", mShop)
            write_csv(folder_path, "monster_inventory.csv", mInv)
            write_csv(folder_path, "item_shop.csv", iShop)
            write_csv(folder_path, "item_inventory.csv", iInv)
            print(f"Data berhasil disimpan ke folder /data/{folder_name}.")

    else:  # Buat folder "data"
        print("Folder data tidak ditemukan.")
        print(f"Membuat folder /data/...")
        sleep(1)
        os.makedirs(data_directory)
        print(f"Folder /data berhasil dibuat")
        print(f"Membuat folder /data/{folder_name}...")
        sleep(1)
        os.makedirs(folder_path)

        # Write CSV data to files
        write_csv(folder_path, "user.csv", userpas)
        write_csv(folder_path, "monster.csv", mons)
        write_csv(folder_path, "monster_shop.csv", mShop)
        write_csv(folder_path, "monster_inventory.csv", mInv)
        write_csv(folder_path, "item_shop.csv", iShop)
        write_csv(folder_path, "item_inventory.csv", iInv)
        print("Data berhasil disimpan ke folder /data/" + folder_name)

