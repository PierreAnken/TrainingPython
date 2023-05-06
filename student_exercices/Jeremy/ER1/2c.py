# Exercice 2.c (seconde composition)
import turtle

turtle.up()
wn = turtle.Screen()
wn.bgcolor("black")
turtle.shape("square")
turtle.shapesize(0.9)

# les boucles for ci-dessous permettent de parcourir tous
# les points d’une image
for x in range(-100, 101, 20):
    for y in range(-100, 101, 20):
        # les instructions ci-dessous traitent chaque point
        # composant l’image selon leur position (x,y)
        turtle.goto(x, y)

        if -90 < x < 90 and -30 < y < 30:
            turtle.color("white")
        elif -90 < y < 90 and -30 < x < 30:
            turtle.color("white")
        else:
            turtle.color("red")
        turtle.stamp()
