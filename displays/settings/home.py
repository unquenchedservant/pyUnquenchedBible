import sys
from utilities import variables as var, menu as m, menu_helpers as mh
from displays.settings import pref_bible
from displays.settings import bible_versions
from displays.settings import psalms
    
def getPreferredBible(version):
    if version == "bible_gateway":
        return "Bible Gateway"
    elif version == "logos":
        return "Logos Bible Software"
    else:
        return "Unknown"
def start(term):
    var.menu_type="settings"
    cursor_y = var.settings_position
    title_str = "Settings"
    status_msg = "Enter to change settings |  Press 'esc' to go back"
    option_1 = "Preferred Bible (Current: {})".format(getPreferredBible(var.preferred_bible))
    option_2 = "Bible Version (Logos Only) (Current: {})".format(var.bible_version)
    option_3 = "Read 5 Psalms a Day (Current: {})".format(var.psalms)
    while True:
        m.clear(term)
        m.title(term, title_str)
        m.status_bar(term, status_msg)
        m.menu_option(term, option_1, 1, cursor_y)
        m.menu_option(term, option_2, 2, cursor_y)
        m.menu_option(term, option_3, 3, cursor_y)
        m.menu_option(term, "Go back", 4, cursor_y)
        val = term.inkey()
        if val == 'q' or val.name == "KEY_ESCAPE":
            m.clear(term)
            sys.exit()
        elif val == '1':
            cursor_y = 1
            var.settings_position = cursor_y
        elif val == '2':
            cursor_y = 2
            var.settings_position = cursor_y
        elif val == '3':
            cursor_y = 3
            var.settings_position = cursor_y
        elif val == '4':
            cursor_y = 4
            var.settings_position = cursor_y
        elif val.name == "KEY_UP":
            cursor_y -= 1
            if cursor_y == 0:
                cursor_y = 4
            var.settings_position = cursor_y
        elif val.name == "KEY_DOWN":
            cursor_y += 1
            if cursor_y == 5:
                cursor_y = 1
            var.settings_position = cursor_y
        elif val.name == "KEY_ENTER":
            if cursor_y == 1:
                pref_bible.start(term)
            elif cursor_y == 2:
                bible_versions.start(term)
            elif cursor_y == 3:
                psalms.start(term)
            elif cursor_y == 4:
                var.settings_position = 1
                mh.back(term)
    