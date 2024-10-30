import random

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
WALL = 0
SPACE = 1

class Generator:
    def __init__(self, f_width, f_height, weight) -> None:
        self.width = f_width
        self.height = f_height
        self.rand_weight = weight
        self.field = []

    def __get_in_field(self, x, y):
        return self.field[x + (y * self.width)]
    
    def __should_be_wall(self, x, y) -> bool:
        acc = 0

        if x == 0 or x == (self.width - 1) or y == 0 or y == (self.height - 1):
            return False

        for yp in (-1, 0, 1):
            for xp in (-1, 0, 1):
                if self.__get_in_field(x + xp, y + yp) == WALL:
                    acc += 1
        
        return True if acc >= 5 else False
        
    def iterate_world(self):
        newfield = []

        for y in range(self.height):
            for x in range(self.width):
                if self.__should_be_wall( x, y):
                    newfield.append(WALL)
                else:
                    newfield.append(SPACE)

        self.field[:] = newfield



class Output:
    def __init__(self) -> None:
        self.img_num = 0
        self.image = []
        
    def field_to_img(self, field):
        self.image.clear()

        for p in field:
            if p == WALL:
                self.image.extend(BLACK)
            else:
                self.image.extend(WHITE)

    def put_file(self, width, height):
        filename = "test" + str(self.img_num) + ".ppm"

        with open(filename, 'wb') as f:
            f.write(bytearray(f'P6 {width} {height} {255} ', 'ascii'))
            f.write(bytes(self.image))

        self.img_num += 1



def main():
    random.seed()
    gen = Generator(100, 100, 50)
    out = Output()

    for _ in range(gen.width * gen.height):
        if random.randrange(1, 100) < gen.rand_weight:
            gen.field.append(WALL)
        else:
            gen.field.append(SPACE)

    for _ in range(20):
        gen.iterate_world()
        out.field_to_img(gen.field)
        out.put_file(gen.width, gen.height)


if __name__ == '__main__':
    main()