#!/usr/bin/env python3.11
import time

from frame_buffer import frame_buffer
from screen_procedure import screen
from tetris import tetris
from pynput.keyboard import Key, Listener
import threading

def keyboard_listener(game):
    with Listener(on_press=game.on_press, on_release=game.on_release) as listener:
        listener.join()

def event_loop(game, buffer, scr):

    listener_thread = threading.Thread(target=keyboard_listener, args=(game,))
    listener_thread.daemon = True  # Dzięki temu wątek zakończy się razem z programem
    listener_thread.start()

    while True:
        curent_time = time.time_ns()
        if curent_time > game.next_move_time:
            # game.move_down()
            game.next_move_time += game.loop_time
            # print(curent_time, game.next_move_time )
            game.drow_background()
            game.drow_object()
            game.move_down()
            scr.print_buffer(game)

        if game.needs_redraw:
            game.needs_redraw = False
            # game.drow_background()
            # game.drow_object()
            scr.print_buffer(game)



def main ():

    width = 10
    height = 20

    buffer = frame_buffer(width, height)
    scr = screen(buffer)

    game = tetris(width, height, buffer)

    event_loop(game, buffer, scr)

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
