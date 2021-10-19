#WE're going to be using turtle module
import turtle as tut
import random

#Creating a screen
wn = tut.Screen()
wn.bgcolor("black")
wn.title("Bouncing ball simulation")
#Turns off the screen
wn.tracer(0)

#Creating a balls
balls = []
for x in range(15):
    balls.append(tut.Turtle())
    
#Randomizing a color and shape
color = ["purple", "green", "red", "yellow", "blue", "white", "cyan"]
shapes = ["triangle", "square", "circle", "turtle"]
#Making a loop to loor around all 10 balls
for ball in balls:
    ball.shape(random.choice(shapes))
    ball.penup()
    ball.speed(0)
    x = random.randint(-290,290)
    y = random.randint(200,400)
    ball.color(random.choice(color))
    ball.goto(x,y)
    ball.dy = 0
    ball.dx = random.randint(-2,2)
    #rotating the ball
    ball.da = random.randint(-5,5)

gravity = 0.1

#making a loop that runs forever for the ball to keep on falling

while True:
    wn.update()
    for ball in balls:
        ball.rt(ball.da)
        ball.dy -= gravity
        ball.sety(ball.ycor() + ball.dy)
    
     #for speed x coardinates
        ball.setx(ball.xcor() + ball.dx)

    #check for wall collision
        if ball.xcor() > 300:
            ball.dx *= -1
            ball.da *= -1
        if ball.xcor() < -300:
            ball.da *= -1
            ball.dx *= -1

    #Check for bounce.
        if ball.ycor() < -300:
            ball.sety(-300)
            ball.da *= -1
            ball.dy *= -1


    #check for collision between balls
    for i in range(0, len(balls)):
        for j in range(i+1, len(balls)):
            
            #checking for distance
            if balls[i].distance(balls[j]) < 20:
                #Changing color after collision.
                #balls[i].color(random.choice(color))
                #balls[j].color(random.choice(color))
                
                balls[i].dx, balls[j].dx = balls[j].dx, balls[i].dx
                balls[i].dy, balls[j].dy = balls[j].dy, balls[i].dy
                
                       
        

















#Last line of our code, this keeps our screen on the loop
wn.mainloop()
