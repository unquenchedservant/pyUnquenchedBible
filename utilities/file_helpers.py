import os
import json
from utilities import variables as var

def getRootPath():
    if os.name == "nt": #windows
        rootPath = os.path.expanduser("~") + "\\AppData\\Roaming\\UnquenchedBible"
    elif os.name == "posix": #wow, this is easy now, with mac and linux both being posix now
        rootPath = os.path.expanduser("~") + "/.unquenchedbible"
    return rootPath 

def getPreferencesPath():
    return getRootPath() + "/preferences.json"

def loadPreferences():
    with open(getPreferencesPath()) as json_file:
        preferences = json.load(json_file)
        var.reading_plan = preferences["reading_plan"]
        var.bible_version = preferences["bible_version"]
        var.preferred_bible = preferences["preferred_bible"]

def getPGHPath():
    return getRootPath() + "/pgh.json"

def getMcheynePath():
    return getRootPath() + "/mcheyne.json"

def savePreferences():
    preferences = {
        "reading_plan": var.reading_plan,
        "bible_version": var.bible_version,
        "preferred_bible": var.preferred_bible
    }
    preferences_json = json.dumps(preferences)
    with open(getPreferencesPath(), "w") as outfile:
        outfile.write(preferences_json)

def savePGH():
    pgh = {
        "day": var.pgh_day,
        "lists_done": var.pgh_lists_done,
        "list_1": var.pgh_list_1,
        "list_1_done": var.pgh_list_1_done,
        "list_2": var.pgh_list_2,
        "list_2_done": var.pgh_list_2_done,
        "list_3": var.pgh_list_3,
        "list_3_done": var.pgh_list_3_done,
        "list_4": var.pgh_list_4,
        "list_4_done": var.pgh_list_4_done,
        "list_5": var.pgh_list_5,
        "list_5_done": var.pgh_list_5_done,
        "list_6": var.pgh_list_6,
        "list_6_done": var.pgh_list_6_done,
        "list_7": var.pgh_list_7,
        "list_7_done": var.pgh_list_7_done,
        "list_8": var.pgh_list_8,
        "list_8_done": var.pgh_list_8_done,
        "list_9": var.pgh_list_9,
        "list_9_done": var.pgh_list_9_done,
        "list_10": var.pgh_list_10,
        "list_10_done": var.pgh_list_10_done
    }
    pgh_json = json.dumps(pgh)
    with open(getPGHPath(), "w") as outfile:
        outfile.write(pgh_json)