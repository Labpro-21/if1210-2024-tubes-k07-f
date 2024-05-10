import os

from csv import *
from potion import *
from monster import *

currentUser = [3, 'Agen_P', 'platypus123', 'agent', 0] # sementara aja aslinya ambil dari login
mInv = read_csv(monster_inventory_filepath())
mons = read_csv(monster_filepath())
iInv = read_csv(item_inventory_filepath())


def chooseMons(userMons):
    while True:
        choice = int(input("Pilih monster untuk bertarung: "))
        print()
        monsNum = len(userMons)
        if choice > monsNum:
            print("Pilihan nomor tidak tersedia!")
            print()
        else:
            for i in range(len(userMons)):
                if choice == i+1:
                    currentMons = [userMons[i][0], userMons[i][1],
                                   userMons[i][2], userMons[i][3], userMons[i][4]]
                    break
            break
    return (currentMons)


def userPot(iInv):
    strength = 0
    resilience = 0
    healing = 0
    for i in range(1, len(iInv)):
        if int(iInv[i][0]) == int(currentUser[0]):
            if iInv[i][1] == "strength":
                strength = int(iInv[i][2])
            if iInv[i][1] == "resilience":
                resilience = int(iInv[i][2])
            if iInv[i][1] == "healing":
                healing = int(iInv[i][2])
    currentPot = [strength, resilience, healing]
    return (currentPot)


def yourTurn(mons_type, atk_power, def_power, hp, strengthBool, resilienceBool, healingBool, turnCnt, finished, currentPot):
    print(f"============ TURN {turnCnt} ({mons_type}) ============")
    print("1. Attack")
    print("2. Potion")
    print("3. Flee")
    while True:
        command = input("Pilih perintah: ")
        if int(command) == 3:
            print()
            print("Anda berhasil kabur dari BATTLE!")
            finished = True  # keluar dari battle
            break
        elif int(command) == 2:
            while True:
                type_potion = ""
                print()
                print("============ POTION LIST ============")
                print(
                    f"1. Strength Potion (Qty: {currentPot[0]}) - Increases ATK Power")
                print(
                    f"2. Resilience Potion (Qty: {currentPot[1]}) - Increases DEF Power")
                print(
                    f"3. Healing Potion (Qty: {currentPot[2]}) - Restores Health")
                print("4. Cancel")
                print()

                potCommand = input("Pilih potion atau cancel: ")
                if int(potCommand) == 1:
                    if strengthBool == True:
                        print(
                            f"Kamu mencoba memberikan ramuan ini kepada {mons_type}, namun dia menolaknya seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.")
                    elif currentPot[0] > 0:
                        type_potion = "strength"
                        print(
                            f"Setelah meminum ramuan ini, aura kekuatan terlihat mengelilingi {mons_type} dan gerakannya menjadi lebih cepat dan mematikan.")
                        strengthBool = True
                        currentPot = [currentPot[0]-1,
                                      currentPot[1], currentPot[2]]
                        break
                    else:
                        print(
                            "Wah, kamu sedang tidak memiliki ramuan ini, silahkan pilih ramuan lain!")
                elif int(potCommand) == 2:
                    if resilienceBool == True:
                        print(
                            f"Kamu mencoba memberikan ramuan ini kepada {mons_type}, namun dia menolaknya seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.")
                    elif currentPot[1] > 0:
                        type_potion = "resillence"
                        print(
                            f"Setelah meminum ramuan ini, muncul sebuah energi pelindung di sekitar {mons_type} yang membuatnya terlihat semakin tangguh dan sulit dilukai.")
                        resilienceBool = True
                        currentPot = [currentPot[0],
                                      currentPot[1]-1, currentPot[2]]
                        break
                    else:
                        print(
                            "Wah, kamu sedang tidak memiliki ramuan ini, silahkan pilih ramuan lain!")
                elif int(potCommand) == 3:
                    if healingBool == True:
                        print(
                            f"Kamu mencoba memberikan ramuan ini kepada {mons_type}, namun dia menolaknya seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.")
                    elif currentPot[2] > 0:
                        type_potion = "healing"
                        print(
                            f"Setelah meminum ramuan ini, luka-luka yang ada di dalam tubuh {mons_type} sembuh dengan cepat. Dalam sekejap, {mons_type} terlihat kembali prima dan siap melanjutkan pertempuran.")
                        healingBool = True
                        currentPot = [currentPot[0],
                                      currentPot[1], currentPot[2]-1]
                        break
                    else:
                        print(
                            "Wah, kamu sedang tidak memiliki ramuan ini, silahkan pilih ramuan lain!")
                elif int(potCommand) == 4:
                    break
                else:
                    print("Perintah tidak valid. Silahkan pilih perintah diatas!")
            if type_potion != "":
                atk_power, def_power, hp = potion(
                    type_potion, atk_power, def_power, hp)
            print()
    turnCnt += 1
    return finished


def BATTLE(mons, mInv):
    strengthBool = False
    resilienceBool = False
    healingBool = False
    chosen = mons[2]
    levelList = []
    # nanti level musuh random i guess?
    enemy = [chosen[1], chosen[2], chosen[3], chosen[4], 1]
    print("""
        _/\----/\   
        /         \     /\
      
      |  O    O   |   |  |
      |  .vvvvv.  |   |  |
      /  |     |   \  |  |
      /   `^^^^^'    \ |  |
    ./  /|            \|  |_
  /   / |         |\__     /
  \  /  |         |   |__|
    `'   |  _      |
      _.-'-' `-'-'.'_
__.-'               '-.__""")

    print(f"RAWRRR, Monster {enemy[1]} telah muncul !!!")
    print(f"""
Name      : {enemy[0]}
ATK Power : {enemy[1]}
DEF Power : {enemy[2]}
HP        : {enemy[3]}
Level     : {enemy[4]}""")

    print("============ MONSTER LIST ============")
    count = 0
    tempMons = []
    userMons = []
    for i in range(len(mInv)):
        for j in range(len(mons)):
            if str(mInv[i][0]) == str(currentUser[0]):
                if str(mInv[i][1]) == str(mons[j][0]):
                    tempMons.append(mons[j][1])       # name
                    tempMons.append(int(mons[j][2]))  # atk
                    tempMons.append(int(mons[j][3]))  # def
                    tempMons.append(int(mons[j][4]))  # hp
                    tempMons.append(int(mInv[i][2]))  # level
                    userMons.append(tempMons)
                    tempMons = []

    for i in range(len(userMons)):
        print(f"{i+1}. {userMons[i][0]}")

    currentMons = chooseMons(userMons)
    mons_type = currentMons[0]
    atk_power = currentMons[1]
    def_power = currentMons[2]
    hp = currentMons[3]
    level = currentMons[4]
    atk_power, def_power, hp = monster(atk_power, def_power, hp, level)

    print("""          
    /\----/\_   
   /         \  /|
  |  | O    O | / |
  |  | .vvvvv.|/  /
  /   | |     |   /
/    | `^^^^^   /
| /|  |         /
/ |    ___    |
    \  |   |   |
    |  |   |   |
    \._\   \._\ 
""")
    print(f"RAWRRR, Agent X mengeluarkan monster {currentMons[0]} !!!")
    print(f"""
Name      : {mons_type}
ATK Power : {atk_power}
DEF Power : {def_power}
HP        : {hp}
Level     : {level}""")

    turnCnt = 1
    finished = False
    currentPot = userPot(iInv)
    while not finished:
        finished = yourTurn(mons_type, atk_power, def_power, hp, strengthBool,
                            resilienceBool, healingBool, turnCnt, finished, currentPot)


BATTLE(mons, mInv)
