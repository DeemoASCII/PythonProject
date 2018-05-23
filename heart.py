from turtle import *


def go_to(x,y):
    up()
    goto(x,y)
    down()
def big_Circle(size): #函数用于绘制心的大圆
    speed(1)
    for i in range(150):
        forward(size)
        right(0.3)
def small_Circle(size):#函数用于绘制心的小圆
    speed(1)
    for i in range(210):
        forward(size)
        right(0.786)
def line(size):
    speed(1)
    forward(51*size)
def heart(x,y,size):
    go_to(x,y)
    left(150)
    begin_fill()
    line(size)
    big_Circle(size)
    small_Circle(size)
    left(120)
    small_Circle(size)
    big_Circle(size)
    line(size)
    end_fill()
def arrow():
    pensize(10)
    setheading(0)
    go_to(-400,0)
    left(15)
    forward(150)
    go_to(339,178)
    forward(150)
def arrowHead():
    pensize(1)
    speed(1)
    color('red','red')
    begin_fill()
    left(120)
    forward(20)
    right(150)
    forward(35)
    right(120)
    forward(35)
    right(150)
    forward(20)
    end_fill()
def main():
    screensize()
    pensize(2)
    color('red','pink')
    # getscreen().tracer(30, 0) #取消注释后，快速显示图案
    heart(200,0,1)#画出第一颗心，前面两个参数控制心的位置，函数最后一个参数可控制心的大小
    setheading(0)#使画笔的方向朝向x轴正方向
    heart(-80,-100,1.5)#画出第二颗心
    arrow()#画出穿过两颗心的直线
    arrowHead()#画出箭的箭头
    pencolor('black')
    go_to(90,100)
    write("肖向彬  &  唐宇晨",align="center",font=("楷体",30,"normal"))
    go_to(180,-50)
    pencolor('pink')
    write("奉日月以为盟，昭天地以为鉴",align="center",font=("楷体",15,"normal"))
    go_to(180, -80)
    write("啸山河以为证，敬鬼神以为凭",align="center",font=("楷体",15,"normal"))
    go_to(180, -110)
    write("从此山高不阻其志，涧深不断其行",align="center",font=("楷体",15,"normal"))
    go_to(180, -140)
    write("流年不毁其意，风霜不掩其情",align="center",font=("楷体",15,"normal"))
    go_to(180, -170)
    write("纵然前路荆棘遍野，亦将坦然无惧仗剑随行",align="center",font=("楷体",15,"normal"))
    go_to(180, -200)
    write("生死不离，从一而终！",align="center",font=("楷体",15,"normal"))
    done()

if __name__ == '__main__':
    main()
