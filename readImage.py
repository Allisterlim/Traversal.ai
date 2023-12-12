from PIL import Image
import pytesseract
import numpy as np
import matplotlib.pyplot as plt
import json


pytesseract.pytesseract.tesseract_cmd = (
    # r"c:\Program Files\Tesseract-OCR\tesseract.exe" # Nyan's one
    r"c:\Users\allis\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
)

img = plt.imread("screenshot_0.jpg")
fig, ax = plt.subplots()

with open("screenshot_0.json") as f:
    screenshot_data = json.load(f)
    print(screenshot_data)

ax.imshow(img)
x = screenshot_data["gaze_x"]
y = screenshot_data["gaze_y"]


ax.scatter(x, y)
plt.savefig("screenshot_with_draw_0")

# plt.show()

# write code to draw a box at the different points, this is where you're going to OCR.
# define width and height of this box
crop_width, crop_height = 300, 200

timesteps = screenshot_data["time"]

# at each time step, crop the image at the x,y coordinates and save
for timestep in timesteps:
    image_x = screenshot_data["gaze_x"][timestep]
    image_y = screenshot_data["gaze_y"][timestep]

    # Calculate the top-left corner coordinates
    start_x = image_x - crop_width // 2
    start_y = image_y - crop_height // 2

    cropped_image = img[start_y : start_y + crop_height, start_x : start_x + crop_width]

    # Convert the cropped image to a PIL Image
    cropped_image_pil = Image.fromarray(cropped_image)

    # Save the cropped image
    cropped_image_pil.save(f"cropped_image_{timestep}.jpg")

    crop_text = pytesseract.image_to_string(cropped_image)

    print("timestep:", timestep)
    print("crop_text:", crop_text)


# draw this to visualize and adjust how big your OCR boxes should be
# you might be unnecessarily converting to numpy arrays and then back to images.
