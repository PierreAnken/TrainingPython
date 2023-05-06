# Exercice 2.a (test et identification)
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
        turtle.color("white")
        turtle.stamp()
