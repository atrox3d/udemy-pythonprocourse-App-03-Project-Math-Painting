from canvas import Canvas
from shapes import Rectangle, Square

canvas_width = int(input('Enter canvas width: '))
canvas_heigth = int(input('Enter canvas heigth: '))

colors = {
    'white': (255, 255, 255),
    'black': (0, 0, 0)
}
while (canvas_color := input("Enter canvas color (white or black): ").lower()) not in colors.keys():
    pass
canvas = Canvas(
    height=canvas_heigth,
    width=canvas_width,
    color=colors[canvas_color]
)
choices = ['rectangle', 'square']
while True:                                                         # main loop
    while (                                                         # shape loop
            shape_type := input(
                'What would you like to draw? '
                '(square, rectangle, quit exits): '
            ).lower()
    ) in choices:
        row = int(input(f'Enter row for {shape_type}: '))           # row is common to all shapes
        column = int(input(f'Enter column for {shape_type}: '))     # colums is commont to all shapes

        if shape_type == "rectangle":                               # rectangtle: width, heigth
            width = int(input(f'Enter width of {shape_type}: '))
            height = int(input(f'Enter height of {shape_type}: '))
        else:
            side = int(input(f'Enter side of {shape_type}: '))      # square: side, side

        while (red := int(input(f'How much red (0-255) for {shape_type}?: '))) not in range(0, 256):
            pass

        while (green := int(input(f'How much green (0-255) for {shape_type}?: '))) not in range(0, 256):
            pass

        while (blue := int(input(f'How much blue (0-255) for {shape_type}?: '))) not in range(0, 256):
            pass

        if shape_type == 'rectangle':
            r1 = Rectangle(row=row, column=column, height=height, width=width, color=(red, green, blue))
            r1.draw(canvas)
        else:
            s1 = Square(row=row, column=column, side=side, color=(red, green, blue))
            s1.draw(canvas)
    else:
        if shape_type == 'quit':                                    # shape is not in list
            break                                                   # quit breaks, everything else continues

canvas.make('images/shapes.png')

