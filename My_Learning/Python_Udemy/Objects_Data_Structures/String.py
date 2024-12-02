# Strings are character sequences under single or double quotes!!!

string = "A B C D E F G H"

# Strings are ordered squences that means we can use indexing and slicing to grab subsections of the string!

print(string[0::2]) # [start:stop:step]

# \n - new line

#lenght of string

print(len(string))

# Indexing

print(string[4])

# Can do reverse indexing also

print(string[4])

# Slicing

print(string[2:]) # from

print(string[:8:2]) # up to not including last

print(string[2:8:2]) # [start:stop:step]

# Strings are immutable

# String objects do not support item assignment and cannot reassign just a part of it


# But there are ways around it

# Slice

name = "Pam"

name = name[1:]

name += "P"

print(name)


# Object types

x = "string"

x.lower()
x.upper()
print(x.index("r")) # Gives an index location
print(x.upper())
print(x.lower())
