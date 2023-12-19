from displays import main as main_menu 
from utilities import variables as var
from utilities import menu as m
import blessed
if __name__ == "__main__":
    var.init()
    term = blessed.Terminal()
    main_menu.start(term)
    #print("Curses error. Try increasing the size of your terminal window.")