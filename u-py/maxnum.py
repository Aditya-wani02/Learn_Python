# student_marks=input("enter the marks").split()
# for s in range(0,len(student_marks)):
#     student_marks[s]=int(student_marks[s])
# print(student_marks)
student_marks=[54,65,76,23,88,65,78,98,32]
maxnum=0
for i in student_marks :
    if i > maxnum:
        maxnum = i
print(maxnum)
