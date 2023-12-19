import sys
from utilities import variables as var
from utilities import menu as m
from displays import readings
from displays.settings import home as main_settings
    
def start(term):
    title_str = "Unquenched Bible"
    status_msg = "Written by Jonathan Thorne | ©2023 | Press 'esc' to quit"
    option_1 = "1. Today's Reading"
    option_2 = "2. Settings (WIP)"
    option_3 = "3. Quit"
    
    with term.cbreak(), term.hidden_cursor():
        val = ''
        cursor_y = var.main_position
        while True:
            m.clear(term) 
            m.title(term, title_str)
            m.status_bar(term, status_msg)
            m.menu_option(term, option_1, 1, cursor_y)
            m.menu_option(term, option_2, 2, cursor_y)
            m.menu_option(term, option_3, 3, cursor_y)     
            val = term.inkey()
            if val == '1':
                cursor_y = 1
                var.main_position = cursor_y
            elif val == '2':
                cursor_y = 2
                var.main_position = cursor_y
            elif val == '3':
                cursor_y = 3
                var.main_position = cursor_y
            elif val == 'q' or val.name == "KEY_ESCAPE":
                m.clear(term)
                sys.exit()
            elif val.name == "KEY_UP":
                cursor_y -= 1
                if cursor_y == 0:
                    cursor_y = 3
                var.main_position = cursor_y
            elif val.name == "KEY_DOWN":
                cursor_y += 1
                if cursor_y == 4:
                    cursor_y = 1
                var.main_position = cursor_y
            elif val.name == "KEY_ENTER":
                if cursor_y == 1:
                    readings.start(term)
                if cursor_y == 2:
                    main_settings.start(term)
                if cursor_y == 3:
                    m.clear()
                    sys.exit()
            else:
                print(term.move_xy(1, 4) + term.black_on_white + term.bold("Unknown key: {}".format(val)))
                ip = input("Press enter to continue...")
