import random

version = 0.1

def d4():
    d4 = random.choice([1, 2, 3, 4])
    return d4

BOY = d4() - d4()
DEX = d4() - d4()
SVY = d4() - d4()
TEC = d4() - d4()

print("DEAD IN SPACE Game Assistant")
print("v" + str(version))
print("Ability Values")
print("BODY: " + str(BOY))
print("DEXTERITY: " + str(DEX))
print("SAVVY: " + str(SVY))
print("TECH: " + str(TEC))