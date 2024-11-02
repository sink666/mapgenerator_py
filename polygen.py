import random

# black, white, red, blue, green, yellow, cyan, magenta
PALETTE = ['000000','FFFFFF','FF0000','00FF00','0000FF','FFFF00','00FFFF','FF00FF']

def put_file(width, height, data):
    filename = "test.ppm"

    with open(filename, 'wb') as f:
        f.write(bytearray(f'P6 {width} {height} {255} ', 'ascii'))

        for p in data:
            f.write(bytes.fromhex(PALETTE[p]))


def main():
    # random.seed()
    img = [ 
        0, 1, 2, 
        3, 4, 5, 
        6, 7, 0, 
    ]

    put_file(3, 3, img)



if __name__ == '__main__':
    main()