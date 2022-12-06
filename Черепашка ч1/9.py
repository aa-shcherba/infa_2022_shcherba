import turtle as t
t.shape('turtle')

n = int(t.textinput(u"Введите количество лепестков.", "Введите количество окружностей: "))
x = 1
while x <= n:
    t.circle(50)
    t.left(360 / n)
    x += 1

t.done()