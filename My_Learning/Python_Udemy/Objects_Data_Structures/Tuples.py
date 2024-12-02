# Tuples are immutable

set = {1, 2, 3, 4, 5, 6, 7, 8}
list = [1, 2, 3, 4, 5, 6, 7, 8]
tuple = (1, 2, 3, 4, 5, 6, 7, 8)

print(len(tuple))

# Tuples have built in methods for tuples and that's index and count method

# Count and Index - Only for index

t = ("a", "a", "b", "a", "t")

print(t.count("a")) # How many times "a" appears in tuple

print(t.index("b")) # Location of "b"

# Checking type

print(type(tuple))

print(type(list))

print(type(set))

# Tuples can also have slicing and indexing

print(t[2:9:2])

# Main difference between list and a tuple is that tuples are immutable
# Tuples cannot be modified, why used? Passing around objects that should NOT be changed