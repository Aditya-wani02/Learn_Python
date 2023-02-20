height = float(input("enter height in meters"))
weight = float(input("Enter the weight in kg"))
bmi= round(weight/(height ** 2))

# print(int(bmi))
if bmi < 18.5:
    print(f"Your bmi is {bmi} so you are underweight")
elif bmi <25:
     print(f"Your bmi is {bmi} so you are Normal Weight")
elif bmi < 30:
     print(f"Your bmi is {bmi} so you are Overweight")
elif bmi < 35:
     print(f"Your bmi is {bmi} so you are Obese")
else:
     print(f"Your bmi is {bmi} so you are Clinically Obese")