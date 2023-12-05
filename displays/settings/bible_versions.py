import curses
import sys
import webbrowser
from utilities import variables as var, menu as m, menu_helpers as mh
from utilities import file_helpers as fh
def getSettingChecked(version):
    if var.bible_version == version:
        return "X"
    else:
        return " "
def getIndex(version):
    returnValues = {
        "ESV": 1,
        "NIV": 2,
        "KJV": 3,
        "CSB": 4,
        "NASB": 5,
        "NASB2020": 6,
        "NKJV": 7,
        "NLT": 8,
        "NET": 9,
        "MSG": 10,
        "LEB": 11,
        "NRSV": 12,
        "RSV": 13,
        "PASSION": 14,
        "ASV": 15
    }
    return returnValues[version]
    
def display(stdscr):
    var.menu_type="bible_version"
    var.bible_version_position = getIndex(var.bible_version)
    cursor_y = var.bible_version_position
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
    
    option_15 = "Save and Go back"
    while(True):
        option_1 = "[{}] ESV".format(getSettingChecked("ESV"))
        option_2 = "[{}] NIV".format(getSettingChecked("NIV"))
        option_3 = "[{}] KJV".format(getSettingChecked("KJV"))
        option_4 = "[{}] CSB".format(getSettingChecked("CSB"))
        option_5 = "[{}] NASB1995".format(getSettingChecked("NASB"))
        option_6 = "[{}] NASB2020".format(getSettingChecked("NASB2020"))
        option_7 = "[{}] NKJV".format(getSettingChecked("NKJV"))
        option_8 = "[{}] NLT".format(getSettingChecked("NLT"))
        option_9 = "[{}] NET".format(getSettingChecked("NET"))
        option_10 = "[{}] MSG".format(getSettingChecked("MSG"))
        option_11 = "[{}] LEB".format(getSettingChecked("LEB"))
        #option_11 = "[{}] AMP".format(getSettingChecked("AMP"))
        option_12 = "[{}] NRSV".format(getSettingChecked("NRSV"))
        option_13 = "[{}] RSV".format(getSettingChecked("RSV"))
        option_14 = "[{}] Passion".format(getSettingChecked("PASSION"))
        #option_13 = "[{}] NCV".format(getSettingChecked("NCV"))
        #option_14 = "[{}] GW".format(getSettingChecked("GW"))
        option_15 = "[{}] ASV".format(getSettingChecked("ASV"))
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
        m.menu_option(stdscr, option_12, 12, 1, cursor_y)
        m.menu_option(stdscr, option_13, 13, 1, cursor_y)
        m.menu_option(stdscr, option_14, 14, 1, cursor_y)
        m.menu_option(stdscr, option_15, 15, 1, cursor_y)
        m.menu_option(stdscr, "Go Back", 16, 1, cursor_y)
        stdscr.move(cursor_y, cursor_x)
        stdscr.refresh()
        k = stdscr.getch()
        last_pressed = k
        if k == 27 or k == ord('q'):
            var.bible_version_position = 1
            mh.back()
        elif k == curses.KEY_UP:
            cursor_y -= 1
            if cursor_y == 0:
                cursor_y = 16
            var.reading_position = cursor_y
        elif k == curses.KEY_DOWN:
            cursor_y += 1
            if cursor_y == 17:
                cursor_y = 1
            var.reading_position = cursor_y
        elif k == 9:
            if cursor_y == 1:
                var.bible_version = "ESV"
                fh.savePreferences()    
            elif cursor_y == 2:
                var.bible_version = "NIV"
                fh.savePreferences()
            elif cursor_y == 3:
                var.bible_version = "KJV"
                fh.savePreferences()
            elif cursor_y == 4:
                var.bible_version = "CSB"
                fh.savePreferences()
            elif cursor_y == 5:
                var.bible_version = "NASB"
                fh.savePreferences()
            elif cursor_y == 6:
                var.bible_version = "NASB2020"
                fh.savePreferences()
            elif cursor_y == 7:
                var.bible_version = "NKJV"
                fh.savePreferences()
            elif cursor_y == 8:
                var.bible_version = "NLT"
                fh.savePreferences()
            elif cursor_y == 9:
                var.bible_version = "NET"
                fh.savePreferences()
            elif cursor_y == 10:
                var.bible_version = "MSG"
                fh.savePreferences()
            elif cursor_y == 11:
                var.bible_version = "LEB"
                fh.savePreferences()
            elif cursor_y == 12:
                var.bible_version = "NRSV"
                fh.savePreferences()
            elif cursor_y == 13:
                var.bible_version = "RSV"
                fh.savePreferences()
            elif cursor_y == 14:
                var.bible_version = "PASSION"
                fh.savePreferences()
            elif cursor_y == 15:
                var.bible_version = "ASV"
                fh.savePreferences()
        elif k == 10:
            var.bible_version_position = 1
            mh.back()
        elif k == ord('1'):
            cursor_y = 1
            var.bible_version_position = cursor_y
        elif k == ord('2'):
            cursor_y = 2
            var.bible_version_position = cursor_y
        elif k == ord('3'):
            cursor_y = 3
            var.bible_version_position = cursor_y
        elif k == ord('4'):
            cursor_y = 4
            var.bible_version_position = cursor_y
        elif k == ord('5'):
            cursor_y = 5
            var.bible_version_position = cursor_y
        elif k == ord('6'):
            cursor_y = 6
            var.bible_version_position = cursor_y
        elif k == ord('7'):
            cursor_y = 7
            var.bible_version_position = cursor_y
        elif k == ord('8'):
            cursor_y = 8
            var.bible_version_position = cursor_y
        elif k == ord('9'):
            cursor_y = 9
            var.bible_version_position = cursor_y
def start():
    curses.wrapper(display)
    