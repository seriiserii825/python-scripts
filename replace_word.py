#!/usr/bin/python3
import os

from termcolor import colored

from libs.select import selectMultiple

output = os.popen("fzf").read().split("\n")[0]
file_name = output.split("/")[-1].strip()
print(colored(f"file_name: {file_name}", "green"))

file_path_without_name = output.replace(file_name, "").strip()
files = os.popen("grep -l -Rwn . -e " + file_name).read().split("\n")
files = list(filter(None, files))
selected_files = selectMultiple(files)
print(colored(f"selected_files: {selected_files}", "blue"))

new_word = input("Enter new word: ")
if not new_word:
    print(colored("New word cannot be empty", "red"))
    exit(1)
print(colored(f"new_word: {new_word}", "yellow"))
new_file_path = file_path_without_name + new_word

for file in selected_files:
    os.popen(f"sed -i 's/{file_name}/{new_word}/g' {file}").read()
    print(colored(f"Replaced {file_name} with {new_word} in {file}", "green"))

os.system(f"mv {output} {new_file_path}")
print(colored(f"Renamed {output} to {new_file_path}", "blue"))
