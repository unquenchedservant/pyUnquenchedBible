from utilities import variables as var
from displays import main
from displays.settings import home as main_settings
"""
gets the title for the menu based on menu_type (authors, ) and sort_int(1-4 or 1 if not sortable)
"""
def get_title(sort_int):
    if var.menu_type == "authors":
        if sort_int == 1:
            return  "JETS Author Listing - Sorted by Last (A-Z)"
        elif sort_int == 2:
            return "JETS Author Listing - Sorted by Last (Z-A)"
        elif sort_int == 3:
            return "JETS Author Listing - Sorted by First (A-Z)"
        elif sort_int == 4:
            return "JETS Author Listing - Sorted by First (Z-A)"
    elif var.menu_type == "volume":
        return "JETS by Volume (Year)"
    elif var.menu_type == "issue":
        return "Volume {} ({})".format(var.volume_number, var.volume_year)
    elif var.menu_type == "articles":
        if var.issue_number == "All":
            return "Volume {} ({}) - All Issues".format(var.volume_number, var.volume_year)
        else:
            return "Volume {} ({}) - Issue {}".format(var.volume_number, var.volume_year, var.issue_number)
    elif var.menu_type == "author_articles":
        return "Articles by {}".format(var.author_name)

#def get_display_row(display, width):
#    if var.menu_type == "authors":
#        return sort_dict.get_name(display)
#    elif var.menu_type == "volume":
#        display_number = string_handler.display_number(str(display))
#        display = string_handler.display_volume(display_number, str(display))
#        return display
#    elif var.menu_type == "issue":
#        number = str(display)
#        return "Vol {} ({}) - Issue {}".format(var.volume_number, var.volume_year, number)
#    elif var.menu_type == "articles" or var.menu_type == "author_articles":
#        return string_handler.display_string(display, width, var.menu_type)


def back():
    if var.menu_type == "readings" or var.menu_type == "settings":
        main.start()
    if var.menu_type == "pref_bible" or var.menu_type == "bible_version" or var.menu_type == "psalms":
        main_settings.start()
'''
def get_status_bar(current_page, num_pages, sort_int):
    menuStr1 = "'m' : Main Menu"
    menuStr2 = "'m'/esc : Main Menu"
    menuStr3 = "esc : Main Menu"
    nextStr = "'n' : Next"
    prevStr = "'p' : Previous"
    openStr = "'o' : Open"
    infoStr =  "'i' : Info"
    issueStr = "esc : Issue Selection"
    volStr1 = "'v' : Volume Selection"
    volStr2 = "'p'/'v'/esc : Volume Selection"
    arrowStr = "arrow keys : Navigation"
    alphaStr = "(a-z) : Go to Letter"
    authorStr = "'a'/esc : Back to Author"
    if var.menu_type == "authors":
        current = "Last"
        cur2 = "Z-A"
        if sort_int == 1:
            current = "First"
            cur2 = "Z-A"
        elif sort_int == 2:
            current = "First"
            cur2 = "A-Z"
        elif sort_int == 3:
            current = "Last"
            cur2 = "Z-A"
        elif sort_int == 4:
            current = "Last"
            cur2 = "A-Z"
        return " {} | {} | {} | 1: Sort by {} | 2: Sort ({})".format(menuStr3, arrowStr, alphaStr, current, cur2)
    elif var.menu_type == "volume":
        if current_page == 1:
            return " {} | {}".format(nextStr, menuStr2)
        elif current_page == num_pages:
            return " {} | {}".format(prevStr, menuStr2)
        else:
            return " {} | {} | {}".format(nextStr, prevStr, menuStr2)

    elif var.menu_type == "issue":
        return " {} | {} ".format(volStr2, menuStr1)
    elif var.menu_type == "articles":
        if num_pages == 1:
            return " {} | {} | {} | {} | {}".format(openStr, infoStr, issueStr, volStr1, menuStr1)
        elif current_page == 1 and not num_pages == 1:
            return " {} | {} | {} | {} | {} | {}".format(nextStr, openStr, infoStr, issueStr, volStr1, menuStr1)
        elif current_page == num_pages and not num_pages == 1:
            return " {} | {} | {} | {} | {} | {}".format(prevStr, openStr, infoStr, issueStr, volStr1, menuStr1)
        else:
            return " {} | {} | {} | {} | {} | {} | {}".format(nextStr, prevStr, openStr, infoStr, issueStr, volStr1, menuStr1)
    elif var.menu_type == "author_articles":
        if num_pages == 1:
            return " {} | {} | {} | {}".format(openStr, infoStr, authorStr, menuStr1)
        if current_page == 1 and not num_pages == 1:
            return " {} | {} | {} | {} | {}".format(nextStr, openStr, infoStr, authorStr, menuStr1)
        elif current_page == num_pages:
            return " {} | {} | {} | {} | {}".format(prevStr, openStr, infoStr, authorStr, menuStr1)
        else:
            return " {} | {} | {} | {} | {} | {}".format(nextStr, prevStr, openStr, infoStr, authorStr, menuStr1)
            '''