import cv2
import numpy as np
import random
from common import BASE_DIR, IMAGES_TRAIN, LABELS_TRAIN, IMAGES_VAL, LABELS_VAL

WIDTH = 256
HEIGHT = 256

NUM_TRAIN = 30
NUM_VAL = 3

def make_img_square_circle(path_img, path_label):
    circles = random.randint(1, 2)
    squares = random.randint(1, 2)
    bg_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    img_arr = np.full((HEIGHT, WIDTH, 3), bg_color, np.uint8)
    labels = []
    for i in range(circles):
        x, y, radius, color = random_circle_params()
        cv2.circle(img_arr, (x, y), radius, color, -1)
        mlc = make_label_circle(x, y, radius)
        labels.append(mlc)
    for i in range(squares):
        x, y, width, color = random_square_params()
        cv2.rectangle(img_arr, (x - width // 2, y - width // 2),
                      (x + width // 2, y + width // 2), color, -1)
        mls = make_label_square(x, y, width)
        labels.append(mls)
    cv2.imwrite(path_img, img_arr)
    with open(path_label, 'w') as f:
        f.write('\n'.join(labels))


def make_label_circle(x_center, y_center, radius):
    x = x_center / WIDTH
    y = y_center / HEIGHT
    w = radius * 2 / WIDTH
    h = radius * 2 / HEIGHT
    return f"0 {x:.6f} {y:.6f} {w:.6f} {h:.6f}"

def make_label_square(x_center, y_center, width):
    x = x_center / WIDTH
    y = y_center / HEIGHT
    w = width / WIDTH
    h = width / HEIGHT
    return f"1 {x:.6f} {y:.6f} {w:.6f} {h:.6f}"

def random_circle_params():
    radius = random.randint(1, min(WIDTH, HEIGHT) // 2)
    x_center = random.randint(radius, WIDTH - radius)
    y_center = random.randint(radius, HEIGHT - radius)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return x_center, y_center, radius, color

def random_square_params():
    width = random.randint(1, min(WIDTH, HEIGHT) // 2)
    half = width // 2
    x_center = random.randint(half, WIDTH - half)
    y_center = random.randint(half, HEIGHT - half)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return x_center, y_center, width, color


def generate_dataset(count, images_dir, labels_dir):
    for i in range(count):
        make_img_square_circle(images_dir + f"/img{i}.jpg", labels_dir + f"/img{i}.txt")

generate_dataset(NUM_TRAIN, BASE_DIR + IMAGES_TRAIN, BASE_DIR + LABELS_TRAIN)
generate_dataset(NUM_VAL, BASE_DIR + IMAGES_VAL, BASE_DIR + LABELS_VAL)