def potion(type_potion,atk_power,def_power,hp):
    if type_potion == "strength":
        atk_power= 1.05 * atk_power
    elif type_potion=="resillence":
        def_power= 1.05* def_power
    elif type_potion=='healing':
        hp= 1.25* hp
    return atk_power,def_power,hp
