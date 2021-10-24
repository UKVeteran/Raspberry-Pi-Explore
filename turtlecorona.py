import turtle
jj = turtle.Turtle()
s=turtle.Screen()
turtle.screensize(1000,1000)
jj.pencolor("red")
s.bgcolor("black")
jj.pencolor("dark cyan")
jj.pensize(2)
Python=0
CplusPlus=0
jj.speed(0)
jj.penup()
jj.goto(0,280)
jj.pendown()
while True:
    jj.forward(Python)
    jj.right(CplusPlus)
    Python+=3
    CplusPlus+=1
    if CplusPlus==210:
        break
    jj.hideturtle()
turtle.done()