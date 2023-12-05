import os
import json
from utilities import variables as var

def getRootPath():
    if os.name("nt"):
        rootPath = os.path.expanduser("~") + "AppData/Roaming/UnquenchedBible"
    elif os.name("posix"): #wow, this is easy now, with mac and linux both being posix now
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
