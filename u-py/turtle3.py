from turtle import Screen, Turtle

tim=Turtle()
# tim.pensize(70)
tim.color("red")
for i in range(0,3):
    tim.forward(100)
    tim.right(120)
tim.color("blue")
for i in range(0,4):
    tim.forward(100)
    tim.right(90)

tim.color("green")
for i in range(0,5):
    tim.forward(100)
    tim.right(72)


tim.color("aqua")
for i in range(0,6):
    tim.forward(100)
    tim.right(60)

tim.color("brown")
for i in range(0,7):
    tim.forward(100)
    tim.right(51.42857142857143)
tim.color("orange")
for i in range(0,8):
    tim.forward(100)
    tim.right(45)

screen=Screen()
screen.exitonclick()