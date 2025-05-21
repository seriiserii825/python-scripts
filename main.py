#!/usr/bin/python3

from aspectRatio import aspectRatio
from calcBlocks import calcBlocks
from generatePassword import generatePassword
from sortFiles import sortFiles
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
    print("[yellow]6. Generate password")
    print("[blue]7. Calculate percentages")
    print("[green]8. Aspect Ratio")
    print("[blue]9. Sort files")

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
    elif choose == "6":
        generatePassword()
    elif choose == "7":
        calcBlocks()
    elif choose == "8":
        aspectRatio()
    elif choose == "9":
        sortFiles()
    else:
        exit()

menu()

# 1000
# 400
# 300
