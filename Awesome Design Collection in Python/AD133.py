#awesome design 133 in Python
from turtle import *
import colorsys
tracer(232)
bgcolor("black")

def H():
    h = 0
    n =8

    for i in range(250):
        c = colorsys.hsv_to_rgb(h,1,1)
        color('black')
        up()
        goto(0,0)
        down()
        h +=1/n
        pensize(1)
        rt(452)
        circle(i,9)
        lt(24)
        fd(i*10)
        for j in range(i):
            color(c)
            fillcolor("black")
            begin_fill()
            rt(356)
            circle(j,93,steps=10)
            end_fill()
        
H()        
ht()
done()
