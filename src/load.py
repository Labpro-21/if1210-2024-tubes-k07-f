import os
import sys
import argparse
from time import sleep
from src.save import *

def read_csv(filename, folder_path):
    # Manually construct the file path
    if folder_path[-1] != "/":
        folder_path += "/"
    file_path = folder_path + filename

    data = []

    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"Error: The file {filename} was not found in the folder {folder_path}.")
        return data

    # Open and read the CSV file
    with open(file_path, mode='r', newline='') as file:
        for line in file:
            row = []
            cell = ""
            for char in line:
                if char == '\n' or char == '\r':
                    continue
                if char == ';':
                    row.append(cell)
                    cell = ""
                else:
                    cell += char
            if cell:
                row.append(cell)  # Append the last cell
            data.append(row)

    return data


def show_folders():
    data_directory = os.path.dirname(__file__) + "/../data/"
    available_folders = os.listdir(data_directory)
    print("Daftar folder penyimpanan yang tersedia:")
    for i in range(len(available_folders)):
        print(f"{i+1}. {available_folders[i]}")

# Fungsi melakukan load folder penyimpanan


def load(folder):
    data_directory = os.path.dirname(__file__) + "/../data/"
    folder_path = data_directory + folder
    file_csv = ["user.csv", "monster.csv", "item_inventory.csv",
                "monster_inventory.csv", "item_shop.csv", "monster_shop.csv"]
    if os.path.exists(folder_path):  # Jika nama folder ada di /data/
        missing_file = False
        # Mengecek apakah ada file csv yang missing dalam folder yang dipilih
        for i in range(len(file_csv)):
            if os.path.exists(os.path.join(folder_path, file_csv[i])) == False:
                missing_file = True

        if missing_file:  # Jika ada missing file
            print()
            print("Salah satu file .csv dalam folder ini tidak ada! Cek kembali isi folder anda!")
            print()

        else:  # Jika tidak ada missing file
            valid_load = True
            print()
            print("Loading...")
            sleep(1)
            # Load user.csv
            userpas = read_csv("user.csv", folder_path)

            # Load monster.csv
            mons = read_csv("monster.csv", folder_path)

            # Load monster_inventory.csv
            mInv = read_csv("monster_inventory.csv", folder_path)

            # Load item_inventory.csv
            iInv = read_csv("item_inventory.csv", folder_path)

            # Load item_shop.csv
            iShop = read_csv("item_shop.csv", folder_path)

            # Load monster_shop.csv
            mShop = read_csv("monster_shop.csv", folder_path)

            print("Selamat datang di program OWCA!")
            print(
                "Anda belum login, ketik 'HELP' untuk melihat command-command yang available!")
            valid_load = True
            return userpas, mons, iInv, mInv, iShop, mShop, valid_load

    else:  # Jika nama folder tidak valid
        print()
        print(f"Folder {folder} tidak dapat ditemukan!")
        show_folders()
        print()
        sys.exit()

# Fungsi membuat folder penyimpanan baru dan melakukan load game files apabila user memilih NEWGAME


def start():
    parser = argparse.ArgumentParser(
        description="Load Data Program OWCA. Format: python main.py <nama_folder>. Tulis NEWGAME pada <nama_folder> untuk membuat folder baru.")
    parser.add_argument(
        "folder", help="Nama folder tempat penyimpanan data program")
    args = parser.parse_args()

    if not args.folder:  # Jika tidak diinput (nama_folder)
        print("Masukkan nama folder tempat penyimpanan data program Anda!")
        print("Pertama kali bermain? Tulis NEWGAME pada <nama_folder>!")
        print("Usage: python main.py <nama_folder>")
        print()
        show_folders()

    else:  # Jika input (nama_folder)
        return load(args.folder)
    # python main.py <"folder">
