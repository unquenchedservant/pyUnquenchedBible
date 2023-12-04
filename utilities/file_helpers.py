import os
from utilities import variables as var

def getRootPath():
    if os.name("nt"):
        rootPath = os.path.expanduser("~") + "AppData/Roaming/UnquenchedBible"
    elif os.name("posix"): #wow, this is easy now, with mac and linux both being posix now
        rootPath = os.path.expanduser("~") + "/.unquenchedbible"
    
    return rootPath 

def getPreferencesPath():
    return getRootPath() + "/preferences.json"
