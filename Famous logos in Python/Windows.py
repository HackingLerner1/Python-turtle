from turtle import *

speed(1)
bgcolor("black")
penup()

goto(-50,60)
pendown()
color('#00adef')
begin_fill()
goto(100,100)
goto(100,-100)
goto(-50,-60)

goto(-50,60)
end_fill()

color("black")
goto(15,100)
color("black")
width(10)
goto(15,-100)
penup()

goto(100,0)
pendown()

goto(-100,0)

done()
