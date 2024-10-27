import array
import random

IMG_W = 100
IMG_H = 100
PPM_HEADER = f'P6 {IMG_W} {IMG_H} {255} '
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
image = array.array('B')
field = []

def noise() -> int:
    r = random.randrange(1, 100)
    if r > 35:
        return 1
    else:
        return 0


def field_to_img():
    image.clear()

    for p in field:
        if p == 0:
            image.fromlist(BLACK)
        else:
            image.fromlist(WHITE)


def should_be_wall(x, y) -> bool:
    acc = 0

    if x == 0 or x == (IMG_W - 1) or y == 0 or y == (IMG_H - 1):
        return True

    for yp in (-1, 0, 1):
        for xp in (-1, 0, 1):
            if field[(x + xp) + ((y + yp) * IMG_W)] == 0:
                acc += 1
        
    if acc >= 4:
        return True
    else:
        return False



def iterate_world():
    newfield = []

    for y in range(IMG_H):
        for x in range(IMG_W):
            if should_be_wall(x, y) == True:
                newfield.append(0)
            else:
                newfield.append(1)

    field[:] = newfield


def out_to_file(file_num):
    filename = "test" + str(file_num) + ".ppm"

    with open(filename, 'wb') as f:
        f.write(bytearray(PPM_HEADER, 'ascii'))
        image.tofile(f)


def main():
    random.seed()

    for _ in range(IMG_W * IMG_H):
        field.append(noise())

    for fv in range(9):
        iterate_world()
        field_to_img()
        out_to_file(fv)


if __name__ == '__main__':
    main()