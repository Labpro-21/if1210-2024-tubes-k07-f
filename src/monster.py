def monster(atk_power:int, def_power:int, hp:int, level:int):
    if 2 <= level <= 5 :
        add = 1 + ((level - 1) * 0.1)
        atk_power *= add
        def_power *= add
        hp *= add
    if def_power > 50:
        def_power = 50

    return int(atk_power), int(def_power), int(hp)

#print(monster)

def attack(x:int)
    atk_power = random_number ((0.7 * atk_power)),(1.3* atk_power)
return atk_power

#gayakin bener :")
