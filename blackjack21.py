import random

# ace() no longer works (at least when deck is full, probably for more scenarios)
# make it so that as soon as you go over 21, you lose (idk what to do about aces though)
# some tens are counted twice idk why
# CAN'T DO MATH IDK WHY WTF
# it thinks that [ace of hearts, 2 of diamonds, 8 of spades] is 23 when ace is 11

values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king", "ace"]
suits = ["spades", "clubs", "diamonds", "hearts"]
score = []  # integer values of all of the cards, aces are labeled "a", can iterate through list, overwrite this later


def random_card():
    card_value = values[random.randint(0, (len(values) - 1))]
    card_suit = suits[random.randint(0, (len(suits) - 1))]

    try:
        score.append(int(card_value))
    except ValueError:
        if card_value.__eq__("jack") or card_value.__eq__("queen") or card_value.__eq__("king"):
            score.append(10)  # this is going off for every random card generated, even for duplicates
        elif card_value.__eq__("ace"):
            score.append("a")

    return f"{card_value} of {card_suit}"


def duplicate_card(hand: list):
    new_card = random_card()

    try:
        if hand.__contains__(new_card):
            return duplicate_card(hand)
        else:
            hand.append(new_card)
            return hand
    except RecursionError:
        raise RecursionError


def hit(hand: list):
    try:
        print(f"hand: {hand}")
        print()
        print("hit? (y/n)")
        yn = input()

        if yn.__eq__("y"):
            new_hand = duplicate_card(hand)
            print()
            return hit(new_hand)
        if yn.__eq__("n"):
            return hand
        else:
            print("please enter either ''y'' or ''n''")
            print()
            return hit(hand)
    except RecursionError:
        print()
        print("you already have the whole deck!")
        print(f"hand size: {len(hand)}, score size: {len(score)}")
        return hand


def ace(ind: int, hand: list):
    print()
    if score[ind].__eq__("a"):
        print(f"would you like the {hand[ind]} to be a 1 or an 11? (1/11)")
        inp = input()
        if inp == "1":
            return 1
        if inp == "11":
            return 11
        else:
            print()
            print("please enter either 1 or 11")
            return ace(ind, hand)


def calculate_score(score_list: list, hand: list):
    final_score = 0

    for n in range(0, (len(score_list))):
        try:
            final_score += int(score_list[n])
        except ValueError:
            final_score += int(ace(n, hand))  # need a way to get index of aces past the first one. THIS STILL BREAKS
    print()
    return final_score


def play():
    card1 = random_card()
    hand = duplicate_card([card1])  # starting hand (two cards)

    print()
    final_hand = hit(hand)

    final_score = calculate_score(score, final_hand)

    if final_score < 17:
        print(f"yikes... you got {final_score} points.")
    if 17 <= final_score <= 20:
        print(f"good job! you got {final_score} points.")
    if final_score == 21:
        print(f"wow! you got {final_score} points!")
    if final_score > 21:
        print(f"you busted! you got {final_score} points.")


play()
