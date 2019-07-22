import turtle


def draw_square(t, length):
    for i in range(4):
        t.forward(length)
        t.left(90)


def main():
    wn = turtle.Screen()
    wn.bgcolor("green")
    joe = turtle.Turtle()
    joe.color("blue")
    joe.speed(10)
    for i in range(24):
        joe.left(15)
        draw_square(joe, 100)

    wn.exitonclick()


if __name__ == "__main__":
    main()
