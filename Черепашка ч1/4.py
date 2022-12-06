import turtle as t

t.shape('turtle')
x=0
for i in range(10):
    for j in range(4):
        t.forward(15*(i+1)+x)
        t.right(90)
    t.penup()
    t.left(135)
    t.forward(15*2**0.5)
    t.right(135)
    x=x+15
    t.pendown()
t.done()