import curses
import sys
import webbrowser
from utilities import variables as var, menu as m, menu_helpers as mh
from utilities import scripture_helpers as sh
from utilities import list_helpers as lh   
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

    title_str = "Today's Reading"
    
    if var.reading_plan == "pgh":
        option_1 = "1. {}".format(lh.getPGHReading(listNum=1))
        option_2 = "2. {}".format(lh.getPGHReading(listNum=2))
        option_3 = "3. {}".format(lh.getPGHReading(listNum=3))
        option_4 = "4. {}".format(lh.getPGHReading(listNum=4))
        option_5 = "5. {}".format(lh.getPGHReading(listNum=5))
        if var.psalms:
            option_6a = "6. Psalms"
            option_6b = " - {}".format(lh.getPsalms(1))
            option_6c = " - {}".format(lh.getPsalms(2))
            option_6d = " - {}".format(lh.getPsalms(3))
            option_6e = " - {}".format(lh.getPsalms(4))
            option_6f = " - {}".format(lh.getPsalms(5))
        option_6 = "6. {}".format(lh.getPGHReading(listNum=6))
        option_7 = "7. {}".format(lh.getPGHReading(listNum=7))
        option_8 = "8. {}".format(lh.getPGHReading(listNum=8))
        option_9 = "9. {}".format(lh.getPGHReading(listNum=9))
        option_10 = "10. {}".format(lh.getPGHReading(listNum=10))
    while(True):
        stdscr.clear()
        if (cursor_y == 11 and not var.psalms) or (cursor_y == 16 and var.psalms):
            status_msg = "Press Enter to go Back"
        elif cursor_y == 6 and var.psalms:
            status_msg = "'tab to mark all 5 psalms done"
        else:
            status_msg = "'r' to Read | Tab to mark done | 'esc' to go back"
        m.title(stdscr, title_str)
        m.status_bar(stdscr, status_msg)
        m.menu_option(stdscr, option_1, 1, 1, cursor_y)
        m.menu_option(stdscr, option_2, 2, 1, cursor_y)
        m.menu_option(stdscr, option_3, 3, 1, cursor_y)
        m.menu_option(stdscr, option_4, 4, 1, cursor_y)
        m.menu_option(stdscr, option_5, 5, 1, cursor_y)
        if var.psalms:
            m.menu_option(stdscr, option_6a, 6, 1, cursor_y)
            m.menu_option(stdscr, option_6b, 7, 1, cursor_y)
            m.menu_option(stdscr, option_6c, 8, 1, cursor_y)
            m.menu_option(stdscr, option_6d, 9, 1, cursor_y)
            m.menu_option(stdscr, option_6e, 10, 1, cursor_y)
            m.menu_option(stdscr, option_6f, 11, 1, cursor_y)
            m.menu_option(stdscr, option_7, 12, 1, cursor_y)
            m.menu_option(stdscr, option_8, 13, 1, cursor_y)
            m.menu_option(stdscr, option_9, 14, 1, cursor_y)
            m.menu_option(stdscr, option_10, 15, 1, cursor_y)
            m.menu_option(stdscr, "11. Main Menu", 16, 1, cursor_y)
        else:
            m.menu_option(stdscr, option_6, 6, 1, cursor_y)        
            m.menu_option(stdscr, option_7, 7, 1, cursor_y)
            m.menu_option(stdscr, option_8, 8, 1, cursor_y)
            m.menu_option(stdscr, option_9, 9, 1, cursor_y)
            m.menu_option(stdscr, option_10, 10, 1, cursor_y)
            m.menu_option(stdscr, "11. Main Menu", 11, 1, cursor_y)

        stdscr.move(cursor_y, cursor_x)
        stdscr.refresh()
        k = stdscr.getch()
        if k == 27 or k == ord('q'):
            var.reading_position = 1
            mh.back()
        elif k == curses.KEY_UP:
            cursor_y -= 1
            if cursor_y == 0 and var.psalms:
                cursor_y = 16
            elif cursor_y == 0 and not var.psalms:
                cursor_y = 11
            var.reading_position = cursor_y
        elif k == curses.KEY_DOWN:
            cursor_y += 1
            if var.psalms:
                if cursor_y == 17:
                    cursor_y = 1
            else:
                if cursor_y == 12:
                    cursor_y = 1
            var.reading_position = cursor_y
        elif k == 10:
            if (var.psalms and cursor_y == 16) or (not var.psalms and cursor_y == 11):
                var.reading_position = 1
                mh.back()
        elif k == 9: #TODO: add logic
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
            #TODO: add logic for psalms
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
            if not var.psalms:
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
            else:
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
                elif cursor_y == 7:
                    parts = option_6b.split()[1:]
                elif cursor_y == 8:
                    parts = option_6c.split()[1:]
                elif cursor_y == 9:
                    parts = option_6d.split()[1:]
                elif cursor_y == 10:
                    parts = option_6e.split()[1:]
                elif cursor_y == 11:
                    parts = option_6f.split()[1:]
                elif cursor_y == 12:
                    parts = option_7.split()[1:]
                elif cursor_y == 13:
                    parts = option_8.split()[1:]
                elif cursor_y == 14:
                    parts = option_9.split()[1:]
                elif cursor_y == 15:
                    parts = option_10.split()[1:]
                if cursor_y != 16 and cursor_y != 6:
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
            if var.psalms:
                cursor_y = 12
            else:
                cursor_y = 7
            var.reading_position = cursor_y
        elif k == ord('8'):
            if var.psalms:
                cursor_y = 13
            else:
                cursor_y = 8
            var.reading_position = cursor_y
        elif k == ord('9'):
            if var.psalms:
                cursor_y = 14
            else:
                cursor_y = 9
            var.reading_position = cursor_y
        elif k == ord('0'):
            if var.psalms:
                cursor_y = 15
            else:
                cursor_y = 10
            var.reading_position = cursor_y
        elif k == ord('-'):
            if var.psalms:
                cursor_y = 16
            else:
                cursor_y = 11
            var.reading_position = cursor_y
def start():
    curses.wrapper(display)
    