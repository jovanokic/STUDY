# key words dont work in other categories
from typing import List

# range function

my_list = [1,2,3]

for num in range(3,10,2): # range(start,stop,step)
    print(num)

# range is a generator you need to cast it to list

y: list[int] = list(range(0,11,2))
print(y)

index_count = 0

for letter in "abcde":
    index_count += 1
    print(f"At index {index_count}, the letter is {letter}")


index_count = 0
word = "abcde"
for letter in word:

    print(word[index_count])
    index_count += 1

# This is how we use enumerate function

index_count = 0
word = "abcde"
for letter in enumerate(word):

    print(letter)
    index_count += 1

# Now we got a tuple lets use tuple unpacking function


index_count = 0
word = "abcde"
for number,letter in enumerate(word):
    print(f"{number}{letter}\n")

# Zip functions zips lists together

list1 = [1,2,3]
list2 = ["a","b","c"]

y = zip(list1,list2)

print(list(y))

for item in y:
    print(item)


if "a" in ["a", "b", "c"]:

    print("true")

d = {"mykey": 365}

if "mykey" in d:
    print("true")

# random library


# shuffling randomly a list

from random import shuffle

mylist = [1,2,3,4,5,6,7,8,9,10]

shuffle(mylist)

print(mylist)


# function for grabbing random int

from random import randint


print(randint(0,100)) #a down and b upper range

# user input


a = int(input("enter number here: "))

print(type(a))

