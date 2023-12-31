import os
import json
from utilities import file_helpers as fh
def checkFiles():
    if not os.path.exists(fh.getRootPath()):
        os.mkdir(fh.getRootPath())
        fh.savePreferences()
        #There will be three here, one more for each reading plan
    else:
        fh.loadPreferences()
def init():
    # Position variables (These aren't saved)
    global main_position # this holds where on the main menu you are 
    main_position = 1
    global reading_position
    reading_position = 1
    global settings_position
    settings_position = 1
    global pref_bible_position
    pref_bible_position = 1
    global bible_version_position
    bible_version_position = 1
    global menu_type # this holds what menu you are on
    menu_type = "main"
    global psalms_position #this one needs to be one off, to account for the top line being a title
    psalms_position = 2

    #General Settings (Needs a file)
    global reading_plan # will hold professor grant horner or mcheyne at some point
    reading_plan = "pgh"
    global bible_version # will try to include as many as possible, will rely on requests
    bible_version="NIV" 
    global preferred_bible
    preferred_bible = "bible_gateway" # two options: "BibleGateway" or "Logos"
    global psalms # this will be a boolean, true if you want to read 5 psalms a day, false if you don't
    psalms = False  

    #Reading Plan Settings (Needs a file)
    global pgh_day
    pgh_day = 0 # 0 is disabled
    global pgh_lists_done
    pgh_lists_done = 0 # max is 10
    global pgh_list_1
    pgh_list_1 = 1
    global pgh_list_1_done
    pgh_list_1_done = False
    global pgh_list_2
    pgh_list_2 = 1
    global pgh_list_2_done
    pgh_list_2_done = False
    global pgh_list_3
    pgh_list_3 = 1
    global pgh_list_3_done
    pgh_list_3_done = False
    global pgh_list_4
    pgh_list_4 = 1
    global pgh_list_4_done
    pgh_list_4_done = False
    global pgh_list_5
    pgh_list_5 = 1
    global pgh_list_5_done
    pgh_list_5_done = False
    global pgh_list_6
    pgh_list_6 = 1
    global pgh_list_6_done
    pgh_list_6_done = False
    global pgh_list_7
    pgh_list_7 = 1
    global pgh_list_7_done
    pgh_list_7_done = False
    global pgh_list_8
    pgh_list_8 = 1
    global pgh_list_8_done
    pgh_list_8_done = False
    global pgh_list_9
    pgh_list_9 = 1
    global pgh_list_9_done
    pgh_list_9_done = False
    global pgh_list_10
    pgh_list_10 = 1
    global pgh_list_10_done
    pgh_list_10_done = False

    #TODO: Add mcheyne variables

    checkFiles()