import array
import random

IMG_W = 300
IMG_H = 300
PPM_HEADER = f'P6 {IMG_W} {IMG_H} {255} '
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
IMAGE = array.array('B')
FIELD = []

def noise() -> int:
    r = random.randrange(1, 100)
    if r > 70:
        return 1
    else:
        return 0


def field_to_img():
    for p in FIELD:
        if p == 0:
            IMAGE.fromlist(WHITE)
        else:
            IMAGE.fromlist(BLACK)


def main():
    random.seed()

    for _ in range(IMG_W * IMG_H):
        FIELD.append(noise())

    field_to_img()

    with open('test.ppm', 'wb') as f:
        f.write(bytearray(PPM_HEADER, 'ascii'))
        IMAGE.tofile(f)

if __name__ == '__main__':
    main()