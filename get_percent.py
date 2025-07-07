import os
import pyperclip


def get_percent_from_width():
    data = input("Enter full width and width f,w: ")
    if data and "," in data:
        full_width, width = data.split(",")
        if not full_width.strip().isdigit():
            exit("full_width is not digit")
        if not width.strip().isdigit():
            exit("width is not digit")
    else:
        exit("enter width,height by comma")

    full_width = int(full_width)
    width = int(width)
    percent = round((width / full_width) * 100, 2)
    percent = f"{percent}%"

    pyperclip.copy(percent)
    os.system(f"notify-send 'Percent {percent} copied to clipboard'")
