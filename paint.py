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
    #初始设置
    #画布
    tu.screensize(800, 600, "white")
    tu.setup(0.3, 0.3)
    # 画笔
    tu.pensize(3)
    tu.pencolor("brown")
    tu.speed(10)
    tu.shape("turtle")
    tu.hideturtle()

def funny():
    #初始化
    paint_init()
    # paint_axis()
    #脸
    tu.penup()
    tu.goto(0, -150)
    tu.pencolor("brown")
    tu.pendown()
    tu.setheading(0)
    tu.fillcolor("yellow")
    tu.begin_fill()
    tu.circle(150)
    tu.end_fill()

    #眼眶
    tu.pencolor("brown")
    #左眼眶
    tu.penup()
    tu.goto(-50, 20)
    tu.fillcolor("white")
    tu.pendown()
    tu.begin_fill()
    tu.setheading(90)
    tu.circle(20, 180)
    tu.setheading(180)
    tu.fd(30)
    tu.setheading(90)
    tu.circle(-50, 180)
    tu.setheading(180)
    tu.fd(30)
    tu.end_fill()

    #右眼眶
    tu.penup()
    tu.goto(90, 20)
    tu.pendown()
    tu.begin_fill()
    tu.setheading(90)
    tu.circle(20, 180)
    tu.setheading(180)
    tu.fd(30)
    tu.setheading(90)
    tu.circle(-50, 180)
    tu.setheading(180)
    tu.fd(30)
    tu.end_fill()

    #眼珠
    #左眼珠
    tu.penup()
    tu.goto(-105, 20)
    tu.fillcolor("black")
    tu.setheading(0)
    tu.down()
    tu.begin_fill()
    tu.circle(14)
    tu.end_fill()

    #右眼珠
    tu.penup()
    tu.goto(35, 20)
    tu.fillcolor("black")
    tu.setheading(0)
    tu.down()
    tu.begin_fill()
    tu.circle(14)
    tu.end_fill()

    # 嘴巴
    tu.penup()
    tu.goto(-120, -20)
    tu.pencolor("brown")
    tu.setheading(270)
    tu.pendown()
    tu.circle(120, 180)  # 半径为正数时，圆心在右边画圆，负数左边画圆

    tu.done()


