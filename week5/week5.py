# import random
# for i in range(10):
#     print(random.random())
#
# for i in range(10):
#     print(random.randint(25, 35))
#
# import math
# a = int(input("Enter lenght:"))
# b = int(input("Enter width:"))
# hypotenuse = math.sqrt(a**2 + b**2)
# print(hypotenuse)
#
# import math
# def areaofcircle(r):
#     return math.pi * r**2
# print(areaofcircle(int(input("Enter radius:"))))
#
# import turtle
# def drawstart(t, side):
#     for i in range(5):
#         t.forward(side)
#         t.right(144)
# screen = turtle.Screen()
# tess = turtle.Turtle()
# drawstart(tess, 100)
# screen.exitonclick()

def drawsquare(t, side):
    for i in range(4):
        t.forward(side)
        t.left(90)
# import turtle
# tess = turtle.Turtle()
# screen = turtle.Screen()
# screen.bgcolor("lightgreen")
# tess.color("pink")
# tess.speed(99999)
# tess.pensize(3)
# for i in range(5):
#     drawsquare(tess, 20)
#     tess.penup()
#     tess.forward(40)
#     tess.pendown()
# screen.exitonclick()

# import turtle
# tess = turtle.Turtle()
# screen = turtle.Screen()
# screen.bgcolor("lightgreen")
# tess.color("pink")
# tess.speed(99999)
# tess.pensize(3)
# for i in range(20, 120, 20):
#     drawsquare(tess, i)
#     tess.penup()
#     tess.backward(10)
#     tess.right(90)
#     tess.forward(10)
#     tess.left(90)
#     tess.pendown()
# screen.exitonclick()