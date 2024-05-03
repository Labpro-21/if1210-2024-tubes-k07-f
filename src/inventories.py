import os

def read_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        row = []
        field = ""
        in_quotes = False

        for char in file.read():
            if char == ';' and not in_quotes:
                row.append(field)
                field = ""
            elif char == '"' and not in_quotes:
                in_quotes = True
            elif char == '"' and in_quotes:
                in_quotes = False
            elif char == '\n' and not in_quotes:
                row.append(field)
                data.append(row)
                row = []
                field = ""
            else:
                field += char

        if field:
            row.append(field)
            data.append(row)

    return data


def get_current_directory():
    return os.path.dirname(os.path.abspath(__file__))

tempFilepath = get_current_directory()
charFilepath = [char for char in tempFilepath]
newcharFilepath = []
tempFilepath = get_current_directory()
charFilepath = [char for char in tempFilepath]
newcharFilepath = []

if charFilepath[-1] == "c" and charFilepath[-2] == "r" and charFilepath[-3] == "s" and charFilepath[-4] == "\\":
    for i in range(len(charFilepath)-4):
        if ord(charFilepath[i]) != 92:
            newcharFilepath.append(charFilepath[i])
        else:
            newcharFilepath.append("/")
else:
    for i in (charFilepath):
        if ord(i) != 92:
            newcharFilepath.append(i)
        else:
            newcharFilepath.append("/")

filepath = ("".join(map(str, newcharFilepath)))
mInv_path = filepath+"/data/monster_inventory.csv"
iInv_path = filepath+"/data/item_inventory.csv"
mons_path = filepath+"/data/monster.csv"

mInv = read_csv(mInv_path)
iInv = read_csv(iInv_path)
mons = read_csv(mons_path)

currentUser = [3, 'Agen_P', 'platypus123', 'agent', 0] # cuma sampel, nanti diambil dari fungsi login

def Inventory(currentUser, mInv, iInv, mons):
  print(f"============ INVENTORY LIST (User ID: {currentUser[0]}) ============")
  print(f"Jumlah O.W.C.A. Coin-mu sekarang {currentUser[4]}")
  invCount = 0
  mTemp = []
  iTemp = []


  for i in range(len(mInv)):
      if mInv[i][0] == str(currentUser[0]):
          print(
              f"{invCount+1}. Monster       (Name: {mons[i][1]}, Lvl: {mInv[i][2]}, HP: {mons[i][4]})")
          invCount += 1
          stats = [invCount, mons[i][1], mons[i][2],
                  mons[i][3], mons[i][4], mInv[i][2]]
          mTemp.append(stats)

  for i in range(len(iInv)):
      if iInv[i][0] == str(currentUser[0]):
          print(
              f"{invCount+1}. Potion        (Type: {iInv[i][1]}, Qty: {iInv[i][2]})")
          invCount += 1
          potInfo = [invCount, iInv[i][1], iInv[i][2]]
          iTemp.append(potInfo)

  print()
  while True:
      pilihanInv = input(">>> ")
      if pilihanInv.upper() != "KELUAR":
          if int(pilihanInv) <= int(len(mTemp)):
              for i in range(len(mTemp)):
                  if int(pilihanInv) == mTemp[i][0]:
                      print("Monster")
                      print(f"Name      : {mTemp[i][1]}")
                      print(f"ATK Power : {mTemp[i][2]}")
                      print(f"Def Power : {mTemp[i][3]}")
                      print(f"HP        : {mTemp[i][4]}")
                      print(f"Level     : {mTemp[i][5]}")
                      break
          elif int(pilihanInv) > int(len(mTemp)):
              for i in range(len(iTemp)):
                  if int(pilihanInv) == iTemp[i][0]:
                      print("Potion")
                      print(f"Type      : {iTemp[i][1]}")
                      print(f"Quantity  : {iTemp[i][2]}")
                      break
      elif pilihanInv.upper() == "KELUAR":
          break

Inventory(currentUser, mInv, iInv, mons)