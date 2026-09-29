import os

def gen_image_tags(folder, strings):
    for e in os.scandir(folder):
        if e.is_file():
            strings += [f"<img src=\".{e.path}\" width=\"700px\">"]
        elif e.is_dir():
            strings += gen_image_tags(e, [])
    return strings
if __name__ == "__main__":
    s = gen_image_tags("./images/hcrr", [])
    for tag in sorted(s):
        print(tag)