import os
import shutil


from copystatic import copy_content
from getcontent import generate_page


dir_path_static = "./static"
dir_path_public = "./public"
path_content = "./content/index.md"
path_template = "./template.html"
path_index = "./public/index.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    copy_content(dir_path_static, dir_path_public)
    generate_page(path_content, path_template, path_index)


main()