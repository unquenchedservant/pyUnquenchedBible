import curses
import sys
import webbrowser
from utilities import variables as var, menu as m, menu_helpers as mh
from utilities import file_helpers as fh
def getSettingChecked(version):
    if var.preferred_bible == version:
        return "X"
    else:
        return " "
def getIndex(preferred_bible):
    returnValues = {
        "bible_gateway": 1,
        "logos": 2
    }
    return returnValues[preferred_bible]
def display(stdscr):
    var.menu_type="pref_bible"
    var.pref_bible_position = getIndex(var.preferred_bible)
    cursor_y = var.pref_bible_position
    cursor_x = 1
    last_pressed = "None"
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
    status_msg = "Press Tab to Select |  Press 'esc' to go back  | Autosaves"
    
    while(True):
        option_1 = "[{}] Bible Gateway".format(getSettingChecked("bible_gateway"))
        option_2 = "[{}] Logos".format(getSettingChecked("logos"))
        stdscr.clear()
        m.title(stdscr, title_str)
        m.status_bar(stdscr, status_msg)
        m.menu_option(stdscr, option_1, 1, 1, cursor_y)
        m.menu_option(stdscr, option_2, 2, 1, cursor_y)
        m.menu_option(stdscr, "Go Back", 3, 1, cursor_y)
        stdscr.move(cursor_y, cursor_x)
        stdscr.refresh()
        k = stdscr.getch()
        last_pressed = k
        if k == 27 or k == ord('q'):
            var.pref_bible_position = 1
            mh.back()
        elif k == curses.KEY_UP:
            cursor_y -= 1
            if cursor_y == 0:
                cursor_y = 3
            var.reading_position = cursor_y
        elif k == curses.KEY_DOWN:
            cursor_y += 1
            if cursor_y == 4:
                cursor_y = 1
            var.reading_position = cursor_y
        elif k == 9:
            if cursor_y == 1:
                var.preferred_bible = "bible_gateway"
                fh.savePreferences()
            elif cursor_y == 2:
                var.preferred_bible = "logos"
                fh.savePreferences()
        elif k == 10:
            var.pref_bible_position = 1
            mh.back()
        elif k == ord('1'):
            cursor_y = 1
            var.pref_bible_position = cursor_y
        elif k == ord('2'):
            cursor_y = 2
            var.pref_bible_position = cursor_y
        elif k == ord('3'):
            cursor_y = 3
            var.pref_bible_position = cursor_y
def start():
    curses.wrapper(display)
    