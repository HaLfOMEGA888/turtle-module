import turtle
sq = turtle.Turtle()
sq.pensize(5)
sq.color("green")
sq.fillcolor("Light green")
sq.begin_fill()
for sqr in [1, 2, 3, 4]:
    sq.forward(100)
    sq.right(90)
sq.end_fill()
