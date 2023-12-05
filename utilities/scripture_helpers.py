import webbrowser
from utilities import variables as var
def openBibleGateway(parts):
    url = "https://www.biblegateway.com/passage/?search="
    for part in parts:
        url = url + part + "+"
        url = url[:-1] #takes out extra +
    webbrowser.open(url)

def openLogos(parts):
    chapter = parts[-1]
    remainder = parts[:-1]
    book = " ".join(remainder)
    logosBook = getLogosBook(book)
    logosRes = getLogosResource()
    logosRef = getLogosReference()
    logosURL = "logosres:{};ref={}.{}{};off=0".format(logosRes, logosRef, logosBook, str(chapter))
    webbrowser.open(logosURL)
def getLogosReference():
    logosReferences = {
        "ESV": "BibleESV",
        "NIV": "BibleNIV",
        "KJV": "BibleKJV",
        "CSB": "BibleCSB2",
        "NASB": "BibleNASB95",
        "NASB2020": "BibleNASB95",
        "NKJV": "BibleNKJV",
        "NLT": "BibleNLT",
        "NET": "BibleNET",
        "MSG": "Bible",
        "LEB": "BibleLEB2",
        # "AMP": "BibleAMP", i don't currently have the AMP in my logos
        "NRSV": "BibleNRSV",
        "RSV": "BibleRSV",
        "PASSION": "Bible",
        # "NCV": "BibleNCV", I don't currently have the NCV in my logos
        # "GW": "BibleGW", I don't currently have the GW in my logos
        "ASV": "BibleKJV"
    }
    return logosReferences[var.bible_version]
def getLogosResource():
    logos_resources = {
        "ESV": "esv",
        "NIV": "niv2011",
        "KJV": "kjv1900",
        "CSB": "csb",
        "NASB": "nasb95",
        "NASB2020": "nasb2020",
        "NKJV": "nkjv",
        "NLT": "nlt",
        "NET": "gs-netbible",
        "MSG": "message",
        "NRSV": "nsrv",
        "LEB": "leb",
        "RSV": "rsv",
        "PASSION": "pssntrnsltnsngs",
        "ASV": "asv"
    }
    return logos_resources[var.bible_version]
def getLogosBook(book):
    logos_books = { #first testing on NIV, will check ESV if difference
        "Genesis": "Ge",
        "Exodus": "Ex",
        "Leviticus": "Le",
        "Numbers": "Nu",
        "Deuteronomy": "Dt",
        "Joshua": "Jos",
        "Judges": "Jdg",
        "Ruth": "Ru",
        "1 Samuel": "1Sa",
        "2 Samuel": "2Sa",
        "1 Kings": "1Ki",
        "2 Kings": "2Ki",
        "1 Chronicles": "1Ch",
        "2 Chronicles": "2Ch",
        "Ezra": "Ezr",
        "Nehemiah": "Ne",
        "Esther": "Es",
        "Job": "Job",
        "Psalm": "Ps",
        "Proverbs": "Pr",
        "Ecclesiastes": "Ec",
        "Song of Solomon": "So",
        "Isaiah": "Is",
        "Jeremiah": "Je",
        "Lamentations": "La",
        "Ezekiel": "Eze",
        "Daniel": "Da",
        "Hosea": "Ho",
        "Joel": "Joe",
        "Amos": "Am",
        "Obadiah": "Ob",
        "Jonah": "Jon",
        "Micah": "Mic",
        "Nahum": "Na",
        "Habakkuk": "Hab",
        "Zephaniah": "Zep",
        "Haggai": "Hag",
        "Zechariah": "Zec",
        "Malachi": "Mal",
        "Matthew": "Mt",
        "Mark": "Mk",
        "Luke": "Lk",
        "John": "Jn",
        "Acts": "Ac",
        "Romans": "Ro",
        "1 Corinthians": "1Co",
        "2 Corinthians": "2Co",
        "Galatians": "Ga",
        "Ephesians": "Eph",
        "Philippians": "Php",
        "Colossians": "Col",
        "1 Thessalonians": "1Th",
        "2 Thessalonians": "2Th",
        "1 Timothy": "1Ti",
        "2 Timothy": "2Ti",
        "Titus": "Tt",
        "Philemon": "Phm",
        "Hebrews": "Heb",
        "James": "Jas",
        "1 Peter": "1Pe",
        "2 Peter": "2Pe",
        "1 John": "1Jn",
        "2 John": "2Jn",
        "3 John": "3Jn",
        "Jude": "Jud",
        "Revelation": "Re"
    }
    return logos_books[book]