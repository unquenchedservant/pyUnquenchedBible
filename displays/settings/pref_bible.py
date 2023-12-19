import sys
from utilities import variables as var, menu as m, menu_helpers as mh
from utilities import file_helpers as fh
def getSettingChecked(version):
    if var.preferred_bible == version:
        return "X"
    else:
        return " "
def getIndex(preferred_bible):
    returnValues = {
        "bible_gateway": 1,
        "logos": 2
    }
    return returnValues[preferred_bible]
def start(term):
    var.menu_type="pref_bible"
    var.pref_bible_position = getIndex(var.preferred_bible)
    cursor_y = var.pref_bible_position
    title_str = "Settings - Preferred Bible"
    status_msg = "Press Tab to Select |  Press 'esc' to go back  | Autosaves"
    while True:
        m.clear(term)
        option_1 = "[{}] Bible Gateway".format(getSettingChecked("bible_gateway"))
        option_2 = "[{}] Logos".format(getSettingChecked("logos"))
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
            var.pref_bible_position = cursor_y
        elif val.name == "KEY_DOWN":
            cursor_y += 1
            if cursor_y == 4:
                cursor_y = 1
            var.pref_bible_position = cursor_y
        elif val.name == "KEY_TAB":
            if cursor_y == 1:
                var.preferred_bible = "bible_gateway"
                fh.savePreferences()
            elif cursor_y == 2:
                var.preferred_bible = "logos"
                fh.savePreferences()
        elif val.name == "KEY_ENTER":
            var.pref_bible_position = 1
            mh.back(term)
        elif val == '1':
            cursor_y = 1
            var.pref_bible_position = cursor_y
        elif val == '2':
            cursor_y = 2
            var.pref_bible_position = cursor_y
        elif val == '3':
            cursor_y = 3
            var.pref_bible_position = cursor_y
    