import random

guess_the_number = None

player = "Yes"

while player != "No":

    rand_int = random.randint(1,100)

    while rand_int != guess_the_number:

        guess_the_number = int(input("Choose a number from 1 to 100: "))

        if guess_the_number > rand_int:
            print("Your number is lower, enter new number: ")

        elif guess_the_number < rand_int:
            print("Your number is higher, enter new number: ")

        else:
            print("good job at guessing")
            break

    player = input("Would you like to play more, Yes or No: ")


print("game over!")