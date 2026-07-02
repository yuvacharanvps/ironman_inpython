#this is code to draw iron man face in python
turtle.pendown()
    turtle.color('red')
    turtle.begin_fill()
    for i in range(len(piece[0])):
        x,y=piece[0][i]
        turtle.goto(x,y)

    for i in range(len(piece[1])):
        x,y=piece[1][i]
        turtle.goto(x,y)
    turtle.end_fill()
draw_piece(piece1,piece1Goto)
draw_piece(piece2,piece2Goto)
draw_piece(piece3,piece3Goto)
turtle.hideturtle()
turtle.done()
