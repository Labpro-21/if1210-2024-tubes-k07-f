import os

from src.csv import *
from src.potion import *
from src.monster import *
from src.rng import *
from src.login import *
from src.inventories import *
from src.battle import *

reward = [[1, 30], [2, 50], [3, 100], [4, 160], [5, 250]]

def mInvList(invCount, currentUser, mInv, mons, mTemp):
    for i in range(len(mInv)):
        for j in range(len(mons)):
            if str(mInv[i][0]) == str(currentUser[0]):
                if str(mInv[i][1]) == str(mons[j][0]):
                    print(
                        f"{invCount+1}. Monster       (Name: {mons[j][1]}, Lvl: {mInv[j][2]}, HP: {mons[j][4]})")
                    invCount += 1
                    stats = [invCount, mons[j][1], int(mons[j][2]),
                             int(mons[j][3]), int(mons[j][4]), int(mInv[i][2])]
                    mTemp.append(stats)
    return mTemp


def yourTurnArena(mons_type, atk_power, def_power, hp, strengthBool, resilienceBool, healingBool, turnCnt, currentPot, enemy_type, enemy_atk_power, enemy_def_power, enemy_hp, enemy_level, dmgCalc, damage_given):
    flee = False
    cancelPot = False
    print(f"============ TURN {turnCnt} ({mons_type}) ============")
    print("1. Attack")
    print("2. Potion")
    print("3. Flee")
    while True:
        try:
            command = (input("Pilih perintah: "))
            command = int(command)
            if (command) == 3:
                print()
                print("GAME OVER! Anda mengakhiri sesi latihan!")
                flee = True  # keluar dari battle
                break

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
                            cancelPot = True
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
                tempAtk, percentage = playerAtk(LCG, atk_power)
                damagecalc, tempAtk, defcalc = dmgCalc(
                    tempAtk, enemy_def_power, enemy_hp, percentage)
                enemy_hp = int(enemy_hp - damagecalc)
                damage_given += damagecalc
                if enemy_hp > 0 :
                    print(f"""
        Name      : {enemy_type}
        ATK Power : {enemy_atk_power}
        DEF Power : {enemy_def_power}
        HP        : {enemy_hp}
        Level     : {enemy_level}""")
                else :
                    print(f"""
    Name      : {enemy_type}
    ATK Power : {enemy_atk_power}
    DEF Power : {enemy_def_power}
    HP        : 0
    Level     : {enemy_level}""")
                print()
                print(
                    f"Penjelasan : ATT: {tempAtk} ({percentage}%), Reduced by: {defcalc} ({enemy_def_power}%), ATT Results: {int(damagecalc)}")
                print()
                break

            else:
                print("Masukkan perintah yang valid")
        except ValueError:
            print("Masukkan perintah yang valid!")
            print()

    if enemy_hp <= 0:
        win = True
    else:
        win = False
    return atk_power, def_power, hp, enemy_hp, win, currentPot, strengthBool, resilienceBool, healingBool, cancelPot, flee, damage_given


def enemyTurnArena(mons_type, atk_power, def_power, hp, level, enemy_type, enemy_atk_power, enemy_def_power, enemy_hp, enemy_level, turnCnt, dmgCalc, damage_received):
    print(f"============ TURN {turnCnt} ({enemy_type}) ============")
    print()
    print(f"SCHWINKKK, {enemy_type} menyerang {mons_type} !!!")

    tempAtk, percentage = enemyAtk(LCG, enemy_atk_power)
    damagecalc, tempAtk, defcalc = dmgCalc(tempAtk, def_power, hp, percentage)
    hp = int(hp - damagecalc)
    damage_received += damagecalc
    if hp > 0 :
        print(f"""
    Name      : {mons_type}
    ATK Power : {int(atk_power)}
    DEF Power : {int(def_power)}
    HP        : {int(hp)}
    Level     : {level}""")
    else :
        print(f"""
Name      : {mons_type}
ATK Power : {int(atk_power)}
DEF Power : {int(def_power)}
HP        : 0
Level     : {level}""")
    print()
    print(
        f"Penjelasan : ATT: {tempAtk} ({percentage}%), Reduced by: {defcalc} ({def_power}%), ATT Results: {int(damagecalc)}")
    print()
    if hp <= 0:
        lose = True
    else:
        lose = False
    return lose, hp, damage_received

