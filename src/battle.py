import os

from src.csv import *
from src.potion import *
from src.monster import *
from src.rng import *
from src.login import *


def chooseMons(userMons):
    while True:
        choice = (input("Pilih monster untuk bertarung: "))
        choice = int(choice)
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
    strengthIndex = 1
    resilienceIndex = 1
    healingIndex = 1
    for i in range(1, len(iInv)):
        if int(iInv[i][0]) == int(currentUser[0]):
            if iInv[i][1] == "strength":
                strength = int(iInv[i][2])
                strengthIndex = i
            if iInv[i][1] == "resilience":
                resilience = int(iInv[i][2])
                resilienceIndex = i
            if iInv[i][1] == "healing":
                healing = int(iInv[i][2])
                healingIndex = i
    currentPot = [strength, resilience, healing]
    return (currentPot, strengthIndex, resilienceIndex, healingIndex)

def userBall(iInv):
    monsterBall = 0
    for i in range(1, len(iInv)):
        if int(iInv[i][0]) == int(currentUser[0]):
            if iInv[i][1] == "monster_ball":
                monsterBall = int(iInv[i][2])
                ballIndex = i
    return (monsterBall, ballIndex)


def playerAtk(LCG, atk_power):
    batas_bawah = atk_power * 70 / 100
    batas_atas = atk_power * 130 / 100
    m = 2**32
    a = 82
    c = 100
    min_val = batas_bawah
    max_val = batas_atas

    seed = next_seed()
    random_integer = LCG(min_val, max_val, seed, a, c, m)
    rng = random_integer

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
    batas_atas = (enemy_atk_power * 130 / 100)

    m = 2**32
    a = 62
    c = 120
    min_val = batas_bawah
    max_val = batas_atas

    seed = next_seed()
    random_integer = LCG(min_val, max_val, seed, a, c, m)
    rng = random_integer

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


def yourTurn(mons_type, atk_power, def_power, hp, strengthBool, resilienceBool, healingBool, turnCnt, currentPot, strengthIndex, resilienceIndex, healingIndex, enemy_type, enemy_atk_power, enemy_def_power, enemy_hp, enemy_level, dmgCalc, chosenEnemy, userBall, userMons):
    end = False
    flee = False
    cancel = False
    while True:
        print(f"============ TURN {turnCnt} ({mons_type}) ============")
        print("1. Attack")
        print("2. Use Potion")
        print("3. Use Monster Ball")
        print("4. Flee")
        command = (input("Pilih perintah: "))
        command = int(command)
        if (command) == 4:
            print()
            print("Anda berhasil kabur dari BATTLE!")
            flee = True  # keluar dari battle
            break

        elif (command) == 3:
            print()
            monsterBall, ballIndex = userBall(iInv)
            alreadyHaveMons = False
            for i in range(len(userMons)):
                if enemy_type == userMons[i][0]:
                    alreadyHaveMons = True

            if alreadyHaveMons:
                print(f"Anda sudah memiliki monster {enemy_type} dalam inventory!")
                print()
                cancel = True
                break
            elif monsterBall > 0:
                monsterBall -= 1
                iInv[ballIndex][2] = int(iInv[ballIndex][2])
                iInv[ballIndex][2] -= 1
                print("Swoosshhhhh, Anda mengeluarkan Monster Ball !!!")
                capture = rngCapture(LCG,enemy_level)
                if capture:
                    print(f"Selamat, Anda berhasil mendapatkan monster {enemy_type} !!!")
                    mInv.append([currentUser[0], chosenEnemy[0], enemy_level])
                    end = True

                    print(f"""
Name      : {enemy_type}
ATK Power : {enemy_atk_power}
DEF Power : {enemy_def_power}
HP        : {enemy_hp}
Level     : {enemy_level}""")
                    print()
                    print(f"Sisa Monster Ball Anda: {monsterBall}")
                    print()
                    break
                else:
                    print(f"Yahhh, Anda belum berhasil mendapatkan monster {enemy_type} !!!")
                    print()
                    print(f"Sisa Monster Ball Anda: {monsterBall}")
                    print()
            else:
                print("Anda tidak memiliki Monster Ball dalam inventory!")

        elif (command) == 2:
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
                            iInv[strengthIndex][2] = int(iInv[strengthIndex][2])
                            iInv[strengthIndex][2] -= 1
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
                            iInv[resilienceIndex][2] = int(iInv[resilienceIndex][2])
                            iInv[resilienceIndex][2] -= 1
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
                            iInv[healingIndex][2] = int(iInv[healingIndex][2])
                            iInv[healingIndex][2] -= 1
                            break
                        else:
                            print(
                                "Wah, kamu sedang tidak memiliki ramuan ini, silahkan pilih ramuan lain!")
                    elif int(potCommand) == 4:
                        cancel = True
                        break
                    else:
                        print(
                            "Perintah tidak valid. Silahkan pilih perintah diatas!")
                if type_potion != "":
                    atk_power, def_power, hp = potion(
                        type_potion, atk_power, def_power, hp)
                print()
                break

        elif (command) == 1:
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

        else:
            print("Masukkan perintah yang valid")

    if enemy_hp <= 0:
        win = True
    else:
        win = False
    return atk_power, def_power, hp, enemy_hp, win, currentPot, strengthBool, resilienceBool, healingBool, cancel, flee, end, iInv


