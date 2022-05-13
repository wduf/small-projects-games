import random

# 5x5 board, outer ring worth 1 point, inner ring worth 3 points
# number id system: top row = 1-5, second row = 6-10, ... bottom row = 20-25

# very basic ai, everything happens in the learn() method
# basically, lower probability if it is a choice that returns 1 or 2 points


def play(position: int):
    if 1 <= position <= 25:
        if position == 1 or position == 2 or position == 3 or position == 4 or position == 5 or \
                position == 6 or position == 10 or position == 11 or position == 15 or position == 16 or \
                position == 20 or position == 21 or position == 22 or position == 23 or position == 24 or \
                position == 25:
            # print("1 points")
            return 1
        if position == 7 or position == 8 or position == 9 or position == 12 or position == 14 or position == 17 \
                or position == 18 or position == 19:
            # print("2 points")
            return 2
        if position == 13:
            # print("3 points")
            return 3


def input_play():
    print()
    print("position? (1-25)")
    inp = input()

    try:
        if 1 <= int(inp) <= 25:
            if int(inp) == 1 or int(inp) == 2 or int(inp) == 3 or int(inp) == 4 or int(inp) == 5 or \
                    int(inp) == 6 or int(inp) == 10 or int(inp) == 11 or int(inp) == 15 or int(inp) == 16 or \
                    int(inp) == 20 or int(inp) == 21 or int(inp) == 22 or int(inp) == 23 or int(inp) == 24 or \
                    int(inp) == 25:
                print("1 points")
            if int(inp) == 7 or int(inp) == 8 or int(inp) == 9 or int(inp) == 12 or int(inp) == 14 or int(inp) == 17 \
                    or int(inp) == 18 or int(inp) == 19:
                print("2 points")
            if int(inp) == 13:
                print("3 points")
    except ValueError:
        print()
        print("please enter a number 1-25")


def roll(dict0: dict):
    r = random.randint(1, 25)
    n = random.randint(1, 100)
    if n <= dict0.get(r):
        return r
    else:
        return roll(dict0)


# adjusting numbers changes how fast the ai will learn
# can't use number less than 1 because randint() picks integer
def learn(dict0: dict, num: int, points: int):
    if points == 1:
        dict0[num] -= 2  # don't want this, decrease by a lot
    if points == 2:
        dict0[num] -= 1  # okay, but not ideal, decrease by a little bit
    if points == 3:
        dict0[num] += 2  # want this, increase by a lot
    return dict0


def darts_ai():
    pos_dict = {}
    n = 0

    for num in range(1, 26):  # why does this work? first is 1, second is 26, but it goes from 1 to 25?
        pos_dict[num] = 50

    while n < 1000:  # how many times the ai will play and "learn"
        smart_number = roll(pos_dict)
        smart_points = play(smart_number)  # learning happens here

        print(f"position: {smart_number}, points: {smart_points}")
        pos_dict = learn(pos_dict, smart_number, smart_points)
        n += 1

    # print(pos_dict)


darts_ai()
