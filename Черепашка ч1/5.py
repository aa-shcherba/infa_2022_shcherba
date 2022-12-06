import turtle as t

n = 12
t.shape('turtle')
for i in range(n):
    t.forward(100)
    t.stamp()
    t.right(180)
    t.forward(100)
    t.right(180+360/n)
t.done()