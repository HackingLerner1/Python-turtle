#windows 11 logo in Python
from turtle import *
speed(5.5)
pu()
goto(-100,-100)
pd()
fillcolor("#0078d4")
pencolor("#0077d4")
bgcolor("white")
lt(90)
begin_fill()
for i in range(4):
    fd(350)
    rt(90)
end_fill()
pu()
pencolor("white")
goto(80,-100)
pd()
width(6)
fd(355)

pu()
pencolor("white")
goto(-100,70)
pd()
rt(90)
width(6)
fd(355)

ht()
done()
