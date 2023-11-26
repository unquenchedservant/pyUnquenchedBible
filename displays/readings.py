import curses
import sys
from utilities import variables as var, menu as m
def display(stdscr):
    cursor_y = var.reading_position
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
    if var.reading_plan == "pgh":
        option_1 = "1. Matthew 1"
        option_2 = "2. Genesis 1"
        option_3 = "3. Romans 1"
        option_4 = "4. 1 Thessalonians 1"
        option_5 = "5. Job 1"
        option_6 = "6. Psalm 1"
        option_7 = "7. Proverbs 1"
        option_8 = "8. Joshua 1"
        option_9 = "9. Isaiah 1"
        option_10 = "10. Acts 1"
    while(True):
        stdscr.clear()
        m.title(stdscr, title_str)
        m.status_bar(stdscr, status_msg)
        m.menu_option(stdscr, option_1, 1, 1, cursor_y)
        m.menu_option(stdscr, option_2, 2, 1, cursor_y)
        m.menu_option(stdscr, option_3, 3, 1, cursor_y)
        m.menu_option(stdscr, option_4, 4, 1, cursor_y)
        m.menu_option(stdscr, option_5, 5, 1, cursor_y)
        m.menu_option(stdscr, option_6, 6, 1, cursor_y)
        m.menu_option(stdscr, option_7, 7, 1, cursor_y)
        m.menu_option(stdscr, option_8, 8, 1, cursor_y)
        m.menu_option(stdscr, option_9, 9, 1, cursor_y)
        m.menu_option(stdscr, option_10, 10, 1, cursor_y)

        stdscr.move(cursor_y, cursor_x)
        stdscr.refresh()
        k = stdscr.getch()
        if k == 27 or k == ord('q'):
            sys.exit()
        elif k == curses.KEY_UP:
            cursor_y -= 1
            if cursor_y == 0:
                cursor_y = 10
            var.reading_position = cursor_y
        elif k == curses.KEY_DOWN:
            cursor_y += 1
            if cursor_y == 11:
                cursor_y = 1
            var.reading_position = cursor_y
        elif k == 10:
            print("coming soon")
        elif k == ord('1'):
            cursor_y = 1
            var.reading_position = cursor_y
        elif k == ord('2'):
            cursor_y = 2
            var.reading_position = cursor_y
        elif k == ord('3'):
            cursor_y = 3
            var.reading_position = cursor_y
        elif k == ord('4'):
            cursor_y = 4
            var.reading_position = cursor_y
        elif k == ord('5'):
            cursor_y = 5
            var.reading_position = cursor_y
        elif k == ord('6'):
            cursor_y = 6
            var.reading_position = cursor_y
        elif k == ord('7'):
            cursor_y = 7
            var.reading_position = cursor_y
        elif k == ord('8'):
            cursor_y = 8
            var.reading_position = cursor_y
        elif k == ord('9'):
            cursor_y == 9
            var.reading_position = cursor_y
        elif k == ord('10'):
            cursor_y == 10
            var.reading_position = cursor_y 
def start():
    curses.wrapper(display)
    