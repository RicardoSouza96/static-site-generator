import os, shutil
from copystatic import copy_files_recursive

PUBLIC_PATH = "public/"
STATIC_PATH = "static/"

def main():
    if os.path.exists(PUBLIC_PATH):
        shutil.rmtree(PUBLIC_PATH)
    copy_files_recursive(STATIC_PATH, PUBLIC_PATH)
main()