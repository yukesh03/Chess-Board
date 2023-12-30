import turtle


def draw_square(size, color):
  turtle.begin_fillO turtle.fillcolor(color)

for _ in range(4): 
  turtle.forward(size)
  turtle.right(90)
  turtle.end_fill

def draw_chessboard(rows, columns, square_size):
  colors = ["white", "black"]

for row in range(rows):
  for col in range(columns):
    color_index = (row + col) % 2
    x = col * square_size
    y = row * square_size
    turtle.penup turtle.goto(x, y)
    turtle.pendown()
    draw_square(square_size, colors[color_index])
    
    def main:
    turtle speed (0)
    turtle.hideturtle()
    turtle.bgcolor("white")
    draw_chessboard(8, 8, 30) 
    turtle.done()
    
    if__name__=="__main__":
    main()
