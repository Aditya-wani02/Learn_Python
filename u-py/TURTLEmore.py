from turtle import Turtle,Screen

tim= Turtle()
screen = Screen()
def move_forword():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def turn_right():
    tim.right(5)
def turn_left():
    tim.left(5)
def reset():
    tim.reset()
screen.listen()
screen.onkey(key="w",fun=move_forword)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="d",fun=turn_right)
screen.onkey(key="a",fun=turn_left)
screen.onkey(key="c",fun=reset)
screen.exitonclick()
