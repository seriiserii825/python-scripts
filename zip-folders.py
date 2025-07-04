#!/usr/bin/env python3
import os

folders = [f for f in os.listdir(".") if os.path.isdir(f)]
for index, folder in enumerate(folders):
    print(f"{index + 1}. {folder}")
    os.system(f'zip -r "{folder}.zip" "{folder}"')
