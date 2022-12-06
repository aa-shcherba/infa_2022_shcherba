import turtle as t
t.shape('turtle')
x = 1
while x <= 5:
    t.left(180 - (180 / 5))
    t.forward(200)
    x += 1

t.penup()
t.forward(300)
t.pendown()

x = 1
k = 2
while x <= 11:
    t.left(180 - 180*(11-2*k)/11)
    t.forward(200)
    x += 1
t.done()