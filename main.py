import random


min = 1
max = 6

roll_again = "yes"

while roll_again == "yes":
    print("The dices rolled: ")
    die1 = random.randint(min, max)
    die2 = random.randint(min, max)
    print(die1, die2)
    print(die1 + die2)
    if (die1 + die2) == 7 or (die1 + die2) == 11:
        print("You win!")
    else:
        print("You lost!")

    roll_again = input("Roll the dices again? ")
