import turtle as t
import random
color =["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray"]
tim =t.Turtle()

tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for i in range (1,101):
    tim.dot(10,random.choice(color))
    tim.forward(50)

    if i %10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

tim.hideturtle()
screen=t.Screen()
screen.exitonclick()
