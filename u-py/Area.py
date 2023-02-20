import math


def paint_cal(height,width,coverage):
    can = math.ceil(((height*width)/coverage))
    print(f"you'll need {can} cans of paint.")

test_h = int(input("Enter height"))
test_w = int(input("Enter Width"))
coverage=5

paint_cal(height=test_h,width=test_w,coverage=coverage)