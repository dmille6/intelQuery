import git
from pathlib import Path
import shutil


class pullFireHol:
    def __init__(self):
        print ("PullFireHol Object Created")

    def pullListsFromGit(self):
        try:
            #remove previous data
            dirpath = Path('blocklist-ipsets')
            print ("PATH:", dirpath)
            if dirpath.exists() and dirpath.is_dir():
                shutil.rmtree(dirpath)
            #pull new data
            git.Git(".").clone("git://github.com/firehol/blocklist-ipsets.git")
        except:
            print ("Error")