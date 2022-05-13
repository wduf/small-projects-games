import random


# returns score
def find_patterns(slots: list):
    score = 0

    # one point per line times the number
    # horizontals
    if slots[0] == slots[1] == slots[2]:
        score += (1 * slots[0])
        print("h1")
    if slots[3] == slots[4] == slots[5]:
        score += (1 * slots[2])
        print("h2")
    if slots[6] == slots[7] == slots[8]:
        score += (1 * slots[6])
        print("h3")

    # verticals
    if slots[0] == slots[3] == slots[6]:
        score += (1 * slots[0])
        print("v1")
    if slots[1] == slots[4] == slots[7]:
        score += (1 * slots[1])
        print("v2")
    if slots[2] == slots[5] == slots[8]:
        score += (1 * slots[0])
        print("v3")

    # diagonals
    if slots[0] == slots[4] == slots[8]:
        score += (1 * slots[0])
        print("d1")
    if slots[6] == slots[4] == slots[2]:
        score += (1 * slots[6])
        print("d2")

    # this will never happen
    if slots[0] == slots[1] == slots[2] == slots[3] == slots[4] == slots[5] == slots[6] == slots[7] == slots[8]:
        print("holy shit")

    return score


def play_slots():
    # 1 * 7, 2 * 6, 3 * 5, 4 * 4, 5 * 3, 6 * 2, 7 * 1
    numbers = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7]
    # 3 x 3, rows: a-c, columns: 1-3
    a1 = numbers[random.randint(0, (len(numbers) - 1))]
    a2 = numbers[random.randint(0, (len(numbers) - 1))]
    a3 = numbers[random.randint(0, (len(numbers) - 1))]
    b1 = numbers[random.randint(0, (len(numbers) - 1))]
    b2 = numbers[random.randint(0, (len(numbers) - 1))]
    b3 = numbers[random.randint(0, (len(numbers) - 1))]
    c1 = numbers[random.randint(0, (len(numbers) - 1))]
    c2 = numbers[random.randint(0, (len(numbers) - 1))]
    c3 = numbers[random.randint(0, (len(numbers) - 1))]

    # list of slot numbers
    slots = [a1, a2, a3, b1, b2, b3, c1, c2, c3]

    print()
    print("***************")
    print(f"|| {a1} | {a2} | {a3} ||")
    print(f"|| {b1} | {b2} | {b3} ||")
    print(f"|| {c1} | {c2} | {c3} ||")
    print("***************")
    print()

    print(f"score: {find_patterns(slots)}")


play_slots()
