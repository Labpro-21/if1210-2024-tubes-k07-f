import os

from csv import *
from potion import *
from monster import *
from rng import *

currentUser = [5, 'Kenny_agen_rahasia', 'kribogeming55',
               'agent', 6699]  # sementara aja aslinya ambil dari login
rngLevel = rngLevel(LCG)
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


def playerAtk(LCG, atk_power):
    batas_bawah = atk_power * 70 / 100
    batas_atas = atk_power * 130 / 100
    lcgList = []
    lcg = LCG(batas_bawah, batas_atas + 1)
    for _ in range(11):
        lcgList.append(lcg.generate())

    rng = (lcgList[5])
    percentage = rng / atk_power
    if percentage < atk_power/100:
        percentage = -((1 - percentage)*100)
    elif percentage > atk_power/100:
        percentage = (percentage - 1)*100
    else:
        percentage = 0
    return rng, int(percentage)


def enemyAtk(LCG, enemy_atk_power):
    batas_bawah = enemy_atk_power * 70 / 100
    batas_atas = enemy_atk_power * 130 / 100
    lcgList = []
    lcg = LCG(batas_bawah, batas_atas + 1)
    for _ in range(11):
        lcgList.append(lcg.generate())

    rng = (lcgList[6])
    percentage = rng / enemy_atk_power
    if percentage < enemy_atk_power/100:
        percentage = -((1 - percentage)*100)
    elif percentage > enemy_atk_power/100:
        percentage = (percentage - 1)*100
    else:
        percentage = 0
    return rng, int(percentage)


def dmgCalc(tempAtk, enemy_def_power, enemy_hp, percentage):
    defcalc = enemy_def_power/100 * tempAtk
    damagecalc = tempAtk - defcalc
    return damagecalc, tempAtk, defcalc


def yourTurn(mons_type, atk_power, def_power, hp, strengthBool, resilienceBool, healingBool, turnCnt, finished, currentPot, enemy_type, enemy_atk_power, enemy_def_power, enemy_hp, enemy_level, dmgCalc):
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
            if currentPot == [0, 0, 0]:
                print("Anda tidak memiliki potion dalam inventory!")
            else:
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
                break

        elif int(command) == 1:
            print()
            print(f"SCHWINKKK, {mons_type} menyerang {enemy_type} !!!")

            print(enemy_def_power)
            tempAtk, percentage = playerAtk(LCG, atk_power)
            damagecalc, tempAtk, defcalc = dmgCalc(
                tempAtk, enemy_def_power, enemy_hp, percentage)
            enemy_hp = int(enemy_hp - damagecalc)
            print(f"""
Name      : {enemy_type}
ATK Power : {enemy_atk_power}
DEF Power : {enemy_def_power}
HP        : {enemy_hp}
Level     : {enemy_level}""")
            print()
            print(
                f"Penjelasan : ATT: {tempAtk} ({percentage}%), Reduced by: {defcalc} ({enemy_def_power}%), ATT Results: {int(damagecalc)}")
            print()
            break
    return finished


def enemyTurn(mons_type, atk_power, def_power, hp, level, enemy_type, enemy_atk_power, enemy_def_power, enemy_hp, enemy_level, turnCnt, dmgCalc):
    finished = False
    print(f"============ TURN {turnCnt} ({enemy_type}) ============")
    print()
    print(f"SCHWINKKK, {enemy_type} menyerang {mons_type} !!!")

    print(def_power)
    tempAtk, percentage = enemyAtk(LCG, enemy_atk_power)
    damagecalc, tempAtk, defcalc = dmgCalc(tempAtk, def_power, hp, percentage)
    hp = int(hp - damagecalc)
    print(f"""
Name      : {mons_type}
ATK Power : {atk_power}
DEF Power : {def_power}
HP        : {hp}
Level     : {level}""")
    print()
    print(
        f"Penjelasan : ATT: {tempAtk} ({percentage}%), Reduced by: {defcalc} ({def_power}%), ATT Results: {int(damagecalc)}")
    print()
    return finished


def BATTLE(mons, mInv, rngEnemy):
    strengthBool = False
    resilienceBool = False
    healingBool = False
    rngEnemy = rngEnemy(LCG, mons)
    chosen = mons[rngEnemy-1]

    enemy_type = chosen[1]
    enemy_atk_power = (int(chosen[2]))
    enemy_def_power = (int(chosen[3]))
    enemy_hp = (int(chosen[4]))
    enemy_level = rngLevel
    enemy_atk_power, enemy_def_power, enemy_hp = monster(
        enemy_atk_power, enemy_def_power, enemy_hp, enemy_level)
    enemy = [enemy_type, enemy_atk_power,
             enemy_def_power, enemy_hp, enemy_level]
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

    print(f"RAWRRR, Monster {enemy[0]} telah muncul !!!")
    print(f"""
Name      : {enemy[0]}
ATK Power : {enemy[1]}
DEF Power : {enemy[2]}
HP        : {enemy[3]}
Level     : {enemy[4]}""")

    print("============ MONSTER LIST ============")
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
    print(f"RAWRRR, Agent X mengeluarkan monster {mons_type} !!!")
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
        finished = yourTurn(mons_type, atk_power, def_power, hp, strengthBool, resilienceBool, healingBool,
                            turnCnt, finished, currentPot, enemy_type, enemy_atk_power, enemy_def_power, enemy_hp, enemy_level, dmgCalc)
        finished = enemyTurn(mons_type, atk_power, def_power, hp, level, enemy_type,
                             enemy_atk_power, enemy_def_power, enemy_hp, enemy_level, turnCnt, dmgCalc)
        turnCnt += 1


BATTLE(mons, mInv, rngEnemy)
