class screen:
    def __init__(self, buffer):
        self.buffer = buffer.buffer
        self.width = buffer.width + 2
        self.height = buffer.height + 2

    def clean_screen(self):
        claer = "\033[2J"
        new_frame = "\033[;H"
        print(claer,new_frame, end='')

    # def draw_border(self):
    #     for i in range(self.height):
    #         for j in range(self.width):
    #             if i == 0 or i == self.height-1:
    #                 self.change_pixel(j-1, i-1, '█')
    #             if j == 0 or j == self.width-1:
    #                 self.change_pixel(j-1, i-1, '█')
    def draw_border(self):
        for i in range(self.height):
            for j in range(self.width):
                if i == 0 or i == self.height-1:
                    self.screen[i][j] = '█'
                if j == 0 or j == self.width-1:
                    self.screen[i][j] = '█'

    def prepare_screen(self):
        self.screen = [[' ' for i in range(self.width)] for j in range(self.height)]
        for i in range(self.height-2):
            for j in range(self.width-2):
                self.screen[i+1][j+1] = self.buffer[i][j]

    def print_screen(self, game):
        self.clean_screen()
        for i in range(self.height+2):
            print(''.join(self.screen[i]))

    def print_buffer(self, game):
        self.clean_screen()
        self.prepare_screen()
        self.draw_border()
        for i in range(self.height):
            print(''.join(self.screen[i]), i-1)
        print('Position: ', game.object_position)
