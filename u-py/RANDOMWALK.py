import turtle as t
import random
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
angle=[90,180,270,0]
tim = t.Turtle()
turn =[tim.right,tim.left,tim.right,tim.left]
tim.pensize(3)
tim.speed(10)
for i in range (200):
    tim.color(random.choice(colours))
    tim.forward(30)
    # random.choice(turn)(random.choice(angle))
    tim.setheading(random.choice(angle))
    

screen = t.Screen()
screen.exitonclick()


