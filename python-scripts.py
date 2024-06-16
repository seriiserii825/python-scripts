#!/usr/bin/python3

from termcolor import colored
from bitbucket import bitbucketUrl
from convert_fonts import convertFontsFunc
from create_project import createProject
from cyr_to_lat import cyrToLat

def menu():
    print(colored("1. Create project", "magenta"))
    print(colored("2. Convert fonts", "blue"))
    print(colored("3. Cyr to lat", "yellow"))
    print(colored("4. Bitbucket change url", "blue"))

    choose = input("Choose number: ")
    if choose == "1":
        createProject()
    elif choose == "2":
        convertFontsFunc()
    elif choose == "3":
        cyrToLat()
    elif choose == "4":
        bitbucketUrl()
    else:
        exit()

menu()
