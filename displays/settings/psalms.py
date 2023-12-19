import sys
from utilities import variables as var, menu as m, menu_helpers as mh
from utilities import file_helpers as fh
def getSettingChecked(psalms):
    if var.psalms == psalms:
        return "X"
    else:
        return " "
def getIndex(psalms):
    returnValues = {
        True: 1,
        False: 2
    }
    return returnValues[psalms]

def start(term):
    var.menu_type="psalms"
    var.psalms_position = getIndex(var.psalms)
    cursor_y = var.psalms_position
    title_str = "Settings - Read 5 Psalms a Day"
    status_msg = "Press Tab to Select |  Press 'esc' to go back  | Autosaves"
    while True:
        option_1 = "[{}] True".format(getSettingChecked(True))
        option_2 = "[{}] False".format(getSettingChecked(False))
        m.clear(term)
        m.title(term, title_str)
        m.status_bar(term, status_msg)
        m.menu_option(term, option_1, 1, cursor_y)
        m.menu_option(term, option_2, 2, cursor_y)
        m.menu_option(term, "Go Back", 3, cursor_y)
        val = term.inkey()
        if val == 'q' or val.name == "KEY_ESCAPE":
            m.clear(term)
            sys.exit()
        elif val.name == "KEY_UP":
            cursor_y -= 1
            if cursor_y == 0:
                cursor_y = 3
            var.psalms_position = cursor_y
        elif val.name == "KEY_DOWN":
            cursor_y += 1
            if cursor_y == 4:
                cursor_y = 1
            var.psalms_position = cursor_y
        elif val.name == "KEY_TAB":
            if cursor_y == 1:
                var.psalms = True
                fh.savePreferences()
            elif cursor_y == 2:
                var.psalms = False
                fh.savePreferences()
        elif val.name == "KEY_ENTER":
            var.psalms_position = 1
            mh.back(term)
        elif val == '1':
            cursor_y = 1
            var.psalms_position = cursor_y
        elif val == '2':
            cursor_y = 2
            var.psalms_position = cursor_y
        elif val == '3':
            cursor_y = 3
            var.psalms_position = cursor_y    