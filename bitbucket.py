#!/usr/bin/python3
import pyperclip

from libs.buffer import addToClipBoard


def bitbucketUrl():
    clipboard = pyperclip.paste()

    if clipboard.startswith("git clone git@bitbucket.org:sites-bludelego"):
        clipboard = clipboard.replace(
            clipboard, "git clone git@bitbucket.org-b:sites-bludelego"
        )
        addToClipBoard(clipboard)
    else:
        print("Not a valid Bitbucket URL")
