from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
colormode(255)

#cd -change directory
#ls -list files/folders

leo.forward(300)
leo.left(90)
leo.forward(300)
leo.forward(300)
leo.left(90)

i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(90)
    i = i + 1

leo.penup()
leo.goto(45, 60)
leo.pendown()



leo.color(99, 204, 250)
leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1
leo.end_fill()
leo.speed(50)
leo.hideturtle()

bob: Turtle = Turtle()

side_length: int = 300
 
i: int = 0
while (i < 3):
    bob.forward(side_length)
    side_length = side_length * 0.97
    bob.left(120)
    i = i + 1