import turtle as t
import random
angle=[90,180,270,0]
tim = t.Turtle()
t.colormode(255)
def rancolor():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r,g,b)
    return random_color
tim.pensize(7)
tim.speed("fastest")
for i in range (200):
    tim.color(rancolor())
    tim.forward(30)
    # random.choice(turn)(random.choice(angle))
    tim.setheading(random.choice(angle))
    



