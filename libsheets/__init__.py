import libsheets
import libsheets.rendermanager
import os

def padright(text, length):
    return text + (" " * (int(length) - int(len(text))))

def padleft(text, length):
    return (" " * (int(length) - int(len(text)))) + text

def center(text, length):
    if not len(text) % 2 == 0:
        text2 = text + " "
    else:
        text2 = text
    
    return (" " * int(round(int((int(length) - int(len(text2)))/2), 0)) + text2 + " " * int(round(int((int(length) - int(len(text2)))/2), 0)))

def render():
    """
    Just a random alias to a function in another file,
    just to make lives easier when code is edited
    """
    libsheets.rendermanager.render()\

def clear():
    os.system("clear||cls")