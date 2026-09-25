import os


def addToClipBoardFile(file):
    command = f"cat {file} | xclip -selection clipboard"
    print(command)
    os.system(command)
