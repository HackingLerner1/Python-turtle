#awesome design 142 in Pytohn
from turtle import *
import colorsys
tracer(100)
bgcolor("black")

def H():
    h = 0
    n = 101
    up()
    goto(0,60)
    down()
    pensize(5)
    for i in range(100):
        c = colorsys.hsv_to_rgb(h,1,1)
        color(c)
        h +=1/n
        fd(51)
        circle(i,5)
        for k in range(i):
            fd(42)
            rt(63)
            bk(5)
            circle(k,10)
            rt(51)         
            
H()
for p in range(11):
    H()
ht()
done()
