import sys
from utilities import variables as var
from utilities import menu as m
from utilities import arith 
from displays import readings
from displays.settings import home as main_settings
def get_color(term, cursor_y, option):
    if cursor_y == option:
        return term.black_on_white
    else:
        return term.white       
def start(term):
    title_str = "Unquenched Bible"
    status_msg = "Written by Jonathan Thorne | ©2023 | Press 'esc' to quit"
    option_1 = "1. Today's Reading"
    option_2 = "2. Settings (WIP)"
    option_3 = "3. Quit"
    
    with term.cbreak(), term.hidden_cursor():
        print(term.home + term.clear)
        val = ''
        cursor_y = var.main_position
        #m.title_2(term, title_str)
        while True: 
            print(term.home + term.clear)
            print(term.move_xy(arith.title_start(title_str, term.width), 1) + term.cyan + term.bold(title_str))
            print(term.move_xy(1, term.height - 0) + term.black_on_white + term.bold(status_msg))
            print(term.move_xy(1, 1) + get_color(term, cursor_y, 1) + term.bold(option_1))
            print(term.move_xy(1, 2) + get_color(term, cursor_y, 2) + term.bold(option_2))
            print(term.move_xy(1, 3) + get_color(term, cursor_y, 3) + term.bold(option_3))       
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
                print(term.home + term.clear)
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
                    readings.start()
                if cursor_y == 2:
                    main_settings.start()
                if cursor_y == 3:
                    print(term.home + term.clear)
                    sys.exit()
            else:
                print(term.move_xy(1, 4) + term.black_on_white + term.bold("Unknown key: {}".format(val)))
                ip = input("Press enter to continue...")
