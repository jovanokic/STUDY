# Naci Koren

x = 100 ** 0.5


# Naci Kvadrat

y = 100 ** 2


# Naci kub

z = 100 ** 3

print(f"{x} {y} {z}")

# Build a list in two seprate ways:

x = [0] * 3
print(x)

x = [0]

x.append(0)
x.append(0)

print(x)


# Reassign "hello" in this nested list to say 'goodbye' instead

list = [1, 2, [3, 4, "hello"]]

list[2][2] = "goodbye"

print((list[2][2]))

# Sort the list below

list4 = [4, 3, 4, 6, 1]

list4.sort()

print(list4)

# Grab hello from dicts
# Dictonaries are double indexing pairs and not sequence

d = {"simple_key": "hello"}
print(d["simple_key"])

d = {"k1": {"k2": "hello"}}
print(d["k1"]["k2"])

d = {"k1":[{"k2":["deep_key", ["hello"]]}]}

print(d["k1"][0]["k2"][1][0])

d = {"k1": [1, 2, {"k2": ["trick",{"tough":[1, 2, ["hello"]]}]}]}

print(d["k1"][2]["k2"][1]["tough"][2][0])

# Tuples List main difference - tuples are immutable
# Tuple example t = (1, 2, 3)

# Unique thing about sets that they do not repeat them selfs - no duplicates

# Use a set to find a unqiue value on list below

list = [1, 2, 2, 3, 3, 4, 4, 11, 22, 3, 3, 2]

set = (list)

print(set)

# Booleans # True, False statnemts

