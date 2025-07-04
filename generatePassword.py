import os
import secrets
import string

import pyperclip
from pyfzf.pyfzf import FzfPrompt


def containsUppercase(password):
    for char in password:
        if char.isupper():
            return True
    return False


def containsSymbols(password):
    for char in password:
        if char in string.punctuation:
            return True
    return False


def getPassword(length=12, symbols=True, uppercase=True):
    combination: str = string.ascii_lowercase + string.digits
    if symbols:
        combination += string.punctuation
    if uppercase:
        combination += string.ascii_uppercase

    combination_length = len(combination)
    password = ""
    for _ in range(length):
        password += combination[secrets.randbelow(combination_length)]

    return password


def copyToClipboard(password):
    pyperclip.copy(password)
    os.system("notify-send 'Password copied to clipboard'")  # Linux


def generatePassword():
    length = int(input("Enter the length of the password: "))
    symbols = input("Include symbols? (y/n): ").lower() == "y"

    passwords = []

    for _ in range(10):
        password = getPassword(length, symbols)
        passwords.append(password)

    fzf = FzfPrompt()
    selected_password = fzf.prompt(passwords)
    if selected_password:
        print(f"Selected password: {selected_password[0]}")
        copyToClipboard(selected_password[0])
    else:
        print("No password selected.")
