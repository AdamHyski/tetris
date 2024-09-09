#!/usr/bin/env python3.11
import time
from frame_buffer import frame_buffer
from screen_procedure import screen
from tetris import tetris

def draw_square(width, height):
    print ('█'*(width+2))
    for i in range(height):
        print ('█' + ' '*width + '█')
    print ('█'*(width+2))



def main ():

    width = 11
    height = 20

    buffer = frame_buffer(width, height)
    scr = screen(buffer)

    game = tetris(width, height, buffer)

    game.event_loop()

    # for i in range(height * 10):

    #     game.drow_background()
    #     game.drow_object()
    #     game.move_down()
    #     scr.print_buffer()
    #     time.sleep(0.1)


    # for i in range(height):
    #     buffer.change_pixel(5, i, '█')
    #     scr.print_buffer()
    #     buffer.change_pixel(5, i, ' ')
    #     time.sleep(0.1)

if __name__ == '__main__':
    main ()
