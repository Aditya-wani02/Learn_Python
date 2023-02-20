student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

students_grade={}

for key in student_scores:
    if student_scores[key] >= 91:
        students_grade[key] =  "Outstanding"
    elif student_scores[key] >= 81:
        students_grade[key] =  "Exceeds Exceptions"
    elif student_scores[key] >= 71:
        students_grade[key] =  "Acceptable"
    elif student_scores[key] <= 70:
        students_grade[key] =  "Fail"

print(students_grade)