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

plt.show()

# write code to draw a box at the different points, this is where you're going to OCR.
# draw this to visualize and adjust how big your OCR boxes should be

# OCR for image to text
# print(pytesseract.image_to_string(image))
