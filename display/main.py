import curses
import sys
from utilities import variables as var, menu as m
def main_menu(stdscr):
    cursor_y = var.main_position
    cursor_x = 1
    k = 0

    curses.curs_set(0)

    stdscr.clear()
    stdscr.refresh()

    height, width = stdscr.getmaxyx()

    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)

    title_str = "Unquenched Bible"
    status_msg = "Written by Jonathan Thorne | ©2023 | Press 'esc' to quit"
    option_1 = "1. Coming Soon"
    option_2 = "2. Coming Soon"
    option_3 = "3. Coming Soon"
    option_4 = "4. Quit"

    while(True):
        stdscr.clear()
        m.title(stdscr, title_str)
        m.status_bar(stdscr, status_msg)
        m.menu_option(stdscr, option_1, 1, 1, cursor_y)
        m.menu_option(stdscr, option_2, 2, 1, cursor_y)
        m.menu_option(stdscr, option_3, 3, 1, cursor_y)
        m.menu_option(stdscr, option_4, 4, 1, cursor_y)

        stdscr.move(cursor_y, cursor_x)
        stdscr.refresh()
        k = stdscr.getch()
        if k == 27 or k == ord('q'):
            sys.exit()
        elif k == curses.KEY_UP:
            cursor_y -= 1
            if cursor_y == 0:
                cursor_y = 4
            var.main_position = cursor_y
        elif k == curses.KEY_DOWN:
            cursor_y += 1
            if cursor_y == 5:
                cursor_y = 1
            var.main_position = cursor_y
        #TODO: add options for key right
        elif k == 10:
            char = int.from_bytes(stdscr.instr(cursor_y, 1, 1), byteorder='little')
            if char == ord('4'):
                sys.exit()
        elif k == ord('1'):
            cursor_y = 1
            var.main_position = cursor_y
        elif k == ord('2'):
            cursor_y = 2
            var.main_position = cursor_y
        elif k == ord('3'):
            cursor_y = 3
            var.main_position = cursor_y
        elif k == ord('4'):
            cursor_y = 4
            var.main_position = cursor_y
        
def start():
    curses.wrapper(main_menu)