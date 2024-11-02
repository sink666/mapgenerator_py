import random

# black, white, red, blue, green, yellow, cyan, magenta
PALETTE = [
    [0, 0, 0],
    [255, 255, 255],
    [255, 0, 0],
    [0, 255, 0],
    [0, 0, 255],
    [255, 255, 0],
    [0, 255, 255],
    [255, 0, 255]
]

class Output:
    def __init__(self) -> None:
        self.img_num = 0
        self.image = []
        
    def data_to_img(self, data):
        self.image.clear()

        for p in data:
            self.image.extend(PALETTE[p])

    def put_file(self, width, height):
        filename = "test" + str(self.img_num) + ".ppm"

        with open(filename, 'wb') as f:
            f.write(bytearray(f'P6 {width} {height} {255} ', 'ascii'))
            f.write(bytes(self.image))

        self.img_num += 1



def main():
    random.seed()



if __name__ == '__main__':
    main()