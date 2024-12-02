# Many objects in Python are "iterable". meaning we can iterate over every element in every  object.
# Such as every element in  a list or every character in a string
# We can use for loops to execute a block of code for every iteration

# Iterate means you can "iterate" over the object - read or through the objects - preform an action for every thing in an object
# Example - you can iterate over every character in a string, iterate over every item in a list, intereate over every key in a dict

# Syntax for loops

my_iterable = [1, 2, 3]

for item_name in my_iterable:
    print(item_name)



my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in my_list:
    print(num)

string = "JaSamJovan"

for char in string:
    print(char)

# print only even numbers

for even_num in my_list:
    if even_num % 2 == 0:
        print(even_num)

# my solution

for even_num in my_list[1::2]:
    print(even_num)


# Multiple for loops

list_sum = 0

for num in my_list:
    list_sum = list_sum + num
    print(list_sum)

print(list_sum)


tup = (1, 2, 3)

for item in tup:
    print(item)

# Tuple unpacking - special quality with tuples


mylist = [(1,2),(3,4),(5,6),(7,8),(9,0)]


for pairs in mylist:
    print(pairs)

# this is where you unpack them
for (a,b) in mylist: # can do it with out () ----> for a,b in mylist:
    print(a)
    print(b)



my_lists = [(1,3,5,7,9),(2,4,6,8,10),(12,14,16,18,110)]

for (a,b,c,d,f) in my_lists:
    print(a)
    print(b)
    print(c)
    print(d)
    print(f)



# Dictonaries

d = {"k1":1, "k2": 2, "k3": 3}


# taking adventage of tuple unpacking for dict

for key,value in d.items():
    print(items)








