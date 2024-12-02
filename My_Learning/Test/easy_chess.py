correct = True
while correct == True:
    input_x_1 = int(input("Your move: "))
    input_y_1 = int(input("Your move: "))

    if input_x_1 == 1 or input_x_1 == 2 or input_x_1 == 3  or input_x_1 == 4  or input_x_1 == 5  or input_x_1 == 6  or input_x_1 == 7  or input_x_1 == 8:
        input_x_2 = int(input("Next Move: "))
        input_y_2 = int(input("Next Move: "))

        if input_x_1 == input_x_2 + 2 or input_x_1 == input_x_2 - 2:

            if input_y_1 == input_y_2 + 1 or input_y_1 == input_y_2 - 1:
                print(f"great success you moved to {input_x_2}{input_y_2}")

            else:
                print(f"Cannot move to {input_x_2}{input_y_2}")

        elif input_x_1 == input_x_2 + 1 or input_x_1 == input_x_2 - 1:

            if input_y_1 == input_y_2 + 2 or input_y_1 == input_y_2 - 2:
                print(f"great success you moved to {input_x_2}{input_y_2}")

            else:
                print(f"Cannot move to {input_x_2}{input_y_2}")

        else:
            print(f"Cannot move to {input_x_2}{input_y_2}")


    else:
        print("not correct, play again!")


print(f"Good job your initial horse move was {input_x}{input_y}, and you moved to {input_x_2}.{input_y_2}")
