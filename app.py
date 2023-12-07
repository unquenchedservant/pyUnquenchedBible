from displays import main as main_menu 
from utilities import variables as var
import curses
if __name__ == "__main__":
    var.init()
    try:
        main_menu.start()
    except curses.error:
        print("Curses error. Try increasing the size of your terminal window.")