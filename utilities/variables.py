def init():
    # Position variabls
    global main_position # this holds where on the main menu you are 
    main_position = 1
    global reading_position
    reading_position = 1
    global settings_position
    settings_position = 1
    global pref_bible_position
    pref_bible_position = 1

    # Menu Variables
    global menu_type # this holds what menu you are on
    menu_type = "main"

    #General Settings (Needs a file)
    global reading_plan # will hold professor grant horner or mcheyne at some point
    reading_plan = "pgh"
    global bible_version # will try to include as many as possible, will rely on requests
    bible_version="NIV" 
    global preferred_bible
    preferred_bible = "bible_gateway" # two options: "BibleGateway" or "Logos"
