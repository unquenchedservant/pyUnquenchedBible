import sys
from utilities import variables as var, menu as m, menu_helpers as mh
from utilities import scripture_helpers as sh
from utilities import list_helpers as lh

def getReadingDone(list):
    listDone = False
    if list == 1:
        listDone = var.pgh_list_1_done
    elif list == 2:
        listDone = var.pgh_list_2_done
    elif list == 3:
        listDone = var.pgh_list_3_done
    elif list == 4:
        listDone = var.pgh_list_4_done
    elif list == 5:
        listDone = var.pgh_list_5_done
    elif list == 6:
        listDone = var.pgh_list_6_done
    elif list == 7:
        listDone = var.pgh_list_7_done
    elif list == 8:
        listDone = var.pgh_list_8_done
    elif list == 9:
        listDone = var.pgh_list_9_done
    elif list == 10:
        listDone = var.pgh_list_10_done
    if listDone:
        return "X"
    else:
        return " "
def start(term):
    var.menu_type="readings"
    cursor_y = var.reading_position
    title_str = "Today's Reading"
    status_msg = "Enter to go to reading | Press 'esc' to go back"
    if var.reading_plan == "pgh":
        option_1 = "1.  [{}] {}".format(getReadingDone(1), lh.getPGHReading(listNum=1))
        option_2 = "2.  [{}] {}".format(getReadingDone(2), lh.getPGHReading(listNum=2))
        option_3 = "3.  [{}] {}".format(getReadingDone(3), lh.getPGHReading(listNum=3))
        option_4 = "4.  [{}] {}".format(getReadingDone(4), lh.getPGHReading(listNum=4))
        option_5 = "5.  [{}] {}".format(getReadingDone(5), lh.getPGHReading(listNum=5))
        if var.psalms:
            option_6a = "6. [{}] Psalms".format(getReadingDone(6))
            option_6b = "        - {}".format(lh.getPsalms(1))
            option_6c = "        - {}".format(lh.getPsalms(2))
            option_6d = "        - {}".format(lh.getPsalms(3))
            option_6e = "        - {}".format(lh.getPsalms(4))
            option_6f = "        - {}".format(lh.getPsalms(5))
        option_6 = "6.  [{}] {}".format(getReadingDone(6), lh.getPGHReading(listNum=6))
        option_7 = "7.  [{}] {}".format(getReadingDone(7), lh.getPGHReading(listNum=7))
        option_8 = "8.  [{}] {}".format(getReadingDone(8), lh.getPGHReading(listNum=8))
        option_9 = "9.  [{}] {}".format(getReadingDone(9), lh.getPGHReading(listNum=9))
        option_10 = "10. [{}] {}".format(getReadingDone(10), lh.getPGHReading(listNum=10))
    while(True):
        m.clear(term)
        if (cursor_y == 11 and not var.psalms) or (cursor_y == 16 and var.psalms):
            status_msg = "Press Enter to go Back"
        elif cursor_y == 6 and var.psalms:
            status_msg = "'tab' to mark all 5 Psalms done"
        elif var.psalms and (cursor_y >=7 and cursor_y <= 11):
            status_msg = "'r' to Read | 'esc' to go back"
        else:
            status_msg = "'r' to Read | Tab to mark done | 'esc' to go back"
        m.title(term, title_str)
        m.status_bar(term, status_msg)
        m.menu_option(term, option_1, 1, cursor_y)
        m.menu_option(term, option_2, 2, cursor_y)
        m.menu_option(term, option_3, 3, cursor_y)
        m.menu_option(term, option_4, 4, cursor_y)
        m.menu_option(term, option_5, 5, cursor_y)
        if var.psalms:
            m.menu_option(term, option_6a, 6, cursor_y)
            m.menu_option(term, option_6b, 7, cursor_y)
            m.menu_option(term, option_6c, 8, cursor_y)
            m.menu_option(term, option_6d, 9, cursor_y)
            m.menu_option(term, option_6e, 10, cursor_y)
            m.menu_option(term, option_6f, 11, cursor_y)
            m.menu_option(term, option_7, 12, cursor_y)
            m.menu_option(term, option_8, 13, cursor_y)
            m.menu_option(term, option_9, 14, cursor_y)
            m.menu_option(term, option_10, 15, cursor_y)
            m.menu_option(term, "11. Main Menu", 16, cursor_y)
        else:
            m.menu_option(term, option_6, 6, cursor_y)        
            m.menu_option(term, option_7, 7, cursor_y)
            m.menu_option(term, option_8, 8, cursor_y)
            m.menu_option(term, option_9, 9, cursor_y)
            m.menu_option(term, option_10, 10, cursor_y)
            m.menu_option(term, "11. Main Menu", 11, cursor_y)
        val = term.inkey()
        if val == 'q' or val.name == "KEY_ESCAPE":
            m.clear()
            sys.exit()
        elif val.name == "KEY_UP":
            cursor_y -= 1
            if cursor_y == 0 and var.psalms:
                cursor_y = 16
            elif cursor_y == 0 and not var.psalms:
                cursor_y = 11
            var.reading_position = cursor_y
        elif val.name == "KEY_DOWN":
            cursor_y += 1
            if var.psalms:
                if cursor_y == 17:
                    cursor_y = 1
            else:
                if cursor_y == 12:
                    cursor_y = 1
            var.reading_position = cursor_y
        elif val.name == "KEY_ENTER":
            if (var.psalms and cursor_y == 16) or (not var.psalms and cursor_y == 11):
                var.reading_position = 1
                mh.back(term)
        elif val.name == "KEY_TAB":
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
            #TODO: add logic for psalms #jk this should be easy now
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
        elif val == 'r':
            parts = []
            if not var.psalms:
                if cursor_y == 1:
                    parts = option_1.split()[3:]
                elif cursor_y == 2:
                    parts = option_2.split()[3:]
                elif cursor_y == 3:
                    parts = option_3.split()[3:]
                elif cursor_y == 4:
                    parts = option_4.split()[3:]
                elif cursor_y == 5:
                    parts = option_5.split()[3:]
                elif cursor_y == 6:
                    parts = option_6.split()[3:]
                elif cursor_y == 7:
                    parts = option_7.split()[3:]
                elif cursor_y == 8:
                    parts = option_8.split()[3:]
                elif cursor_y == 9:
                    parts = option_9.split()[3:]
                elif cursor_y == 10:
                    parts = option_10.split()[3:]
                if cursor_y != 11:
                    if var.preferred_bible == "bible_gateway":
                        sh.openBibleGateway(parts)
                    elif var.preferred_bible == "logos":
                        sh.openLogos(parts)
            else:
                if cursor_y == 1:
                    parts = option_1.split()[3:]
                elif cursor_y == 2:
                    parts = option_2.split()[3:]
                elif cursor_y == 3:
                    parts = option_3.split()[3:]
                elif cursor_y == 4:
                    parts = option_4.split()[3:]
                elif cursor_y == 5:
                    parts = option_5.split()[3:]
                elif cursor_y == 7:
                    parts = option_6b.split()[3:]
                elif cursor_y == 8:
                    parts = option_6c.split()[3:]
                elif cursor_y == 9:
                    parts = option_6d.split()[3:]
                elif cursor_y == 10:
                    parts = option_6e.split()[3:]
                elif cursor_y == 11:
                    parts = option_6f.split()[3:]
                elif cursor_y == 12:
                    parts = option_7.split()[3:]
                elif cursor_y == 13:
                    parts = option_8.split()[3:]
                elif cursor_y == 14:
                    parts = option_9.split()[3:]
                elif cursor_y == 15:
                    parts = option_10.split()[3:]
                if cursor_y != 16 and cursor_y != 6:
                    if var.preferred_bible == "bible_gateway":
                        sh.openBibleGateway(parts)
                    elif var.preferred_bible == "logos":
                        sh.openLogos(parts)
        elif val == '1':
            cursor_y = 1
            var.reading_position = cursor_y
        elif val == '2':
            cursor_y = 2
            var.reading_position = cursor_y
        elif val == '3':
            cursor_y = 3
            var.reading_position = cursor_y
        elif val == '4':
            cursor_y = 4
            var.reading_position = cursor_y
        elif val == '5':
            cursor_y = 5
            var.reading_position = cursor_y
        elif val == '6':
            cursor_y = 6
            var.reading_position = cursor_y
        elif val == '7':
            if var.psalms:
                cursor_y = 12
            else:
                cursor_y = 7
            var.reading_position = cursor_y
        elif val == '8':
            if var.psalms:
                cursor_y = 13
            else:
                cursor_y = 8
            var.reading_position = cursor_y
        elif val == '9':
            if var.psalms:
                cursor_y = 14
            else:
                cursor_y = 9
            var.reading_position = cursor_y
        elif val == '0':
            if var.psalms:
                cursor_y = 15
            else:
                cursor_y = 10
            var.reading_position = cursor_y
        elif val == '-':
            if var.psalms:
                cursor_y = 16
            else:
                cursor_y = 11
            var.reading_position = cursor_y
    #curses.wrapper(display)
    