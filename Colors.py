from colorama import init
from termcolor import colored

init()

def red_text(string):
    return colored(string, color="red")

def green_text(string):
    return colored(string, color="green")

def bold_text(text):
    return colored(text, attrs=["bold"])

def print_bold(text):
    print(bold_text(text))

def dark_text(text):
    return colored(text, attrs=["dark"])

def print_dark(text):
    print(dark_text(text))
