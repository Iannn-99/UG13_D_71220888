import turtle
t=turtle.Screen()
t.bgcolor("#4649FF")
def drawHuruf(x, y, panjang, lebar):
    t.up()
    t.goto(x,y)
    t.down()
    t.pensize(20)
    t.forward(100)
    t.left(90)
drawHuruf(0,0, 50, 100)