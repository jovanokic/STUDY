number = input("enter your number: ")
number = int(number)
# 1, 5, 10, 25

sum = 0

monet25 = 25
monet10 = 10
monet5 = 5
monet1 = 1

while sum != number:
    if number > monet25:
        count = number // monet25
        sum = monet25 * count
    elif number > monet10:
        count = number // monet10
        sum = monet10 * count
    elif number > monet5:
        count = number // monet5
        sum = monet5 * count
    elif number > monet1:
        count = number // monet1
        sum = monet1 * count







print(sum)