import pyfiglet
import termcolor

from colorama import init
init(autoreset=True)

valid_color=("red","green","yellow","magenta","cyan","white")
def print_art(msg,color):
    if color not in valid_color:
        color='magenta'

    ascii_art=pyfiglet.figlet_format(msg)
    colored_ascii=termcolor.colored(ascii_art,color=color)
    print(colored_ascii)

msg = input("What would you like to print? ")
color=input("what color? ")
print_art(msg,color)