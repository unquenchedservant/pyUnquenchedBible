import curses
from utilities import arith, menu_helpers

def get_height(stdscr):
    return stdscr.getmaxyx()[0]
def get_width(stdscr):
    return stdscr.getmaxyx()[1]

def get_sort_1(sort_int):
    if sort_int == 1:
        sort_int = 3
    elif sort_int == 2:
        sort_int = 4
    elif sort_int == 3:
        sort_int = 1
    elif sort_int == 4:
        sort_int = 2
    return sort_int
def get_sort_2(sort_int):
    if sort_int == 1:
        sort_int = 2
    elif sort_int == 2:
        sort_int = 1
    elif sort_int == 3:
        sort_int = 4
    elif sort_int == 4:
        sort_int = 3
    return sort_int

"""
Adds the title to the screen. Purpose is to make other files look nicer

Paramaters:
stdscr  - curses screen
title   - title of the current screen
"""
# I want to convert this to use blessed instead of curses
def clear(term):
    print(term.home + term.clear)

def title(term, title):
    display_x = arith.title_start(title, term.width)
    print(term.move_xy(display_x, 1) + term.cyan + term.bold(title))

def status_bar(term, status_msg):
    magic_number = (term.width - len(status_msg))
    status_msg = status_msg + " " * magic_number
    print(term.move_xy(0, term.height - 0) + term.black_on_white + term.bold(status_msg))


def last_row(stdscr, l_row):
    height = get_height(stdscr)
    stdscr.addstr(height - 3, 1, l_row)

"""
highlights where the cursor_y position is for login screen

Paramaters:
stdscr    - curses screen
string    - the string to display
display_y - where to display the string on the screen (vertically)
display_x - where to display the string on the screen (horizontally)
cursor_y  - where is the cursor_y currently
"""
def get_color(term, cursor_y, option):
    if cursor_y == option:
        return term.black_on_white
    else:
        return term.white

def menu_option(term, string, display_y, cursor_y):
    print(term.move_xy(1, display_y) + get_color(term, cursor_y, display_y) + term.bold(string))


def display_option(stdscr, y_position, x_start_pos, cursor_y, max_rows, num_pages, current_page, last_page_row, display_list):
    width = get_width(stdscr)
    index = arith.get_index(max_rows, num_pages, current_page, y_position, last_page_row)
    pre_display = display_list[index]
    display = menu_helpers.get_display_row(pre_display, width)
    menu_option(stdscr, display, y_position, x_start_pos, cursor_y)

def add_string(stdscr, string, display_y, display_x):
    stdscr.addstr(display_y, display_x, string)