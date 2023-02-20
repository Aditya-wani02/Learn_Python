# score = 0
# height = 1.8 
# isw = True

# print(f"your score is {score}, your height is {height}, you are winning is {isw}")


# life in week
age = int(input("Enter your current age"))
tyear= 90
tmonth= 90 * 12
tweek = 90 * 52
tday= 90 * 365
ryears= tyear - age
rmonths = tmonth - (age*12)
rweek = tweek -(age *52)
rdays = tday - (age * 365)

print(f"You have {rdays} days , {rweek} weeks , {rmonths} months and {ryears} years left")