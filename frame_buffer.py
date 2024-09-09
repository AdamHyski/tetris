class frame_buffer:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.buffer = [[' ' for i in range(width)] for j in range(height)]

    def change_pixel(self, x, y, value):
        self.buffer[y][x] = value

    def fill_with_chessboard(self):
        for i in range(self.height ):
            for j in range(self.width ):
                if (i+j)%2 == 1:
                    self.change_pixel(j, i, '█')

    def print_buffer(self):
        for i in range(self.height):
            print(''.join(self.buffer[i]), end='')
