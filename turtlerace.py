import turtle              # 1. import the modules
import random
wn = turtle.Screen()       # 2. Create a screen
wn.bgcolor('lightblue')

lance = turtle.Turtle()    # 3. Create two turtles
andy = turtle.Turtle()
lance.color('red')
andy.color('blue')
lance.shape('turtle')
andy.shape('turtle')
andy.speed(1)
lance.speed(1)

andy.up()                  # 4. Move the turtles to their starting point
lance.up()
andy.goto(-100, 20)
lance.goto(-100, -20)

# your code goes here

steps = random.randrange(25, 50)

for step in range(steps):
    andy.forward(step)
    lance.forward(step)

wn.exitonclick()
