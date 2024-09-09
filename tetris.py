import time

class tetris:
    def __init__(self, width, height, buffer) -> None:
        self.buffer = buffer
        self.object = '█'
        self.reset_object_position()
        self.background =  [[' ' for i in range(width)] for j in range(height)]
        self.width = width
        self.height = height
        self.initial_start_time = time.time_ns()
        self.loop_time = 500000000
        self.next_move_time = self.initial_start_time + self.loop_time

    def reset_object_position(self):
        self.object_position = [5, 0]

    def move_down(self):

        if self.check_collision([0, 1]):

            self.add_object_to_background()
            self.reset_object_position()
        else:
            self.object_position[1] += 1

    def move_left(self):
        if self.check_collision([-1, 0]):
            pass
        else:
            self.object_position[0] -= 1

    def move_right(self):
        if self.check_collision([1, 0]):
            pass
        else:
            self.object_position[0] += 1

    def drow_object(self):
        self.buffer.change_pixel(self.object_position[0], self.object_position[1], self.object)

    def drow_background(self):
        for i in range(self.height):
            for j in range(self.width):
                self.buffer.change_pixel(j, i, self.background[i][j])
        # self.buffer.buffer = self.background

    def check_collision(self, ofset = [0, 0]):
        if self.object_position[1] >= self.height -1 :
            return True
        elif self.background[self.object_position[1] + ofset[1] ][self.object_position[0] + ofset[0] ] == self.object:
            return True

    def add_object_to_background(self):
        self.change_pixel(self.object_position[0], self.object_position[1], self.object)

    def change_pixel(self, x, y, value):
        self.background[y][x] = value

    def event_loop(self):
        while True:
            curent_time = time.time_ns()
            if curent_time > self.next_move_time:
                # self.move_down()
                self.next_move_time += self.loop_time
                # print(curent_time, self.next_move_time )
                self.drow_background()
                self.drow_object()
                self.move_down()
