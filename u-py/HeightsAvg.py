student_height = input("Enter the heights of the students").split()

for s in range(0,len(student_height)):
# for s in range(-1,0):
    student_height[s]=int(student_height[s])
print(student_height)

theight=0
count=0
for i in student_height:
    theight += i
    count +=1
print(round(theight/count))
