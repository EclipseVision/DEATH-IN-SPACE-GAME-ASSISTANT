import random

version = 0.2


def d2():
    d2 = random.choice([1, 2])
    return d2


def d3():
    d3 = random.choice([1, 2, 3])
    return d3


def d4():
    d4 = random.choice([1, 2, 3, 4])
    return d4


def d6():
    d6 = random.choice([1, 2, 3, 4, 5, 6])
    return d6


def d20():
    d20 = random.choice(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    )
    return d20


def ability():
    abilities = {"BODY": d4() - d4()}
    abilities.update({"DEXTERITY": d4() - d4()})
    abilities.update({"SAVVY": d4() - d4()})
    abilities.update({"TECH": d4() - d4()})
    return abilities


def origin():
    origin = {
        1: "CARBON",
        2: "CHROME",
        3: "PUNK",
        4: "SOLPOD",
        5: "VELOCITY CURSED",
        6: "VOID",
    }
    print(origin[d6()])


if __name__ == "__main__":
    print("DEAD IN SPACE Game Assistant")
    print("v" + str(version))
    print("Ability Values")
