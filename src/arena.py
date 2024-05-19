import os

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


def ARENA(mons, mInv, rngEnemy, currentUser, iInv):
    ballPresence = False
    total_reward = 0
    damage_received = 0
    damage_given = 0
    print("Selamat datang di Arena!!")
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
    hp_reset = hp
    level = currentMons[4]
    atk_power, def_power, hp = monster(atk_power, def_power, hp, level)
    strengthBool = False
    resilienceBool = False
    healingBool = False
    enemyrng = rngEnemy(LCG, mons)
    chosenEnemy = mons[enemyrng]

    enemy_type = chosenEnemy[1]
    enemy_atk_power = (int(chosenEnemy[2]))
    enemy_def_power = (int(chosenEnemy[3]))
    enemy_hp = (int(chosenEnemy[4]))
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

    while stage <= 5:
        stage_akhir = stage-1
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
        currentPot, strengthIndex, resilienceIndex, healingIndex = userPot(
            iInv, currentUser)
        while (not win) and (not lose):
            atk_power, def_power, hp, enemy_hp, win, currentPot, strengthBool, resilienceBool, healingBool, cancel, flee, end, iInv, damage_given = yourTurn(
                mons_type, atk_power, def_power, hp, strengthBool, resilienceBool, healingBool, turnCnt, currentPot, strengthIndex, resilienceIndex, healingIndex, enemy_type, enemy_atk_power, enemy_def_power, enemy_hp, enemy_level, dmgCalc, chosenEnemy, userBall, userMons, ballPresence, damage_given, iInv)

            if not flee:
                if not cancel:
                    if not win:
                        lose, hp, damage_received = enemyTurn(mons_type, atk_power, def_power, hp, level, enemy_type,
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
            print(
                f"Selamat, Anda berhasil mengalahkan monster {enemy_type} !!!")
            print(
                f"STAGE CLEARED! Anda akan mendapatkan {reward[stage-1][1]} OC pada sesi ini! ")
            print("Memulai stage berikutnya...")
            print()
            stage += 1
            hp = hp_reset
            enemyrng = rngEnemy(LCG, mons)
            chosenEnemy = mons[enemyrng]
            enemy_type = chosenEnemy[1]
            enemy_atk_power = (int(chosenEnemy[2]))
            enemy_def_power = (int(chosenEnemy[3]))
            enemy_hp = (int(chosenEnemy[4]))
            enemy_level = int(stage)
            enemy_atk_power, enemy_def_power, enemy_hp = monster(
                enemy_atk_power, enemy_def_power, enemy_hp, enemy_level)
            enemy = [enemy_type, enemy_atk_power,
                     enemy_def_power, enemy_hp, enemy_level]

        if lose:
            print(
                f"Yahhh, Anda dikalahkan monster {enemy_type}. Jangan menyerah, coba lagi !!!")
            print(f"GAME OVER! Sesi latihan berakhir pada stage {stage}!")
            stage_akhir = stage
            stage = 7

    if stage == 6:
        print("Selamat, Anda berhasil menyelesaikan seluruh stage Arena !!!")
        print("============== STATS ==============")
        print(f"""
    Total Hadiah     : {total_reward}
    Jumlah Stage     : 5
    Damage diberikan : {damage_given}
    Damae diterima   : {damage_received}""")
    elif stage == 7:
        print("============== STATS ==============")
        print(f"""
    Total Hadiah     : {total_reward}
    Jumlah Stage     : {stage_akhir}
    Damage diberikan : {damage_given}
    Damage diterima   : {damage_received}""")
    elif flee == True:
        print("============== STATS ==============")
        print(f"""
    Total Hadiah     : {total_reward}
    Jumlah Stage     : {stage_akhir}
    Damage diberikan : {damage_given}
    Damage diterima   : {damage_received}""")
