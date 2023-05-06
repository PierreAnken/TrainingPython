# Exercice 2.b (première composition)
import turtle

turtle.up()
wn = turtle.Screen()
wn.bgcolor('black')
turtle.shape('square')
turtle.shapesize(0.9)

for x in range(-50, 51, 20):
    for y in range(-50, 51, 20):
        turtle.goto(x, y)
        turtle.stamp()

        if x == 0 or y == 0:
            turtle.color("white")
        elif x > 0 and y > 0:
            turtle.color("green")
        elif x < 0 and y < 0:
            turtle.color("red")
        elif x > 0 and y < 0:
            turtle.color("blue")
        elif x < 0 and y > 0:
            turtle.color("magenta")
