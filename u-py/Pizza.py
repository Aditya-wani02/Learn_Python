print("Welcome to python pizzas....!!")
size=input("Enter the size of pizza - S, M ,L")
add_pepperoni=input("Do you want to add pepperoni ?  Y or N")
extra_cheeze= input("Do you want Extra cheeze ? Y or N")
bill=0

if size == "S":
    bill=15
    if add_pepperoni == "Y":
        bill += 2
    if extra_cheeze =="Y":
        bill += 1

      
if size == "M":
    bill=20
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheeze =="Y":
        bill += 1


if size == "L":
    bill=25
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheeze =="Y":
        bill += 1


print(f"Your bill is ${bill}")