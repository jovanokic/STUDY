import random

rand_int = random.randint(0, 36)
print(rand_int)
if rand_int == 0:
    color = "Green"

#here is red if can be divided by 2 and if not then black
elif rand_int <= 10:
    if rand_int % 2 == 0:
        color = "Black"
    else:
        color = "Red"

elif rand_int <= 18:
    if rand_int % 2 == 0:
        color = "Black"
    else:
        color = "Red"
elif rand_int <= 28:
    if rand_int % 2 == 0:
        color = "Black"
    else:
        color = "Red"
else:
    if rand_int % 2 == 0:
        color = "Black"
    else:
        color = "Red"


print(f"the color of your pocket is {color}, glad to help")
