import os
import webbrowser
from rich import print


def openGitRepo():
    ## check if exists .git folder
    if not os.path.exists(".git"):
        print("[red]This is not a git repository")
        return
    ## get remote url
    remote = os.popen("git remote -v").read().split()[1]
    # print(remote)
    ## if remote start with git, change to https just first occurence
    if remote.startswith("git"):
        if 'bitbucket' in remote:
            remote = remote.replace("git@", "https://", 1)
            # replace last .git with src/main
            remote = remote.replace(".git", "/src/main")
            remote = remote.replace("org:", "org/")       
            print(remote)
        else:
            remote = remote.replace("git@", "https://", 1)
            remote = remote.replace("com:", "com/")       
            # print(remote)
    # print(remote)
    # webbrowser.open('https://nabinkhadka.com.np', new = 2)
    webbrowser.open(remote, new=0)
# https://bitbucket.org/seriiserii825/xubuntu/src/main
