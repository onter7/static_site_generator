import os
import shutil


from copystatic import copy_content
from getcontent import generate_pages_recursive


dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
path_template = "./template.html"
dest_dir_path = "./public"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    copy_content(dir_path_static, dir_path_public)
    generate_pages_recursive(dir_path_content, path_template, dest_dir_path)


main()