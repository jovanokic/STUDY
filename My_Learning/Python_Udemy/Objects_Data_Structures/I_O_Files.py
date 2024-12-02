
# f = open(path_to_file, mode)
# In this syntax, the path_to_file parameter specifies the path to the text file that you want to create.

# 'w' – open a file for writing. If the file doesn’t exist, the open() function creates a new file. Otherwise, it’ll overwrite the contents of the existing file.
# 'x' – open a file for exclusive creation. If the file exists, the open() function raises an error (FileExistsError). Otherwise, it’ll create the text file.




with open('C:\\Users\\j_anokic\\OneDrive\\Desktop\\Python\\My_Learning\\Python_Udemy\\Objects_Data_Structures myfile.txt', 'w') as f:
    f.write('Create a new text file! - line one\nThis is line two\nThis is line three')

myfile = open("myfile.txt")

myfile.seek(0)

print(myfile.read())

# If your file is open somewhere else on the computer and lets say you want to delete it you need to close it
# myfile.close() so better way to go about it is:

with open("myfile.txt") as my_new_file:
    contents = my_new_file.read()
print(contents)

# Reading and writing and overwriting to files

# mode "a" will append - add lines to the end of the text files
# "r" read only
# "w" write only
# "a" is append only
# "r+" reading and writing
# "w+" is writing and reading

with open("myfile.txt", mode="r") as myfile:
    contents = myfile.read()


with open("mynewfile.txt", mode="w") as mynewfile:
    mynewfile.write("Line 1\nLine 2\nLine 3")

with open("mynewfile.txt", mode="r") as mynewfile:
    print(mynewfile.read())


with open("mynewfile.txt", mode="w") as mynewfile: # Write mode will overwrite
    mynewfile.write("Linez 1\nLinez 2\nLinez 3")

with open("mynewfile.txt", mode="r") as mynewfile:
    print(mynewfile.read())

with open("mynewfile.txt", mode="a") as mynewfile: # Write mode will overwrite
    mynewfile.write("\nLinez 4")

with open("mynewfile.txt", mode="r") as mynewfile:
    print(mynewfile.read())

