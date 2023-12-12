from PIL import Image
import pytesseract
import numpy as np
import matplotlib.pyplot as plt
import json
import matplotlib.patches as patches


def draw_on_image():
    # img = plt.imread("screenshot_0.jpg")
    # fig, ax = plt.subplots()

    # with open("screenshot_0.json") as f:
    #     screenshot_data = json.load(f)
    #     print(screenshot_data)

    # ax.imshow(img)
    # x = screenshot_data["gaze_x"]
    # y = screenshot_data["gaze_y"]

    # ax.scatter(x, y)
    # plt.savefig("screenshot_with_draw_0")
    # # plt.show()

    # gpt code
    img = plt.imread("screenshot_0.jpg")
    fig, ax = plt.subplots()

    with open("screenshot_0.json") as f:
        screenshot_data = json.load(f)

    ax.imshow(img)

    x = screenshot_data["gaze_x"]
    y = screenshot_data["gaze_y"]

    # Assuming each point in x and y is a center of a square
    for xi, yi in zip(x, y):
        # Create a square as a rectangle, adjust the conversion from pixels to data coordinates as needed
        square = patches.Rectangle(
            (xi - 150, yi - 150), 300, 300, linewidth=1, edgecolor="r", facecolor="none"
        )
        ax.add_patch(square)

    plt.savefig("screenshot_with_draw_0")
    # plt.show()


def read_image():
    with open("screenshot_0.json") as f:
        screenshot_data = json.load(f)
        print(screenshot_data)

    screenshot = Image.open("screenshot_0.jpg")

    # write code to draw a box at the different points, this is where you're going to OCR.
    # define width and height of this box
    crop_width, crop_height = 300, 300

    timesteps = screenshot_data["time"]

    # at each time step, crop the image at the x,y coordinates and save
    for timestep in timesteps:
        image_x = screenshot_data["gaze_x"][timestep]
        image_y = screenshot_data["gaze_y"][timestep]

        # Calculate the top-left corner of the cropping box
        start_x = image_x - crop_width // 2
        start_y = image_y - crop_height // 2

        # Crop the image
        cropped_image = screenshot.crop(
            (start_x, start_y, start_x + crop_width, start_y + crop_height)
        )

        # save image - change this to save it into a folder
        cropped_image.save(f"cropped_images/cropped_image_{timestep}.jpg")

        crop_text = pytesseract.image_to_string(cropped_image)

        print("timestep:", timestep)
        print("crop_text:", crop_text)


if __name__ == "__main__":
    pytesseract.pytesseract.tesseract_cmd = (
        # r"c:\Program Files\Tesseract-OCR\tesseract.exe" # Nyan's one
        r"c:\Users\allis\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
    )

    # draw_on_image()

    # read_image()
