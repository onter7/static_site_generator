import os
import shutil

from copystatic import copy_content


dir_path_static = "./static"
dir_path_public = "./public"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    copy_content(dir_path_static, dir_path_public)


main()