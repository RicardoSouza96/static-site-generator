import os, shutil
from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main() -> None:
    """if os.path.exists(PUBLIC_PATH):
        shutil.rmtree(PUBLIC_PATH)
    copy_files_recursive(STATIC_PATH, PUBLIC_PATH)
    generate_pages_recursive(FROM_PATH, TEMPLATE_PATH, PUBLIC_PATH)"""
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public)
main()