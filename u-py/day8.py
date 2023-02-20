# for one parameter

# def greet(som):
#     print(f"Hello {som} ")
#     print(f"Good Morning {som} ")
#     print(f"How are You {som} ?")

# greet("aditya")



def greet_with(name,location):
    print(f"Hello {name} ")
    print(f"Good Morning {name} ")
    print(f"What is it like in {location} ")
#                   positional arguments
# greet_with("aditya","Jabalpur")
# greet_with("Jabalpur","aditya")


def one(a,b,c):
    print(f" {a} {b} {c}   ")

    #  1,2,3
one(c=3,a=1,b=2)
#      keyword agruments


def greetkey(name,location):
    print(f"Hello {name} ")
    print(f"Good Morning {name} ")
    print(f"What is it like in {location} ")


greetkey(location="london",name="chintu")
