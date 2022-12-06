import turtle
t = turtle.Turtle()
t.shape('turtle')
t.left(90)
n = 100

x = 1
while x <= 20:
    t.circle(n)
    t.circle(-n)
    n += 10
    x += 1
t.done()