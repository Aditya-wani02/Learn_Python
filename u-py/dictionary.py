dictionary={
    "Bugs":"An error in the program that prevents the program form running as expected",
    "Funtion":"A piece of code that you can easily call over and over again",
    # "Loop": "Doing the same thing again and again"
    }

# print(dictionary)
# print(dictionary["Bugs"])

# Adding a new entry
dictionary["Loop"]="Doing the same thing again and again"
# print(dictionary)

Empty_dictionary={}
# wipe an existing dictionary
# dictionary=Empty_dictionary

# print(dictionary)


# redefine
dictionary["Bugs"]="A moth in your computer "
# print(dictionary)

# accessing the dictionary
for key in dictionary:
    print(key)
    print(dictionary[key])