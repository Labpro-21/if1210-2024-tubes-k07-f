import time
from csv import *

def next_seed():
    return int(time.time())


def LCG(min_val, max_val, seed, a, c, m):
    seed = (a * seed + c) % m
    return min_val + (seed % (max_val - min_val + 1))


def rngLevel(LCG):
    m = 2**32
    a = 82
    c = 100
    min_val = 1
    max_val = 5

    seed = next_seed()
    random_integer = LCG(min_val, max_val, seed, a, c, m)
    rng = random_integer
    return rng


def rngEnemy(LCG, mons):
    m = 2**32
    a = 51
    c = 100
    min_val = 1
    max_val = len(mons)-1

    seed = next_seed()
    random_integer = LCG(min_val, max_val, seed, a, c, m)
    rng = random_integer
    return rng


def rngOC(LCG):
    m = 2**32
    a = 82
    c = 100
    min_val = 5
    max_val = 30

    seed = next_seed()
    random_integer = LCG(min_val, max_val, seed, a, c, m)
    rng = random_integer
    return rng


def rngCapture(LCG, enemy_level):
    if enemy_level == 1:
        limit = 75
    elif enemy_level == 2:
        limit = 50
    elif enemy_level == 3:
        limit = 25
    elif enemy_level == 4:
        limit = 10
    elif enemy_level == 5:
        limit = 5

    m = 2**32
    a = 82
    c = 100
    min_val = 1
    max_val = 100

    seed = next_seed()
    random_integer = LCG(min_val, max_val, seed, a, c, m)
    rng = random_integer

    if rng <= limit:
        capture = True
    else:
        capture = False

    return capture



