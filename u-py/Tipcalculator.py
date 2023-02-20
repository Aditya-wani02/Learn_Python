print("Welcome to tip calculator")
total = float(input("What was the total bill ?\n"))
tip = int(input("What percentage of tip would you like to give? 10 ,12 or 15 ?\n"))
people = int(input("How many people to split the bill ?"))
with_tip = total*(tip/100)
totalpay = total + with_tip
payable = totalpay/people
pay = round(payable,2)
h="{:.2f}".format(pay)
print(f"Each should pay : ${h}")
