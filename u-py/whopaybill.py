import random
name_string=input("Enter the name of everyone ,seperated by comman")
names=name_string.split(",")
# n=names.__len__() - 1
n=len(names) - 1
print(n)
person=random.randint(0,n)
print(f"{names[person]} is Going to pay the bill")