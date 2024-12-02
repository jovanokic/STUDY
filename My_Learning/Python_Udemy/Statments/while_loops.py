# While loops will contiue to execute a block of code while some conditions remain True

x = 0

while x <= 5:
    print(f"current value is {x}")
    x += 1
else:
    print(f"value is not equal or less then {x}")


# Break, Continue, Pass

# We can use break contiue and pass statments in our loops to add additinal functionality for various cases. The three statments are defined by:
# Break: Breaks out of the current closest enclosing loop.
# Continue: Goes to the top of the closest enclosing loop.
# Pass: Does nothing at all.

y = [4,2,3]

for item_y in y:
    pass # They keep it as a syntax holder
    print(item_y)

mystring = "Sammy"

for letter in mystring:
    if letter == "a":
        continue # it will skip this part of the loop - like skip-step and just
    print(letter)


for letter in mystring:
    if letter == "a":
        break
    print(letter)