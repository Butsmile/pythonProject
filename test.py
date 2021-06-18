import turtle
turtle.tracer(0)
turtle.pensize(2)
turtle.bgcolor("black")
colors=["red","blue","yellow","purple"]
for x in range(300):
    turtle.color(colors[x%4])
    turtle.forward(2*x)
    turtle.left(91)
turtle.done()
