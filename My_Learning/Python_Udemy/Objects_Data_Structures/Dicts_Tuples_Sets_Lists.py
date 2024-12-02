# Dictionaries:
#
# __getitem__(self, key): Used to define behavior for getting an item using square brackets, e.g., my_dict[key].
#
# __setitem__(self, key, value): Used to define behavior for setting an item using square brackets, e.g., my_dict[key] = value.
#
# __delitem__(self, key): Used to define behavior for deleting an item using del, e.g., del my_dict[key].
#
# __iter__(self): Used to define behavior for iteration over dictionary keys, e.g., in a for loop.
#
# __len__(self): Used to define the behavior of the len() function when applied to the dictionary.
#
# __contains__(self, key): Used to define behavior for the in operator to check if a key is in the dictionary.
#
# Sets:
#
# __contains__(self, item): Used to define behavior for the in operator to check if an item is in the set.
#
# __iter__(self): Used to define behavior for iteration over the elements of the set, e.g., in a for loop.
#
# __len__(self): Used to define the behavior of the len() function when applied to the set.
#
# __eq__(self, other): Used to define behavior for equality comparison between sets (e.g., set1 == set2).
#
# Tuples:
#
# Tuples are immutable in Python, so they have fewer special methods compared to mutable data types like dictionaries, sets, and lists. Some common methods that apply to tuples include:
#
# __getitem__(self, index): Used to access elements in the tuple using indexing, e.g., my_tuple[2].
#
# __iter__(self): Used to define behavior for iteration over the elements of the tuple, e.g., in a for loop.
#
# __len__(self): Used to define the behavior of the len() function when applied to the tuple.
#
# __eq__(self, other): Used to define behavior for equality comparison between tuples (e.g., tuple1 == tuple2).
#
# Lists:
#
# Lists are mutable sequences in Python, and they have their own set of special methods. Some common methods that apply to lists include:
#
# __getitem__(self, index): Used to access elements in the list using indexing, e.g., my_list[2].
#
# __setitem__(self, index, value): Used to define behavior when attempting to modify an element in the list, e.g., my_list[2] = 'new_value'.
#
# __delitem__(self, index): Used to define behavior for deleting an element from the list, e.g., del my_list[2].
#
# __iter__(self): Used to define behavior for iteration over the elements of the list, e.g., in a for loop.
#
# __len__(self): Used to define the behavior of the len() function when applied to the list.
#
# __eq__(self, other): Used to define behavior for equality comparison between lists (e.g., list1 == list2).