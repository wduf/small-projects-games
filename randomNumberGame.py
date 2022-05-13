import random


def guess():
    print()
    print("enter a number 1 - 100")
    g = input()

    try:
        if 1 <= int(g) <= 100:
            return int(g)
        else:
            print()
            print("please enter a number 1 - 100")
            return guess()
    except ValueError:
        print()
        print("that's not a number")
        print("please enter a number 1 - 100")
        return guess()


def winning_number(the_number: int):
    g = guess()

    if g > the_number:
        print("lower")
        winning_number(the_number)
    if g < the_number:
        print("higher")
        winning_number(the_number)
    if g == the_number:
        print("you win!")


def play():
    the_number = random.randint(1, 100)

    winning_number(the_number)


play()
