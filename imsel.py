

import click
import os
import cv2


ESCAPE = 27
DELETE = 0
MAX_HEIGHT = 800


def read_scale_image(path: str) -> cv2.Mat:
    img = cv2.imread(path)
    height, width = img.shape[:2]

    if height > MAX_HEIGHT:
        new_height = MAX_HEIGHT
        ratio = new_height / height
        width = width * ratio
        height = new_height

    img = cv2.resize(img, (int(width), int(height)))

    return img


@click.command()
@click.option('--path', '-p', required=True, type=str, help='The path to iterate')
@click.option('--start_index', '-i', required=False, default=0, type=int, help='The start index')
def main(path, start_index):
    '''
    Iterates through all image files in this path and shows
    the image in a popup. Press any to keep the image
    and continue to the next, or press "Del" to delete the image immediately.
    Press "escape" to exit the program immediately.
    '''
    files = os.listdir(path)
    files.sort()
    index = start_index
    files = files[index:]
    for file in files:
        full_path = os.path.join(path, file)
        img = read_scale_image(full_path)
        cv2.imshow('img', img)
        key = cv2.waitKey()

        if key == ESCAPE:
            exit(0)
        if key == DELETE:
            os.remove(full_path)
        else:
            index += 1
            print(f'Progress: {index}/{len(files)},\
                  {(index / len(files)) * 100:.2f}%')


if __name__ == '__main__':
    main()
