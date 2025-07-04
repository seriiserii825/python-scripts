import os

import pyperclip


def aspectRatio():
    aspect_ratio = 1
    data = input("Enter width and height w,h: ")
    if data and "," in data:
        width, height = data.split(",")
        if not width.strip().isdigit():
            exit("width is not digit")
        if not height.strip().isdigit():
            exit("height is not digit")
    else:
        exit("enter width,height by comma")

    width = int(width)
    height = int(height)
    if width == 0 or height == 0:
        exit("width or height is zero")

    if width > height:
        aspect = round(width / height, 2)
        aspect_ratio = f"{aspect}/1"
    elif width < height:
        aspect = round(height / width, 2)
        aspect_ratio = f"1/{aspect}"
    else:
        aspect_ratio = "1/1"

    aspect_ratio = f"aspect-ratio: {aspect_ratio};"
    pyperclip.copy(aspect_ratio)
    os.system(f"notify-send 'Aspect ratio {aspect_ratio} copied to clipboard'")
