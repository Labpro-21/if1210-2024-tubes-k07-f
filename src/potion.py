def potion(type_potion,atk_power,def_power,hp):
    if type_potion == "strength":
        atk_power= 1.05 * atk_power
    elif type_potion=="resillence":
        def_power = 1.05 * def_power
        if def_power > 50:
            def_power = 50
    elif type_potion=='healing':
        base_hp = hp
        hp= 1.25* base_hp
        if hp > base_hp:
            hp = base_hp
    return atk_power,def_power,hp