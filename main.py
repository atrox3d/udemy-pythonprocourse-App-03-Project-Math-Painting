from canvas import canvas
from shapes import Rectangle, Square

r1 = Rectangle(row=1, column=6, height=7, width=10, color=(100, 200, 125))
r1.draw(canvas)
s1 = Square(row=1, column=3, side=3, color=(0, 100, 222))
s1.draw(canvas)
canvas.make('images/test.png')

