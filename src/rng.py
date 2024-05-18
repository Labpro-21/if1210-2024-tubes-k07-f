import time
from src.csv import *

class LCG:
    def __init__(self, min_val, max_val):
        self.m = 2**32
        self.a = 1664525
        self.c = 1013904223
        self.seed = int(time.time())  # Initialize seed with current time
        self.min_val = min_val
        self.max_val = max_val

    def set_seed(self, seed):
        self.seed = seed

    def generate(self):
        self.seed = (self.a * self.seed + self.c) % self.m
        scaled_number = self.min_val + \
            (self.seed / self.m) * (self.max_val - self.min_val)
        return int(scaled_number)  # Convert the scaled number to an integer


# Example usage
def rngLevel(LCG):
    lcgList = []
    lcg = LCG(1, 6)  # Generate integers between 0 and 100
    for _ in range(11):
        lcgList.append(lcg.generate())

    rng = (lcgList[5])
    return rng

def rngEnemy(LCG, mons):
    lcgList = []
    lcg = LCG(1, len(mons))
    for _ in range(11):
        lcgList.append(lcg.generate())

    rng = (lcgList[5])
    return rng
    
def rngOC(LCG):
    lcgList = []
    lcg = LCG(5, 31)
    for _ in range(11):
        lcgList.append(lcg.generate())

    rng = (lcgList[5])
    return rng

# rng = (rng(LCG))
