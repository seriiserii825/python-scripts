#!/usr/bin/python3
from py_libs.Clipboard import Clipboard


def bitbucketUrl():
    clipboard = Clipboard.read()

    if clipboard.startswith("git clone git@bitbucket.org:sites-bludelego"):
        clipboard = clipboard.replace(
            clipboard, "git clone git@bitbucket.org-b:sites-bludelego"
        )
        Clipboard.write(clipboard)
    else:
        print("Not a valid Bitbucket URL")
