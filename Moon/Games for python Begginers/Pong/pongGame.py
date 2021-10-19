67# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 13:53:57 2021

@author: sabelo sibabalwe
"""
#importing the turtle module, this is strictly for begginers
import turtle
import winsound
#creating a window
wn = turtle.Screen()
wn.title("Pong Game By Sabs")
wn.bgcolor("black")
wn.setup(width=600,height = 400)

#This stops the window from updating, lets us update it manualy.
#This allows for our game to be fast
wn.tracer(0)


#Score
Score1 = 0
Score2 = 0

#Player A
Player_1 = turtle.Turtle()
#Setting speed for our player
Player_1.speed(0)
#------------------------
Player_1.shape("square")
Player_1.color("Blue")
Player_1.shapesize(stretch_wid = 5, stretch_len = 1)
Player_1.penup()
#Starting position
Player_1.goto(-250,0)


#Player B
Player_2 = turtle.Turtle()
#Setting speed for our player
Player_2.speed(0)
#------------------------
Player_2.shape("square")
Player_2.color("Blue")
Player_2.shapesize(stretch_wid = 5, stretch_len = 1)
Player_2.penup()
#Starting position
Player_2.goto(250,0)

#Ball
Ball1 = turtle.Turtle()
#Setting speed for our player
Ball1.speed(0)
#------------------------
Ball1.shape("square")
Ball1.color("Blue")
Ball1.penup()
#Starting position
Ball1.goto(0,0)
#Everytime the ball moves its gonna go two pixels
Ball1.dx = 0.34
Ball1.dy = -0.34


#Ball2
Ball2 = turtle.Turtle()
#Setting speed for our player
Ball2.speed(0)
#------------------------
Ball2.shape("square")
Ball2.color("White")
Ball2.penup()
#Starting position
Ball2.goto(0,0)
#Everytime the ball moves its gonna go two pixels
Ball2.dx =-0.34
Ball2.dy = -0.34



#Creating a list
Balls = [Ball1,Ball2]

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,160)
pen.write("Player A: 0  Player B: 0",align= "center", font=("Courier",24,"bold"))

#Function for player 1
def Player1_up():
    y = Player_1.ycor()
    y +=20
    Player_1.sety(y)

def Player1_down():
    y = Player_1.ycor()
    y -=20
    Player_1.sety(y)

#Functions for player2
def Player2_up():
    y = Player_2.ycor()
    y +=20
    Player_2.sety(y)

def Player2_down():
    y = Player_2.ycor()
    y -=20
    Player_2.sety(y)

#Keyboard binding
wn.listen()
wn.onkeypress(Player1_up, "x")
wn.onkeypress(Player1_down, "z")

wn.onkeypress(Player2_up, "l")
wn.onkeypress(Player2_down, "k")



#Main game loop
while True:
    wn.update()

    for Ball in Balls:
        
    #move the ball
        Ball.setx(Ball.xcor() + Ball.dx)
        Ball.sety(Ball.ycor() + Ball.dy)


        #Boarder checking
        if Ball.ycor() > 190:
            Ball.sety(190)
            Ball.dy *= -1
            #winsound.PlaySound("Bounce.wav", winsound.SND_ASYNC)
        if Ball.ycor() < -190:
            Ball.sety(-190)
            Ball.dy *= -1
            #winsound.PlaySound("Bounce.wav", winsound.SND_ASYNC)

        if Ball.xcor() > 290:
            Ball.goto(0,0)
            Ball.dx *= -1
            Score1 += 1
            pen.clear()
            pen.write(f"Player A: {Score1}  Player B: {Score2}",align= "center", font=("Courier",24,"bold"))


            
        if Ball.xcor() < -290:
            Ball.goto(0,0)
            Ball.dx *= -1
            Score2 += 1
            pen.clear()
            pen.write(f"Player A: {Score1}  Player B: {Score2}",align= "center", font=("Courier",24,"bold"))

        #Player and Ball collisions
        if (Ball.xcor() > 240 and Ball.xcor() < 250) and (Ball.ycor() < Player_2.ycor() + 40 and Ball.ycor() > Player_2.ycor() -40):
            Ball.setx(240)
            Ball.dx *= -1
            #winsound.PlaySound("Jump.wav", winsound.SND_ASYNC)

        if (Ball.xcor() <- 240 and Ball.xcor() > -250) and (Ball.ycor() < Player_1.ycor() + 40 and Ball.ycor() > Player_1.ycor() -40):
            Ball.setx(-240)
            Ball.dx *= -1
            #winsound.PlaySound("Jump.wav", winsound.SND_ASYNC)

        ClosestBall = Balls[0]
        for Ball in Balls:
            if Ball.xcor() > ClosestBall.xcor():
                ClosestBall = Ball
            if Player_2.ycor() < ClosestBall.ycor() and (abs(Player_2.ycor() - ClosestBall.ycor()) > 20):
                Player2_up()
            elif Player_2.ycor() > ClosestBall.ycor() and (abs(Player_2.ycor() - ClosestBall.ycor()) > 20):
                Player2_down()

##    #AI player
##    if Ball.xcor() > Ball2.xcor():
##        
        if Player_2.ycor() < Ball.ycor() and (abs(Player_2.ycor() - Ball.ycor()) > 20):
            Player2_up()
            
        elif Player_2.ycor() > Ball.ycor() and (abs(Player_2.ycor() - Ball.ycor()) > 20):
            Player2_down()
wn.mainloop()
