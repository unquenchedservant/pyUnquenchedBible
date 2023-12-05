import curses
import sys
import webbrowser
from utilities import variables as var, menu as m, menu_helpers as mh
from utilities import scripture_helpers as sh
def display(stdscr):
    var.menu_type="readings"
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
    status_msg = "Press 'r' to Read | Press 'd' to Mark Done |  Press 'esc' to go back"
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
        option_11 = "11. Main Menu"
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
        m.menu_option(stdscr, option_11, 11, 1, cursor_y)

        stdscr.move(cursor_y, cursor_x)
        stdscr.refresh()
        k = stdscr.getch()
        if k == 27 or k == ord('q'):
            var.reading_position = 1
            mh.back()
        elif k == curses.KEY_UP:
            cursor_y -= 1
            if cursor_y == 0:
                cursor_y = 11
            var.reading_position = cursor_y
        elif k == curses.KEY_DOWN:
            cursor_y += 1
            if cursor_y == 12:
                cursor_y = 1
            var.reading_position = cursor_y
        elif k == 10 and cursor_y == 11:
            var.reading_position = 1
            mh.back()
        elif k == ord('d'):
            if cursor_y == 1:
                print("Cursor position 1")
            elif cursor_y == 2:
                print("Cursor position 2")
            elif cursor_y == 3:
                print("Cursor position 3")
            elif cursor_y == 4:
                print("Cursor position 4")
            elif cursor_y == 5:
                print("cursor position 5")
            elif cursor_y == 6:
                print("Cursor position 6")
            elif cursor_y == 7:
                print("Cursor position 7")
            elif cursor_y == 8:
                print("Cursor position 8")
            elif cursor_y == 9:
                print("Cursor position 9")
            elif cursor_y == 10:
                print("cursor position 10")
        elif k == ord('r'):
            parts = []
            if cursor_y == 1:
                parts = option_1.split()[1:]
            elif cursor_y == 2:
                parts = option_2.split()[1:]
            elif cursor_y == 3:
                parts = option_3.split()[1:]
            elif cursor_y == 4:
                parts = option_4.split()[1:]
            elif cursor_y == 5:
                parts = option_5.split()[1:]
            elif cursor_y == 6:
                parts = option_6.split()[1:]
            elif cursor_y == 7:
                parts = option_7.split()[1:]
            elif cursor_y == 8:
                parts = option_8.split()[1:]
            elif cursor_y == 9:
                parts = option_9.split()[1:]
            elif cursor_y == 10:
                parts = option_10.split()[1:]
            if cursor_y != 11:
                if var.preferred_bible == "bible_gateway":
                    sh.openBibleGateway(parts)
                elif var.preferred_bible == "logos":
                    sh.openLogos(parts)
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
def start():
    curses.wrapper(display)
    