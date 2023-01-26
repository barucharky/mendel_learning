#B"H

import random

winning_number = random.randint(1, 10)
i = 5

print("=====")

while i > 0:
    print("YOU HAVE " + str(i) + " GUESSES")

    guess = input("Guess a number!\n")

    if not guess.isnumeric():
        print("Not a number!")

    elif int(guess) < 1 or int(guess) > 10:
        print("not a VALID number")

    else:
        if int(guess) > winning_number:
            print("\nToo big!!!!")

        elif int(guess) < winning_number:
            print("\nToo smaaaaaaalllll!!!!")

        else:
            break

    i = i -1

if int(guess) != winning_number:
    print("Very, very bad.")

else:
    print("Very good!!!")