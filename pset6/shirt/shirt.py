import sys
import os

from PIL import Image

class IllegalArgumentError(ValueError):
    pass

def check_arguments():
    # Check for 3 arguments
    # - input
    # - output
    if len(sys.argv) < 3:
        raise IllegalArgumentError("Too few command-line arguments")
    elif len(sys.argv) > 3:
        raise IllegalArgumentError("Too many command-line arguments")

    # Check if file is image file
    for arg in [sys.argv[1], sys.argv[2]]:
        if ".jpg" not in arg and ".png" not in arg:
            raise IllegalArgumentError("Not an image file")

    # Check if both arg have same ext
    firstExt = sys.argv[1][sys.argv[1].index("."):]
    secondExt = sys.argv[2][sys.argv[2].index("."):]
    if firstExt != secondExt:
        raise IllegalArgumentError("Input and output have different extensions")

    # Check if file is present
    if not os.path.exists(sys.argv[1]):
        raise FileNotFoundError("File does not exist")
    
def paste_image(before_file, after_file):
    # Get shirt Image
    shirt = Image.open("shirt.png")

    # Get before image
    before = Image.open(before_file)
    before = before.resize((shirt.size[0], int(before.size[1]/before.size[0] * shirt.size[1]))) # resize to scale to match shirt
    diff_half = (
        int(before.size[0] - shirt.size[0]) / 2,
        int(before.size[1] - shirt.size[1]) / 2,
    )
    box = (0, diff_half[1], shirt.size[0], shirt.size[1] + diff_half[1]) # create crop box (x1, y1, x2, y2), centralised
    before = before.crop(box) # crop image 

    # paste image over
    before.paste(shirt, (0, 0), shirt)
    before.save(after_file)


def main():

    try:
        check_arguments()
    except Exception as e:
        sys.exit(e)
    else:
        paste_image(before_file=sys.argv[1], after_file=sys.argv[2])


if __name__ == "__main__":
    main()