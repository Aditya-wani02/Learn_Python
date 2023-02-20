import turtle as t
import random
tim =t.Turtle()
tim.speed(0)
t.colormode(255)
def rancolor():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r,g,b)
    return random_color
for i in range(0,72):
    tim.color(rancolor())
    tim.circle(100)
    tim.left(5)

screen=t.Screen()
screen.exitonclick()