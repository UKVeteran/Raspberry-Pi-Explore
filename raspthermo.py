from turtle import Turtle,Screen, mainloop
import random, time

# Update the temperature bar height and value
def drawbar(temp):
       top = (-50 + 260 * temp/40)
       boutline = ((0,-50),(20,-50),(20,top),(-20,top),(-20,-50),(0,-50))
       bar.penup()
       bar.clear()  # clear the old bar and text
       bar.begin_fill()
       for pos in boutline:
              bar.goto(pos)
       bar.end_fill()
       bar.goto(30,top)
       bar.write(str(temp) + " C",font=("Arial",24, "bold"))
 
# Setup a default screen size and Title
wn = Screen()
wn.setup(width = 500, height = 500)
wn.title("RaspPi Temperature Sensor")
 
# define a static thermo backgroup object and a dynamic bar object
thermo = Turtle()
thermo.penup()
bar = Turtle()
bar.color("red")
bar.hideturtle()
 
# define an array for the top tube
outline = ((0,-50),(25,-50),(25,210),(-25,210),(-25,-50),(0,-50))
thermo.hideturtle()
thermo.pensize(5)
for pos in outline:
       thermo.goto(pos)
       thermo.pendown()
 
# add some temperature labels
thermo.penup()
thermo.goto(50,-50)
thermo.write("0 C")
thermo.goto(50,210)
thermo.write("40 C")
 
# draw the filled bulb at the bottom
thermo.goto(0,-137)
thermo.pendown()
thermo.pensize(5)
thermo.color("black","red")
thermo.begin_fill()
thermo.circle(50)
thermo.end_fill()
