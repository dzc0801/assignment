import turtle
import time

screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple", "white"]

t.penup()
t.goto(-250, 150)
t.pendown()
t.pencolor("red")
t.pensize(3)

for _ in range(4):
    t.forward(80)
    t.right(90)

t.penup()
t.goto(-120, 150)
t.pendown()
t.pencolor("yellow")

for _ in range(3):
    t.forward(80)
    t.left(120)

t.penup()
t.goto(10, 150)
t.pendown()
t.pencolor("cyan")

for _ in range(5):
    t.forward(80)
    t.right(144)

t.penup()
t.goto(0, -50)
t.pendown()
t.pensize(2)

for i in range(360):
    t.pencolor(colors[i % len(colors)])
    length = i / 10 + 2
    t.forward(length)
    t.right(59)

turtle.done()