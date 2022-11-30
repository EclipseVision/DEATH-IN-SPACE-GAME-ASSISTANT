import random

version = 0.2

def d4():
    d4 = random.choice([1, 2, 3, 4])
    return d4
def d6():
    d6 = random.choice([1, 2, 3, 4, 5, 6])
    return d6

def ability():
    BOY = d4() - d4()
    DEX = d4() - d4()
    SVY = d4() - d4()
    TEC = d4() - d4()
    print("BODY: " + str(BOY))
    print("DEXTERITY: " + str(DEX))
    print("SAVVY: " + str(SVY))
    print("TECH: " + str(TEC))

def origin():
    origin = {
        1: "CARBON",
        2: "CHROME",
        3: "PUNK",
        4: "SOLPOD",
        5: "VELOCITY CURSED",
        6: "VOID"
    }
    print(origin[d6()])

if __name__ == "__main__":
    print("DEAD IN SPACE Game Assistant")
    print("v" + str(version))
    print("Ability Values")
    ability()
    print("Origin")
    origin()
