import turtle
pen = turtle.Turtle()
def star(size):
    while True:
        pen.forward(size)
        pen.right(144)
wow = eval(input('大小:'))
star(wow)