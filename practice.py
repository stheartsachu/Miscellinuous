from turtle import*
from os import*
import turtle
import os
#background
a = turtle.Screen()
a.title('----GUARDIAN OF THE SPACE----')
a.bgcolor('black')
#border
border=turtle.Turtle()
border.speed(0)
border.color('white')
border.penup()
border.setposition(-300,-300)
border.pendown()
border.pensize(3)
for side in range(4):
    border.fd(600)
    border.lt(90)
border.hideturtle()
#Create the player
player=turtle.Turtle()
player.color('purple')
player.shape('triangle')
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)
playerspeed=15
#create left and right movement for the player
def move_left():
    x=player.xcor()
    x -= playerspeed
    if x<-280:
        x=-280
    player.setx(x)
def move_right():
    x=player.xcor()
    x += playerspeed
    if x>280:
        x=280
    player.setx(x)

a.listen()
a.onkey(move_left,"left")
a.onkey(move_right,"right")
