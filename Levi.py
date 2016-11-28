import turtle
turtle.speed(10)
turtle.penup()
turtle.goto(-100,-100)
turtle.pendown()
def draw(l,n):
    if n==0:
        turtle.forward(l)
        return
    turtle.left(45)
    draw((l/2)*(2**0.5), n - 1)
    turtle.right(90)
    draw((l / 2) * (2 ** 0.5), n - 1)
    turtle.left(45)
draw(500,10)
input()