import turtle
import time

length = int(input("Size: "))

turtle = turtle.Turtle()
turtle.color("red")
turtle.begin_fill()
turtle.left(80)
turtle.forward(length)
turtle.right(160)
turtle.forward(length)

turtle.left(100)
turtle.forward(length)
turtle.right(160)
turtle.forward(length)

turtle.left(60)
turtle.forward(length)
turtle.right(160)
turtle.forward(length)

turtle.left(120)
turtle.forward(length)
turtle.right(160)
turtle.forward(length)

turtle.left(90)
turtle.forward(length)
turtle.right(160)
turtle.forward(length * 1.2)
turtle.end_fill()

time.sleep(3)
