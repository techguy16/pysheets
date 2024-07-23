import libsheets
from colorama import Fore, Back, Style, just_fix_windows_console, init
import random
import os

just_fix_windows_console()
init()

goto = False 

def render():
    libsheets.clear()

    term_output = ""
    
    content = []
    for i in range((os.get_terminal_size().lines - 3)):
        content.append([str(random.randint(1,1000000))])
        for i in range(random.randint(1,10)):
            content[len(content) - 1].append(str(random.randint(1,1000000)))
        

    length_of_longest_line = 0
    index = 0
    for i in range(len(content)):
        if len(content[index]) > length_of_longest_line:
            length_of_longest_line = len(content[index])
        index += 1

    content_index = 0
    index = 1

    
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    alphabet_index = 0
    term_output=f"{" " * 3}"
    for i in range(10):
        term_output += f"{libsheets.center(alphabet[alphabet_index],15)} "
        alphabet_index += 1
    term_output += "\n"
    term_output += f"{libsheets.padright(str(index), len(str(len(content))))} "
    for i2 in range(len(content)):
        for i in range(len(content[content_index])):
            global goto
            if goto == True:
                global highlightX
                global highlightY
                if (i == highlightX - 1) and (i2 == highlightY - 1):
                    term_output += f"{Fore.BLACK}{Back.WHITE}"
            
            term_output += f"{libsheets.padright(content[content_index][0], 15)}{Style.RESET_ALL} "
        index += 1
        term_output += f"\n{Style.BRIGHT}{libsheets.padright(str(index), len(str(len(content))))}{Style.RESET_ALL} "
        content_index += 1

    print(term_output)
    command = input()
    if command.split(" ")[0] == "goto":
        goto = True
        highlightX = int(command.split(" ")[1])
        highlightY = int(command.split(" ")[2])
