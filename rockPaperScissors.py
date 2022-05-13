import random


def choose():
    print("rock, paper, or scissors?")
    choice = input()

    if choice == "r" or choice == "R" or choice == "rock" or choice == "Rock":
        print("you chose rock")
        return 1  # 1 = rock
    if choice == "p" or choice == "P" or choice == "paper" or choice == "Paper":
        print("you chose paper")
        return 2  # 2 = paper
    if choice == "s" or choice == "S" or choice == "scissors" or choice == "Scissors":
        print("you chose scissors")
        return 3  # 3 = scissors
    else:
        print("invalid choice")
        print()
        return choose()


def play_again():
    print()
    print("play again?")
    yn = input()

    if yn == "y" or yn == "Y" or yn == "yes" or yn == "Yes":
        print()
        rps()
    if yn == "n" or yn == "N" or yn == "no" or yn == "No":
        pass
    else:
        print("answer not recognized (assuming no).")


def rps():
    player = choose()
    computer = random.randint(1, 3)  # 1 = rock, 2 = paper, 3 = scissors

    if computer == 1:
        print("the computer chose rock")
    if computer == 2:
        print("the computer chose paper")
    if computer == 3:
        print("the computer chose scissors")

    if player == 1 and computer == 3 or player == 2 and computer == 1 or player == 3 and computer == 2:
        print("you win")
        play_again()
    if player == 1 and computer == 2 or player == 2 and computer == 3 or player == 3 and computer == 1:
        print("you lose")
        play_again()
    else:
        print("it's a tie")
        play_again()


rps()
