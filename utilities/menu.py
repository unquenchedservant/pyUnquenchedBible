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
def title(stdscr, title):
    display_x = arith.title_start(title, stdscr.getmaxyx()[1])
    stdscr.attron(curses.color_pair(1))
    stdscr.attron(curses.A_BOLD)
    stdscr.addstr(0, display_x, title)
    stdscr.attroff(curses.A_BOLD)
    stdscr.attroff(curses.color_pair(1))

def status_bar(stdscr, status_msg):
    height = get_height(stdscr)
    width = get_width(stdscr)
    display_y = height - 1
    magic_number = (width - len(status_msg) - 1)

    stdscr.attron(curses.color_pair(3))
    stdscr.addstr(display_y, 0, status_msg)
    stdscr.addstr(display_y, len(status_msg), " " * magic_number)
    stdscr.attroff(curses.color_pair(3))

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

def menu_option(stdscr, string, display_y, display_x, cursor_y):
    if cursor_y == display_y:
        stdscr.attron(curses.color_pair(3))
    stdscr.addstr(display_y, display_x, string)
    if cursor_y == display_y:
        stdscr.attroff(curses.color_pair(3))

def display_option(stdscr, y_position, x_start_pos, cursor_y, max_rows, num_pages, current_page, last_page_row, display_list):
    width = get_width(stdscr)
    index = arith.get_index(max_rows, num_pages, current_page, y_position, last_page_row)
    pre_display = display_list[index]
    display = menu_helpers.get_display_row(pre_display, width)
    menu_option(stdscr, display, y_position, x_start_pos, cursor_y)

def add_string(stdscr, string, display_y, display_x):
    stdscr.addstr(display_y, display_x, string)