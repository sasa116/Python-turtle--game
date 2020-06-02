import turtle
import math
import random
import os

wd=turtle.Screen()
wd.bgcolor("lightgreen")
wd.bgpic("hhh.gif")



 #for boundary
boundary=turtle.Turtle()
boundary.penup()
boundary.setposition(-250,-250)
boundary.color("black")
boundary.pendown()
boundary.pensize(5)
for side in range(4):
    boundary.forward(500)
    boundary.left(90)

boundary.hideturtle()    
 
 #end game
end=turtle.Turtle()
end.hideturtle()
 #score turtle
sco=turtle.Turtle()
sco.hideturtle()

 #main player
player=turtle.Turtle()
player.shape("turtle")
player.penup()
player.speed(0)

 #games goal
goal=turtle.Turtle()
goal.color("red")
goal.shape("circle")
goal.penup()
goal.speed(0)
goal.setposition(random.randint(-250,250),random.randint(-250,250))


speed=0.25


def turnleft():
     player.left(90)

def turnright():
     player.right(90)
     
def increase_speed():
     global speed
     speed=speed+0.25

def decrease_speed():
     global speed
     speed=speed-0.25     

score=0

 #players keys control   
turtle.listen()
turtle.onkey(turnleft,"Left")
turtle.onkey(turnright,"Right")
turtle.onkey(increase_speed,"Up")
turtle.onkey(decrease_speed,"Down")
while True:
    player.forward(speed)
      #boundary restriction
    if player.xcor() > 250 or player.xcor() < -250:
        end.penup()
        end.hideturtle()
        end.setposition(0,0)
        end.write("Game over",False,align="center",font=("Arial",40,"bold"))
        exit()
    if player.ycor() > 250 or player.ycor() < -250:
        end.penup()
        end.hideturtle()
        end.setposition(0,0)
        end.write("Game over",False,align="center",font=("Arial",40,"bold"))
        exit()
    d = math.sqrt(math.pow(player.xcor()-goal.xcor(),2) + math.pow(player.ycor()-goal.ycor(),2))
    if d < 20 :
        goal.setposition(random.randint(-250,250),random.randint(-250,250))
        score=score+1
        sco.undo()
        sco.penup()
        sco.hideturtle()
        sco.setposition(-250,260)
        s="score :%d" %score
        sco.write(s,False,align="left",font=("Arial",14,"normal"))
















