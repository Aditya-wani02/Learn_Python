# multiple condition
# nested if else statement

# if condition:
#     if condition :
#       do this
#     else:
#       do this
# else:
#     do this

print("Welcome")
height=int(input("Enter your height"))
if height >= 120:
    print("You can ride the rollercoster!!")
    age=int(input("Enter your age"))
    if age < 12:
        print("Pay $5")
    elif age <= 18:
        print("Pay $7")
    else:
        print("Pay $12")
else:
    print("sorry you cant ride the rollercoster")