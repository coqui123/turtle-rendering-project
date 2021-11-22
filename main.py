######################################################
# Project: Project 1
# Student Name:  <redacted>
# UIN: <redacted>
# URL: <redacted>
######################################################

import random #so we can get random numbers
import turtle # so we can draw on screen

t1 = turtle.Turtle() #declaring turtle 
t1.penup() #makes sure turtle doesnt drag

t1._tracer(0)

t2 = turtle.Turtle() #making second turtle object ill use this for the background rendering 
t2.penup() 
t2._tracer(0)

colors = ['white','black','yellow','green','brown','grey'] #colors stored in list to use later 

def draw_rectangle(turtle,x,y,width,length,pen_color,fill_color,heading_angle,pen_size): #draws a rectangle
  turtle.goto(x,y)
  turtle.color(pen_color)
  turtle.setheading(heading_angle)
  turtle.pensize(pen_size)
  turtle.fillcolor(fill_color)
  turtle.begin_fill()
  turtle.pendown()
  turtle.forward(width)
  turtle.right(90)
  turtle.forward(length)
  turtle.right(90)
  turtle.forward(width)
  turtle.right(90)
  turtle.forward(length)
  turtle.end_fill()
  turtle.penup() 

def draw_equilateral_triangle(turtle,x,y,side_length,pen_color,fill_color,heading_angle,pen_size): #draws a trinagle
  turtle.goto(x,y)
  turtle.color(pen_color)
  turtle.setheading(heading_angle)
  turtle.pensize(pen_size)
  turtle.fillcolor(fill_color)
  turtle.begin_fill()
  turtle.pendown() 
  turtle.forward(side_length) 
  turtle.left(120)
  turtle.forward(side_length)
  turtle.left(120)
  turtle.forward(side_length)
  turtle.end_fill()
  turtle.penup() 

def draw_circle(turtle,x,y,radius,extent,steps,pen_color,fill_color,heading_angle,pen_size): #draws a citrcle
  turtle.goto(x,y)
  turtle.color(pen_color)
  turtle.setheading(heading_angle)
  turtle.pensize(pen_size)
  turtle.fillcolor(fill_color)
  turtle.begin_fill()
  turtle.pendown() 
  turtle.circle(radius,extent,steps)
  turtle.end_fill()
  turtle.penup() 

def draw_parallelogram(turtle,x,y,side_length,side_width,pen_color,fill_color,heading_angle,pen_size): #draws a parallelogra
  turtle.goto(x,y)
  turtle.color(pen_color)
  turtle.setheading(heading_angle)
  turtle.pensize(pen_size)
  turtle.fillcolor(fill_color)
  turtle.begin_fill()
  turtle.pendown() 
  turtle.forward(side_width)
  turtle.right(110)
  turtle.forward(side_length)
  turtle.right(70)
  turtle.forward(side_width)
  turtle.right(110)
  turtle.forward(side_length)
  turtle.end_fill()
  turtle.penup() 

def draw_house(turtle,x,y,base_color,roof_color,window_tint): #draws the house at an x and y coord
  draw_rectangle(turtle,x,y,150,150,colors[1],colors[4],0,5)
  draw_rectangle(turtle,x+100,y-100,25,50,colors[1],colors[0],0,5)
  draw_circle(turtle,x+108, y-130,5,None,None,colors[1],base_color,0,1)
  draw_equilateral_triangle(turtle,x,y,150,colors[1],roof_color,0,5)
  draw_parallelogram(turtle,x,y-150,25,150,colors[1],colors[3],0,5)
  draw_rectangle(turtle,x+60,y+75,25,25,colors[1],window_tint,0,5)

def signature(turtle,x,y,size): #name of the scene and my name aka the author
  turtle.goto(x,y)
  turtle.color(colors[0])
  turtle.write("HOUSE IN THE VOID" + " BY " + "redacted",size)
  print("UIN: redacted" + " " + "redacted 🐸")

def draw_star(turtle,x,y,star_outline_color,star_fill_color,pen_size,heading_angle): # draws fragments in reality aka the stars
  for i in range(5):
    turtle.goto(x,y)
    turtle.color(star_outline_color)
    turtle.setheading(heading_angle)
    turtle.pensize(pen_size)
    turtle.fillcolor(star_fill_color)
    turtle.begin_fill()
    turtle.pendown() 
    turtle.forward(10)
    turtle.right(144)
    turtle.penup()

def set_background_color(color): # just sets the background color
  ribbit = turtle.Screen()
  ribbit.bgcolor(color)

def render_background(turtle): #renders the fragments in reality aka stars multiple times in a random way
  frog = random.randint(0,100) #random integer from 0-100

  if frog > 20: #checks if the random number is greater than 20
    print("Look at all those stars 🤯") 

  for i in range(random.randint(0,100)):
    x = random.randint(-220,220)
    y = random.randint(-220,220)
    draw_star(turtle,x,y,colors[0],colors[2],5,0)
  
def main(): #calls all the functions for the scene to display 
  set_background_color(colors[1])
  render_background(t2)
  signature(t2,0,200,200)
  draw_house(t1,0,0,colors[4],colors[2],colors[5])

main()

## information for scorers

## on what line number is the required for loop?
## <line number> 123 and 103 

## on what line number is the required use of a random number?
## <line number> 123 and 120

## on what line number is the required use of a conditional statement?
## <line number> 121

## on what line number is the required use of a list?
## <line number> Use it for all the colors but the list is declared on line 22
