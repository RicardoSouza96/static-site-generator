import os, shutil

def copy_files_recursive (source, destination):
    if not os.path.exists(destination):
        os.mkdir(destination)
    for item in os.listdir(source):
        source_path = os.path.join(source, item)
        destination_path = os.path.join(destination, item)
        if os.path.isfile(source_path):
            shutil.copy(source_path, destination_path)
            print(f"{source_path} -> {destination_path}")
        else:
            copy_files_recursive (source_path, destination_path)
        