from turtle import*
speed(7)
width(1)
penup()
goto(-170,-230)
pendown()
color('#3B9AF0')
begin_fill()
for i in range(4):
    fd(320)
    circle(100,90)
end_fill()
goto(155,-90)
pendown()
color('white')
begin_fill()
lt(120)
fd(60)
rt(120)
fd(40)
circle(18,180)
fd(62)
rt(60)
fd(165)
lt(110)
circle(55,60)
lt(10)
fd(219)
circle(18,180)
end_fill()
penup()
goto(-135,-105)
pendown()
begin_fill()
rt(60)
fd(60)
lt(90)
circle(65,33)
lt(57)
fd(50)
circle(18,180)
end_fill()
penup()
rt(180)
circle(-18,180)
fd(57)
pendown()
begin_fill()
lt(120)
fd(40)
circle(-18,180)
fd(62)
lt(60)
fd(182)
lt(60)
fd(30)
circle(-18,180)
fd(10)
lt(120)
fd(10)
circle(-18,180)
fd(212)
lt(120)
fd(123)
rt(50)
circle(-55,40)
rt(90)
fd(205)
end_fill()
hideturtle()
done()
