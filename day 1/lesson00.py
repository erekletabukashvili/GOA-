from turtle import *
speed(0)

#we want to paint a house
  
#step 1:  draw a square
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door 

forward(70)
color("yellow")
begin_fill()
left(90)
forward(100)      #height of the door
right(90)

forward(60)
right(90)
forward(100)
end_fill()

penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#panjrebis gaketeba 
color("black")
penup()
goto(150,150)
pendown()
left(30)
forward(30)
right(90)
forward(70)
right(90)
forward(45)
right(90)
forward(70)
right(90)
forward(40)
penup()
forward(5)
right(90)
forward(35)
right(90)