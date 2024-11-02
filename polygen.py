import random
from PIL import Image, ImageDraw

# black, white, red, blue, green, yellow, cyan, magenta
PALETTE = ['#000000','#FFFFFF','#FF0000','#00FF00','#0000FF','#FFFF00','#00FFFF','#FF00FF']

class Poly:
    def __init__(self, num_sides, xy, bound_sq) -> None:
        self.sides = []
        self.xy = xy

        for _ in range(num_sides):
            sqgen = (random.randrange(0, bound_sq), random.randrange(0, bound_sq))
            nextp = (self.xy[0] + sqgen[0], self.xy[1] + sqgen[1])
            self.sides.append(nextp)



def main():
    random.seed()

    img = Image.new('RGB', (800, 600), color = PALETTE[1])

    draw = ImageDraw.Draw(img)

    poly = Poly(4, (200, 200), 200)
    draw.polygon(poly.sides, fill = PALETTE[7])

    img.save("out.png")


if __name__ == '__main__':
    main()