import turtle as t

t.shape('turtle')
for i in range(1000):
    t.forward(0.1+0.1*i)
    t.right(10)
t.done()