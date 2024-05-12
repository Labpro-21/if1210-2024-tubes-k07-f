import os
import argparse

class Game:
    def __init__(self):
        self.users_file = "data/user.csv"
        self.monster_inventory_file = "data/monster_inventory.csv"
        self.item_inventory_file = "data/item_inventory.csv"
        self.monster_shop_file = "data/monster_shop.csv"
        self.item_shop_file = "data/item_shop.csv"
        self.koin_file = "data/koin.csv"

    def load_data(self, folder):
        folder_path = os.path.join("data", folder)
        if not os.path.exists(folder_path):
            print(f"Folder \"{folder}\" tidak ditemukan.")
            return False

        print("Loading...")
        print("Selamat datang di program OWCA!")
        return True

def main():
    parser = argparse.ArgumentParser(description="Load data for OWCA program.")
    parser.add_argument("folder", metavar="nama_folder", type=str, help="Nama folder yang berisi file penyimpanan.")
    args = parser.parse_args()

    game = Game()
    if not args.folder:
        print("Tidak ada nama folder yang diberikan!")
        parser.print_usage()
        return

    game.load_data(args.folder)

if __name__ == "__main__":
    main()
