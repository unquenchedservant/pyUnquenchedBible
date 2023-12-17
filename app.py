from displays import main as main_menu 
from utilities import variables as var
from utilities import menu as m
import curses
from blessed import Terminal
if __name__ == "__main__":
    var.init()
    try:
        term = Terminal
        m.title_2(term, "Unquenched Bible")
        print(term.home + term.clear)
    except curses.error:
        print("Curses error. Try increasing the size of your terminal window.")