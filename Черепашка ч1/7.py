import turtle as t

t.shape('turtle')
for i in range(100):
    t.right(90)
    t.forward(10*(i+1))
t.done()