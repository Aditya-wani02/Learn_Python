
print("Welcome")
height=int(input("Enter your height"))
bill = 0
if height >= 120:
    print("You can ride the rollercoster!!")
    age=int(input("Enter your age"))
    if age < 12:
        bill = 5
        print("Child ticket $5")
    elif age <= 18:
        bill=7
        print("Teen ticket $7")
    else:
        bill=12
        print("Adult ticket $12")
    wantpic=input("Do you want a Photograph ? Y or N")
    if wantpic == "Y":
        bill += 3
    print(f"Total bill will be ${bill}")
else:
    print("sorry you cant ride the rollercoster")