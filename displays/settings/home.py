import curses
import sys
import webbrowser
from utilities import variables as var, menu as m, menu_helpers as mh
from displays.settings import pref_bible
from displays.settings import bible_versions
    
def getPreferredBible(version):
    if version == "bible_gateway":
        return "Bible Gateway"
    elif version == "logos":
        return "Logos Bible Software"
    else:
        return "Unknown"
def display(stdscr):
    var.menu_type="settings"
    cursor_y = var.settings_position
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
    status_msg = "Enter to change settings |  Press 'esc' to go back"
    option_1 = "Preferred Bible (Current: {})".format(getPreferredBible(var.preferred_bible))
    option_2 = "Bible Version (Logos Only) (Current: {})".format(var.bible_version)
    while(True):
        stdscr.clear()
        m.title(stdscr, title_str)
        m.status_bar(stdscr, status_msg)
        m.menu_option(stdscr, option_1, 1, 1, cursor_y)
        m.menu_option(stdscr, option_2, 2, 1, cursor_y)
        m.menu_option(stdscr, "Go back", 3, 1, cursor_y)
        stdscr.move(cursor_y, cursor_x)
        stdscr.refresh()
        k = stdscr.getch()
        if k == 27 or k == ord('q'):
            mh.back()
        elif k == curses.KEY_UP:
            cursor_y -= 1
            if cursor_y == 0:
                cursor_y = 2
            var.settings_position = cursor_y
        elif k == curses.KEY_DOWN:
            cursor_y += 1
            if cursor_y == 3:
                cursor_y = 1
            var.settings_position = cursor_y
        elif k == 10 and cursor_y == 3:
            mh.back()
        elif k == 10:
            if cursor_y == 1:
                pref_bible.start()
            elif cursor_y == 2:
                bible_versions.start()
        elif k == ord('d'):
            if cursor_y == 1:
                print("Cursor position 1")
        elif k == ord('1'):
            cursor_y = 1
            var.settings_position = cursor_y
        elif k == ord('2'):
            cursor_y = 1
            var.settings_position = cursor_y
def start():
    curses.wrapper(display)
    