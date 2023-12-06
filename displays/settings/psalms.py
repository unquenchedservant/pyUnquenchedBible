import curses
import sys
import webbrowser
from utilities import variables as var, menu as m, menu_helpers as mh
from utilities import file_helpers as fh
def getSettingChecked(psalms):
    if var.psalms == psalms:
        return "X"
    else:
        return " "
def getIndex(psalms):
    returnValues = {
        True: 1,
        False: 2
    }
    return returnValues[psalms]
def display(stdscr):
    var.menu_type="psalms"
    var.psalms_position = getIndex(var.psalms)
    cursor_y = var.psalms_position
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

        option_1 = "[{}] True".format(getSettingChecked(True))
        option_2 = "[{}] False".format(getSettingChecked(False))
        stdscr.clear()
        m.title(stdscr, title_str)
        m.status_bar(stdscr, status_msg)
        m.menu_option(stdscr, "Read 5 Psalms a Day:", 1, 1, cursor_y)
        m.menu_option(stdscr, option_1, 2, 1, cursor_y)
        m.menu_option(stdscr, option_2, 3, 1, cursor_y)
        m.menu_option(stdscr, "Go Back", 4, 1, cursor_y)
        stdscr.move(cursor_y, cursor_x)
        stdscr.refresh()
        k = stdscr.getch()
        last_pressed = k
        if k == 27 or k == ord('q'):
            var.psalms_position = 1
            mh.back()
        elif k == curses.KEY_UP:
            cursor_y -= 1
            if cursor_y == 1:
                cursor_y = 3
            var.psalms_position = cursor_y
        elif k == curses.KEY_DOWN:
            cursor_y += 1
            if cursor_y == 4:
                cursor_y = 2
            var.psalms_position = cursor_y
        elif k == 9:
            if cursor_y == 2:
                var.psalms = True
                fh.savePreferences()
            elif cursor_y == 3:
                var.psalms = False
                fh.savePreferences()
        elif k == 10:
            var.psalms_position = 1
            mh.back()
def start():
    curses.wrapper(display)
    