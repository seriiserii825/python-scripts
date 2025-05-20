#!/usr/bin/python3

from termcolor import colored
from bitbucket import bitbucketUrl
from convert_fonts import convertFontsFunc
from create_project import createProject
from cyr_to_lat import cyrToLat
from openGitRepo import openGitRepo
from rich import print

def menu():
    print("[green]1. Create project")
    print("[blue]2. Convert fonts")
    print("[green]3. Cyr to lat")
    print("[blue]4. Bitbucket change url")
    print("[green]5. Open github or bitbucket")

    choose = input("Choose number: ")
    if choose == "1":
        createProject()
    elif choose == "2":
        convertFontsFunc()
    elif choose == "3":
        cyrToLat()
    elif choose == "4":
        bitbucketUrl()
    elif choose == "5":
        openGitRepo()
    else:
        exit()

menu()
