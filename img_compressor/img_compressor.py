import os
from PIL import Image, ImageFile

IMG_DIRS = ["articles", "events", "news"]

IMG_DIR = "../sch/media/img/"

images = list()

def reduce_image_size():
    for dir in IMG_DIRS:
        for file in os.listdir(f"{IMG_DIR}/{dir}"):
            if os.stat(f"{IMG_DIR}/{dir}/{file}").st_size > 1048576:
                images.append(f"{IMG_DIR}/{dir}/{file}")

    for image in images:
        img = Image.open(image)
        if (img.size > (1024, 1024)) and (image[-4::] not in ["jpeg", ".png"]):
            img.thumbnail((1024, 1024))
            img.save(image, optimize=True, quality=60)
            images.remove(image)


if __name__ == "__main__":
    reduce_image_size()
    print("+-------------+")
    print("|Files Changed|")
    print("+-------------+")
    print(f"UnChanged Files: {images}")
    # while True:
    #     reduce_image_size()
    #     print("----------")

