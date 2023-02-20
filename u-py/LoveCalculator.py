print(" \n\n")
print("Welcome To Love Calculator..!!!!!")
name1 = input("Enter Your Name \n")
name2 = input("Enter their Name \n")
names=name1 + name2
n1=names.lower()
a=n1.count("t")
b=n1.count("r")
c=n1.count("u")
d=n1.count("e")

a1=n1.count("l")
b1=n1.count("o")
c1=n1.count("v")
d1=n1.count("e")

print(f"T occur {a} times")
print(f"R occur {b} times")
print(f"U occur {c} times")
print(f"E occur {d} times")
t1=a+b+c+d
print("Total =" ,t1)
print(f"L occur {a1} times")
print(f"O occur {b1} times")
print(f"V occur {c1} times")
print(f"E occur {d1} times")
t2=a1+b1+c1+d1
print("Total =" ,t2)

total=t1*10 + t2  

if total <=10 or total >= 90:
    print(f"Your Score is {total}, You go together like coke and mentos  ")
if total >=40 and total <= 55:
     print(f"Your Score is {total}, You are great together!! <3 <3 ")
else:
     print(f"Your Score is {total}")