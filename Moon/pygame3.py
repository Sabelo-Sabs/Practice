import turtle
import time

wn = turtle.Screen()
wn.title("animation screen")
wn.bgcolor("black")

#Creating a player
player = turtle.Turtle()
player.shape("square")
player.color("green")
player.frame = 0
player.frames = ["square", "circle", "turtle"]

###Registering images
##wn.register_shape("invader.gif")
##wn.register_shape("inader2.gif")

def player_animate():
    if player.frame == 0:
        player.shape("circle")
        player.frame = 1
    elif player.frame == 1:
        player.shape("square")
        player.frame = 0
    #set a timer
    wn.ontimer(player_animate, 500)
    
player_animate()
#This loop works forever
while True:
    wn.update()
    print("main loop")
    











#Last line keeps the window open.
wn.mainloop()
