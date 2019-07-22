import turtle


def draw_wheel(t, length, angle):
    t.left(angle)
    draw_square(t, length)


def draw_square(t, length):
    for i in range(4):
        t.forward(length)
        t.left(90)


def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    joe = turtle.Turtle()
    joe.color("blue")
    joe.speed(10)
    for i in range(24):
        draw_wheel(joe, 100, 15)

    wn.exitonclick()


if __name__ == "__main__":
    main()
