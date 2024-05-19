def playerMons(mInv, mons, currentUser):
    monsters = []
    for i in range(1, len(mInv)):
        for j in range(1, len(mons)):
            if int(mInv[i][0]) == int(currentUser[0]):
                if str(mInv[i][1]) == str(mons[j][0]):
                    monsters.append([mons[j][1], int(mInv[i][2])])
    return monsters


upgrade_prices = {
    2: 300,
    3: 500,
    4: 800,
    5: 1000
}


def display_monster(monsters):
    print("\n============ MONSTER LIST ============")
    for idx, monster in enumerate(monsters, 1):
        print(f"{idx}. {monster[0]} (Level: {monster[1]})")


def upgrade_monster(currency, monsters, currentUser, mons, mInv, userpas):
    display_monster(monsters)
    monster_choice = int(input(">>> Pilih monster: ")) - 1

    if monster_choice < 0 or monster_choice >= len(monsters):
        print("Pilihan monster tidak valid.")
        return

    monster = monsters[monster_choice]
    if monster[1] >= 5:
        print("Maaf, monster sudah mencapai level maksimum.")
        return

    upgrade_price = upgrade_prices.get(monster[1] + 1)

    print(f"{monster[0]} akan di-upgrade ke level {monster[1] + 1}.")
    print(
        f"Harga untuk melakukan upgrade {monster[0]} adalah {upgrade_price} OC.")

    confirm = input(">>> Lanjutkan upgrade (Y/N): ").upper()
    if confirm == "Y":
        if currency >= upgrade_price:
            currency -= upgrade_price
            currentUser[4] = int(currentUser[4])
            currentUser[4] = currency
            for i in range(1, len(userpas)):
                if userpas[i][0] == currentUser[0]:
                    userpas[i][4] = int(userpas[i][4])
                    userpas[i][4] = currency

            monster[1] += 1
            breakout = False
            for i in range(1, len(mInv)):
                for j in range(1, len(mons)):
                    if (str(mInv[i][0]) == str(currentUser[0])):
                        if (mons[j][1] == monster[0]):
                            if str(mons[j][0]) == str(mInv[i][1]):
                                print (mons[j][1], monster[0])
                                print(mInv[i][2])
                                mInv[i][2] = int(mInv[i][2])
                                mInv[i][2] += 1
                                breakout = True
                                break
                if breakout:
                    break
            print(mInv)
            print(
                f"Selamat, {monster[0]} berhasil di-upgrade ke level {monster[1]}!")
        else:
            print("Maaf, Anda tidak memiliki cukup OC untuk melakukan upgrade.")
    else:
        print("Upgrade dibatalkan.")
    return currency, userpas, mInv


def LABORATORY(userpas, mInv, mons, currentUser):
    print("Selamat datang di Lab Dokter Asep !!!")
    monsters = playerMons(mInv, mons, currentUser)
    display_monster(monsters)

    currency = int(currentUser[4])
    print("\n============ UPGRADE PRICE ============")
    for level, price in upgrade_prices.items():
        print(f"{level - 1}. Level {level - 1} -> Level {level}: {price} OC")
    print("=======================================")

    while True:
        print("\nApa yang ingin Anda lakukan?")
        print("1. Upgrade monster")
        print("2. Exit")

        choice = input(">>> Masukkan pilihan (1/2): ").strip()

        if choice == "1":
            currency, userpas, mInv = upgrade_monster(
                currency, monsters, currentUser, mons, mInv, userpas)
        elif choice == "2":
            print("Terima kasih telah menggunakan Lab Dokter Asep!")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan angka 1 atau 2.")


# if __name__ == "__main__":
#     LABORATORY(userpas, mInv, mons)
