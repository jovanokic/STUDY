# A B C D E F G H

# 1 2 3 4 5 6 7 8
correct = 0

row = ["A", "B", "C", "D", "E", "F", "G", "H"]

column = ["1", "2", "3", "4", "5", "6", "7", "8"]

test = [row[1], column[1]]

x = input ("What is Your initial horse position, from A to H: ").upper()

y = input ("and now from 1 to 8: ")
y = int(y)

plus_y2 = y + 2
minus_y2 = y - 2

plus_y1 = y + 1
minus_y1 = y - 1

user_input = [x, y]

print(user_input)

if x == "A":

    while correct == 0:

        move_x = input("Now where to move, from A to H: ")
        move_y = input("and from 1 to 8: ")
        move_y = int(move_y)

        if move_x == "B":

            if move_y == plus_y2:
                print("great success")
                correct = 1
            elif move_y == minus_y2:
                print("great success")
                correct = 1
            else:
                print("try again boiii")

        elif move_x == "C":
            if move_y == plus_y1:
                print("great success")
                correct = 1

            elif move_y == minus_y1:
                print("great success")
                correct = 1

            else:
                print("go away boiii")

        else:
            print("Not really boiii, try again")



elif x == "B":
    while correct == 0:

        move_x = input("Now where to move, from A to H: ")
        move_y = input("and from 1 to 8: ")
        move_y = int(move_y)

        if move_x == "C":

            if move_y == plus_y2:
                print("great success")
                correct = 1
            elif move_y == minus_y2:
                print("great success")
                correct = 1
            else:
                print("try again boiii")

        elif move_x == "D":
            if move_y == plus_y1:
                print("great success")
                correct = 1

            elif move_y == minus_y1:
                print("great success")
                correct = 1

            else:
                print("go away boiii")

        else:
            print("Not really boiii, try again")

elif x == "C":
    while correct == 0:

        move_x = input("Now where to move, from A to H: ")
        move_y = input("and from 1 to 8: ")
        move_y = int(move_y)

        if move_x == "D":

            if move_y == plus_y2:
                print("great success")
                correct = 1
            elif move_y == minus_y2:
                print("great success")
                correct = 1
            else:
                print("try again boiii")

        elif move_x == "E":
            if move_y == plus_y1:
                print("great success")
                correct = 1

            elif move_y == minus_y1:
                print("great success")
                correct = 1

            else:
                print("go away boiii")

        else:
            print("Not really boiii, try again")

elif x == "D":
    while correct == 0:

        move_x = input("Now where to move, from A to H: ")
        move_y = input("and from 1 to 8: ")
        move_y = int(move_y)

        if move_x == "E":

            if move_y == plus_y2:
                print("great success")
                correct = 1
            elif move_y == minus_y2:
                print("great success")
                correct = 1
            else:
                print("try again boiii")

        elif move_x == "F":
            if move_y == plus_y1:
                print("great success")
                correct = 1

            elif move_y == minus_y1:
                print("great success")
                correct = 1

            else:
                print("go away boiii")

        else:
            print("Not really boiii, try again")
elif x == "E":
    while correct == 0:

        move_x = input("Now where to move, from A to H: ")
        move_y = input("and from 1 to 8: ")
        move_y = int(move_y)

        if move_x == "F":

            if move_y == plus_y2:
                print("great success")
                correct = 1
            elif move_y == minus_y2:
                print("great success")
                correct = 1
            else:
                print("try again boiii")

        elif move_x == "G":
            if move_y == plus_y1:
                print("great success")
                correct = 1

            elif move_y == minus_y1:
                print("great success")
                correct = 1

            else:
                print("go away boiii")

        else:
            print("Not really boiii, try again")
elif x == "F":
    while correct == 0:

        move_x = input("Now where to move, from A to H: ")
        move_y = input("and from 1 to 8: ")
        move_y = int(move_y)

        if move_x == "G":

            if move_y == plus_y2:
                print("great success")
                correct = 1
            elif move_y == minus_y2:
                print("great success")
                correct = 1
            else:
                print("try again boiii")

        elif move_x == "H":
            if move_y == plus_y1:
                print("great success")
                correct = 1

            elif move_y == minus_y1:
                print("great success")
                correct = 1

            else:
                print("go away boiii")

        else:
            print("Not really boiii, try again")
elif x == "G":
    while correct == 0:

        move_x = input("Now where to move, from A to H: ")
        move_y = input("and from 1 to 8: ")
        move_y = int(move_y)

        if move_x == "H":

            if move_y == plus_y2:
                print("great success")
                correct = 1
            elif move_y == minus_y2:
                print("great success")
                correct = 1
            else:
                print("try again boiii")

        elif move_x == "C":
            if move_y == plus_y1:
                print("great success")
                correct = 1

            elif move_y == minus_y1:
                print("great success")
                correct = 1

            else:
                print("go away boiii")

        else:
            print("Not really boiii, try again")
elif x == "H":

    while correct == 0:

        move_x = input("Now where to move, from A to H: ")
        move_y = input("and from 1 to 8: ")
        move_y = int(move_y)

        if move_x == "G":

            if move_y == plus_y2:
                print("great success")
                correct = 1
            elif move_y == minus_y2:
                print("great success")
                correct = 1
            else:
                print("try again boiii")

        elif move_x == "F":
            if move_y == plus_y1:
                print("great success")
                correct = 1

            elif move_y == minus_y1:
                print("great success")
                correct = 1

            else:
                print("go away boiii")

        else:
            print("Not really boiii, try again")

else:
    print("try again boyo")


horse_move = [move_x, move_y]

print(f"Yes your horse moved to {horse_move}")