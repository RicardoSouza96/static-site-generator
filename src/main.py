import os, shutil
from copystatic import copy_files_recursive
from gencontent import generate_page

PUBLIC_PATH = "public/"
DEST_PATH = "public/index.html"
STATIC_PATH = "static/"
FROM_PATH = "content/index.md"
TEMPLATE_PATH = "template.html"

def main():
    if os.path.exists(PUBLIC_PATH):
        shutil.rmtree(PUBLIC_PATH)
    copy_files_recursive(STATIC_PATH, PUBLIC_PATH)
    generate_page(FROM_PATH, TEMPLATE_PATH, DEST_PATH)
main()