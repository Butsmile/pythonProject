# coding:utf-8
import turtle as tu
#绘制一个滑稽
#绘制坐标线
def paint_axis():
    tu.pencolor("blue")
    tu.penup()
    tu.goto(-380, 0)
    tu.pendown()
    tu.fd(761)
    tu.penup()
    tu.goto(0, -380)
    tu.setheading(90)
    tu.pendown()
    tu.fd(761)



def paint_init():
    #画布
    tu.screensize(800, 600, "white")
    tu.setup(0.3, 0.3)
    # 画笔
    tu.pensize(3)
    tu.pencolor("brown")
    #tu.hideturtle()

def face():
    pass

def mouth():
    pass

def eyes():
    tu.pencolor("brown")
    #左眼
    tu.penup()
    tu.goto(-50, 20)
    tu.pendown()
    tu.setheading(90)
    tu.circle(20, 180)
    tu.setheading(180)
    tu.fd(30)
    tu.setheading(90)
    tu.circle(-50, 180)
    tu.setheading(180)
    tu.fd(30)

    #右眼
    tu.penup()
    tu.goto(70, 20)
    tu.pendown()
    tu.setheading(90)
    tu.circle(20, 180)
    tu.setheading(180)
    tu.fd(30)
    tu.setheading(90)
    tu.circle(-50, 180)
    tu.setheading(180)
    tu.fd(30)



#run field
paint_init()
paint_axis()
eyes()
tu.done()

