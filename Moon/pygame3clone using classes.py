import turtle
import time

wn = turtle.Screen()
wn.title("animation screen")
wn.bgcolor("black")

#Creating a player
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("square")
        self.color("green")
        self.frame = 0
        self.frames = ["square", "circle", "turtle"]

    def animate(self):
        self.frame +=1
        if self.frame >= len(self.frames):
            self.frame = 0
        self.shape(self.frames[self.frame])
        #set a timer
        wn.ontimer(self.animate, 500)
    


###Registering images
##wn.register_shape("invader.gif")
##wn.register_shape("inader2.gif")
player = Player()
player.animate()
#This loop works forever
while True:
    wn.update()
    print("main loop")