def ARENA (mons, mInv, rngEnemy, currentUser) :
    total_reward = 0
    damage_received = 0
    damage_given = 0
    print ("Selamat datang di Arena!!")
    print("============ MONSTER LIST ============")
    tempMons = []
    userMons = []
    stage = 1
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
    strengthBool = False
    resilienceBool = False
    healingBool = False
    rngEnemy = rngEnemy(LCG, mons)
    chosen = mons[rngEnemy]

    enemy_type = chosen[1]
    enemy_atk_power = (int(chosen[2]))
    enemy_def_power = (int(chosen[3]))
    enemy_hp = (int(chosen[4]))
    enemy_level = int(stage)
    enemy_atk_power, enemy_def_power, enemy_hp = monster(
        enemy_atk_power, enemy_def_power, enemy_hp, enemy_level)
    enemy = [enemy_type, enemy_atk_power,
            enemy_def_power, enemy_hp, enemy_level]
    
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

    while stage <= 5 :
        print(f"============ STAGE {stage} ============")
  
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
        turnCnt = 1
        win = False
        lose = False
        currentPot = userPot (iInv)
        while (not win) and (not lose):
            atk_power, def_power, hp, enemy_hp, win, currentPot, strengthBool, resilienceBool, healingBool, cancelPot, flee, damage_given = yourTurnArena(
                mons_type, atk_power, def_power, hp, strengthBool, resilienceBool, healingBool, turnCnt, currentPot, enemy_type, enemy_atk_power, enemy_def_power, enemy_hp, enemy_level, dmgCalc, damage_given)

            if not flee:
                if not cancelPot:
                    if not win:
                        lose, hp, damage_received = enemyTurnArena(mons_type, atk_power, def_power, hp, level, enemy_type,
                                            enemy_atk_power, enemy_def_power, enemy_hp, enemy_level, turnCnt, dmgCalc, damage_received)
                        turnCnt += 1
                    else:
                        break
                else:
                    pass
            else:
                stage = 8
                break

        if win:
            currentUser[4] += reward[stage-1][1]
            total_reward += reward[stage-1][1]
            print(f"Selamat, Anda berhasil mengalahkan monster {enemy_type} !!!")
            print(f"STAGE CLEARED! Anda akan mendapatkan {reward[stage-1][1]} OC pada sesi ini! ")
            print ("Memulai stage berikutnya...")
            print()
            stage+=1
            rngEnemy = rngEnemy(LCG, mons)
            chosen = mons[rngEnemy]
            enemy_type = chosen[1]
            enemy_atk_power = (int(chosen[2]))
            enemy_def_power = (int(chosen[3]))
            enemy_hp = (int(chosen[4]))
            enemy_level = int(stage)
            enemy_atk_power, enemy_def_power, enemy_hp = monster(
                enemy_atk_power, enemy_def_power, enemy_hp, enemy_level)
            enemy = [enemy_type, enemy_atk_power,
                    enemy_def_power, enemy_hp, enemy_level]
        
        if lose:
            print(
                f"Yahhh, Anda dikalahkan monster {enemy_type}. Jangan menyerah, coba lagi !!!")
            print (f"GAME OVER! Sesi latihan berakhir pada stage {stage}!")
            stage_akhir = stage
            stage = 7

    if stage == 6 :
        print ("Selamat, Anda berhasil menyelesaikan seluruh stage Arena !!!")
        print ("============== STATS ==============")
        print(f"""
    Total Hadiah     : {total_reward}
    Jumlah Stage     : 5
    Damage diberikan : {damage_given}
    Damae diterima   : {damage_received}""")
    elif stage == 7 :
        print ("============== STATS ==============")
        print(f"""
    Total Hadiah     : {total_reward}
    Jumlah Stage     : {stage_akhir}
    Damage diberikan : {damage_given}
    Damage diterima   : {damage_received}""")
    elif flee == True and stage == 1:
        print ("============== STATS ==============")
        print(f"""
    Total Hadiah     : 0
    Jumlah Stage     : 0
    Damage diberikan : 0
    Damage diterima   : 0""")
    elif flee == True:
        print ("============== STATS ==============")
        print(f"""
    Total Hadiah     : {total_reward}
    Jumlah Stage     : {stage_akhir}
    Damage diberikan : {damage_given}
    Damage diterima   : {damage_received}""")