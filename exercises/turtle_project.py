"""Creating a little drawing of a house with a fence and some odd little random flowers."""

__author__ = "730472183"

from turtle import Turtle, colormode, done
import random


def draw_square(turtle: Turtle, x: float, y: float, side_length: float, color: str) -> None:
    """Drawing the house."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    i = 0
    while i < 4:
        turtle.forward(side_length)
        turtle.left(90)
        i += 1
    turtle.end_fill()


def draw_triangle(turtle: Turtle, x: float, y: float, side_length: float, color: str) -> None:
    """Drawing the roof."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    i = 0
    while i < 3:
        turtle.forward(side_length)
        turtle.left(120)
        i += 1
    turtle.end_fill()


def draw_line(turtle: Turtle, x1: float, y1: float, x2: float, y2: float, color: str) -> None:
    """Drawing the fence."""
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.color(color)
    turtle.goto(x2, y2)


def draw_flower(turtle: Turtle, x: float, y: float) -> None:
    """Drawing the silly little flowers."""
    colors = ["red", "yellow", "blue", "purple", "orange"]
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    
    i = 0
    while i < 5:
        turtle.color(random.choice(colors))
        turtle.begin_fill()
        turtle.circle(4)
        turtle.end_fill()
        turtle.right(144)
        i += 1


def main() -> None:
    """The main function running the show."""
    colormode(255)
    leo: Turtle = Turtle()
    leo.speed(0)

    draw_square(leo, -50, -100, 100, "beige")

    draw_triangle(leo, -50, 0, 100, "dark red")

    leo.color("grey")
    i = -150
    while i <= 200:
        draw_line(leo, i, -100, i, -50, "grey")
        i += 50

    i = 0
    while i < 5:
        x = random.randint(-150, 150)
        y = random.randint(-50, 100)
        draw_flower(leo, x, y)
        i += 1    

    done()


if __name__ == "__main__":
    main()