def enemyTurn(mons_type, atk_power, def_power, hp, level, enemy_type, enemy_atk_power, enemy_def_power, enemy_hp, enemy_level, turnCnt, dmgCalc):
    print(f"============ TURN {turnCnt} ({enemy_type}) ============")
    print()
    print(f"SCHWINKKK, {enemy_type} menyerang {mons_type} !!!")

    tempAtk, percentage = enemyAtk(LCG, enemy_atk_power)
    damagecalc, tempAtk, defcalc = dmgCalc(tempAtk, def_power, hp, percentage)
    hp = int(hp - damagecalc)
    print(f"""
Name      : {mons_type}
ATK Power : {int(atk_power)}
DEF Power : {int(def_power)}
HP        : {int(hp)}
Level     : {level}""")
    print()
    print(
        f"Penjelasan : ATT: {tempAtk} ({percentage}%), Reduced by: {defcalc} ({def_power}%), ATT Results: {int(damagecalc)}")
    print()
    if hp <= 0:
        lose = True
    else:
        lose = False
    return lose, hp


def BATTLE(mons, mInv, iInv, rngEnemy, currentUser, rngLevel):
    strengthBool = False
    resilienceBool = False
    healingBool = False
    rngEnemy = rngEnemy(LCG, mons)
    rngLevel = rngLevel(LCG)
    chosenEnemy = mons[rngEnemy]

    enemy_type = chosenEnemy[1]
    enemy_atk_power = (int(chosenEnemy[2]))
    enemy_def_power = (int(chosenEnemy[3]))
    enemy_hp = (int(chosenEnemy[4]))
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
Name      : {enemy_type}
ATK Power : {enemy_atk_power}
DEF Power : {enemy_def_power}
HP        : {enemy_hp}
Level     : {enemy_level}""")

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
    print(
        f"RAWRRR, Agent {currentUser[1]} mengeluarkan monster {mons_type} !!!")
    print(f"""
Name      : {mons_type}
ATK Power : {atk_power}
DEF Power : {def_power}
HP        : {hp}
Level     : {level}""")

    turnCnt = 1
    win = False
    lose = False
    currentPot, strengthIndex, resilienceIndex, healingIndex = userPot(iInv)
    while (not win) and (not lose):
        atk_power, def_power, hp, enemy_hp, win, currentPot, strengthBool, resilienceBool, healingBool, cancel, flee, end, iInv = yourTurn(
            mons_type, atk_power, def_power, hp, strengthBool, resilienceBool, healingBool, turnCnt, currentPot, strengthIndex, resilienceIndex, healingIndex, enemy_type, enemy_atk_power, enemy_def_power, enemy_hp, enemy_level, dmgCalc, chosenEnemy, userBall, userMons)

        if not flee:
            if not end:
                if not cancel:
                    if not win:
                        lose, hp = enemyTurn(mons_type, atk_power, def_power, hp, level, enemy_type,
                                            enemy_atk_power, enemy_def_power, enemy_hp, enemy_level, turnCnt, dmgCalc)
                        turnCnt += 1
                    else:
                        break
                else:
                    pass
            else:
                break
        else:
            break

    if win:
        rewardOC = rngOC(LCG)
        currentUser[4] = int(currentUser[4])
        (currentUser[4]) += rewardOC
        for i in range(1, len(userpas)):
            if int(userpas[i][0]) == int(currentUser[0]):
                userpas[i][4] = currentUser[4]
        print(f"Selamat, Anda berhasil mengalahkan monster {enemy_type} !!!")
        print(f"Total OC yang diperoleh: {rewardOC}")
        print()
    if lose:
        print(
            f"Yahhh, Anda dikalahkan monster {enemy_type}. Jangan menyerah, coba lagi !!!")

    return userpas, mInv, iInv

# BATTLE(mons, mInv, rngEnemy, currentUser, rngLevel)
