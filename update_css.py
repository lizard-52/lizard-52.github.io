# deeply cursed script idea. i didn't want to redo the css to move the header image path out and so i have this
import os
import pdb
from time import sleep
from datetime import datetime

header_images = [
    [[10,1], [10,31],"./wobsite_media/wobsite_header_fall.jpg"], \
    [[12,1], [12,25],"./wobsite_media/wobsite_header_christmas.jpg"], \
    [[11,1], [12,31],"./wobsite_media/wobsite_header_winter.jpg"],\
    [[1,1], [2,28],"./wobsite_media/wobsite_header_winter.jpg"],\
]

def get_correct_image(today):
    default = "./wobsite_media/wobsite_header.jpg"
    for img in header_images:
        start = datetime(today.year, img[0][0], img[0][1])
        end = datetime(today.year, img[1][0], img[1][1])
        if today <= end and today >= start:
            return img[2]
    return default

def update_line(l, new_img):
    start = l.find("url(") + 4
    end = l.find(".jpg);") + 4
    return l[:start] + new_img + l[end:]

def update_css():
    today = datetime.today()
    with open("main.css", 'r') as f:
        lines = f.readlines()
    for i, l in enumerate(lines):
        if "./wobsite_media/wobsite_header" in l:
            new_l = update_line(l, get_correct_image(today))
            if new_l != l:
                print("Update to %s" % new_l)
            lines[i] = update_line(l, get_correct_image(today))
    with open("main.css", 'w') as f:
        for l in lines:
            f.write(l)
def main():
    while True:
        update_css()
        sleep(60*60*1)

if __name__ == "__main__":
    main()