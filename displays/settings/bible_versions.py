import sys
from utilities import variables as var, menu as m, menu_helpers as mh
from utilities import file_helpers as fh
def getSettingChecked(version):
    if var.bible_version == version:
        return "X"
    else:
        return " "
def getIndex(version):
    returnValues = {
        "ESV": 1,
        "NIV": 2,
        "KJV": 3,
        "CSB": 4,
        "NASB": 5,
        "NASB2020": 6,
        "NKJV": 7,
        "NLT": 8,
        "NET": 9,
        "MSG": 10,
        "LEB": 11,
        "NRSV": 12,
        "RSV": 13,
        "PASSION": 14,
        "ASV": 15
    }
    return returnValues[version]

def start(term):
    var.menu_type="bible_version"
    var.bible_version_position = getIndex(var.bible_version)
    cursor_y = var.bible_version_position
    title_str = "Settings - Bible Version"
    status_msg = "Press Tab to Select |  Press 'esc' to go back  | Autosaves"
    while True:
        option_1 = "[{}] ESV".format(getSettingChecked("ESV"))
        option_2 = "[{}] NIV".format(getSettingChecked("NIV"))
        option_3 = "[{}] KJV".format(getSettingChecked("KJV"))
        option_4 = "[{}] CSB".format(getSettingChecked("CSB"))
        option_5 = "[{}] NASB1995".format(getSettingChecked("NASB"))
        option_6 = "[{}] NASB2020".format(getSettingChecked("NASB2020"))
        option_7 = "[{}] NKJV".format(getSettingChecked("NKJV"))
        option_8 = "[{}] NLT".format(getSettingChecked("NLT"))
        option_9 = "[{}] NET".format(getSettingChecked("NET"))
        option_10 = "[{}] MSG".format(getSettingChecked("MSG"))
        option_11 = "[{}] LEB".format(getSettingChecked("LEB"))
        option_12 = "[{}] NRSV".format(getSettingChecked("NRSV"))
        option_13 = "[{}] RSV".format(getSettingChecked("RSV"))
        option_14 = "[{}] Passion".format(getSettingChecked("PASSION"))
        option_15 = "[{}] ASV".format(getSettingChecked("ASV"))
        m.clear(term)
        m.title(term, title_str)
        m.status_bar(term, status_msg)
        m.menu_option(term, option_1, 1, cursor_y)
        m.menu_option(term, option_2, 2, cursor_y)
        m.menu_option(term, option_3, 3, cursor_y)
        m.menu_option(term, option_4, 4, cursor_y)
        m.menu_option(term, option_5, 5, cursor_y)
        m.menu_option(term, option_6, 6, cursor_y)
        m.menu_option(term, option_7, 7, cursor_y)
        m.menu_option(term, option_8, 8, cursor_y)
        m.menu_option(term, option_9, 9, cursor_y)
        m.menu_option(term, option_10, 10, cursor_y)
        m.menu_option(term, option_11, 11, cursor_y)
        m.menu_option(term, option_12, 12, cursor_y)
        m.menu_option(term, option_13, 13, cursor_y)
        m.menu_option(term, option_14, 14, cursor_y)
        m.menu_option(term, option_15, 15, cursor_y)
        m.menu_option(term, "Go Back", 16, cursor_y)
        val = term.inkey()
        if val == 'q' or val.name == "KEY_ESCAPE":
            m.clear(term)
            sys.exit()
        elif val == "KEY_UP":
            cursor_y -= 1
            if cursor_y == 0:
                cursor_y = 16
            var.reading_position = cursor_y
        elif val == "KEY_DOWN":
            cursor_y += 1
            if cursor_y == 17:
                cursor_y = 1
            var.reading_position = cursor_y
        elif val == "KEY_TAB":
            if cursor_y == 1:
                var.bible_version = "ESV"
                fh.savePreferences()    
            elif cursor_y == 2:
                var.bible_version = "NIV"
                fh.savePreferences()
            elif cursor_y == 3:
                var.bible_version = "KJV"
                fh.savePreferences()
            elif cursor_y == 4:
                var.bible_version = "CSB"
                fh.savePreferences()
            elif cursor_y == 5:
                var.bible_version = "NASB"
                fh.savePreferences()
            elif cursor_y == 6:
                var.bible_version = "NASB2020"
                fh.savePreferences()
            elif cursor_y == 7:
                var.bible_version = "NKJV"
                fh.savePreferences()
            elif cursor_y == 8:
                var.bible_version = "NLT"
                fh.savePreferences()
            elif cursor_y == 9:
                var.bible_version = "NET"
                fh.savePreferences()
            elif cursor_y == 10:
                var.bible_version = "MSG"
                fh.savePreferences()
            elif cursor_y == 11:
                var.bible_version = "LEB"
                fh.savePreferences()
            elif cursor_y == 12:
                var.bible_version = "NRSV"
                fh.savePreferences()
            elif cursor_y == 13:
                var.bible_version = "RSV"
                fh.savePreferences()
            elif cursor_y == 14:
                var.bible_version = "PASSION"
                fh.savePreferences()
            elif cursor_y == 15:
                var.bible_version = "ASV"
                fh.savePreferences()
        elif val.name == "KEY_ENTER":
            var.bible_version_position = 1
            mh.back(term)
        elif val == "1":
            cursor_y = 1
            var.bible_version_position = cursor_y
        elif val == "2":
            cursor_y = 2
            var.bible_version_position = cursor_y
        elif val == "3":
            cursor_y = 3
            var.bible_version_position = cursor_y
        elif val == "4": 
            cursor_y = 4
            var.bible_version_position = cursor_y
        elif val == "5":
            cursor_y = 5
            var.bible_version_position = cursor_y
        elif val == "6":
            cursor_y = 6
            var.bible_version_position = cursor_y
        elif val == "7":
            cursor_y = 7
            var.bible_version_position = cursor_y
        elif val == "8":
            cursor_y = 8
            var.bible_version_position = cursor_y
        elif val == "9":
            cursor_y = 9
            var.bible_version_position = cursor_y
        elif val == "0":
            cursor_y = 10
            var.bible_version_position = cursor_y
        elif val == "-":
            cursor_y = 11
            var.bible_version_position = cursor_y
        elif val == "=":
            cursor_y = 12
            var.bible_version_position = cursor_y
        
        