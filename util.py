import os
import sys

def gen_image_tags(folder, strings):
    for e in os.scandir(folder):
        if e.is_file():
            strings += [f"<img src=\".{e.path}\" width=\"700px\">"]
        elif e.is_dir():
            strings += gen_image_tags(e, [])
    return strings
if __name__ == "__main__":
    path = sys.argv[1]
    s = gen_image_tags(path, [])
    for tag in sorted(s):
        print(tag)