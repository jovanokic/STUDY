# list comprehensions are a unique way of quickly creating a list with python

# If you find yourself using a for loop along with .append() to create a list, List Comprehensions are a good alternative


my_string = "hello"

mylist = []

for letter in my_string:
    mylist.append(letter)

print(mylist)


#

my_string = "hello"

mylist = [letter for letter in my_string]

print(mylist)

mylist = [num**2 for num in range(0,11)]

print(mylist)

dword = "honor"

honor_list = []

for letter in dword:
    print(letter)