from PIL import Image
import pytesseract

# pytesseract.pytesseract.tesseract_cmd = (
#     r"C:\Users\allis\miniconda3\envs\memoryai\Library\bin"
# )


image = Image.open("helloworld.jpg")
print(pytesseract.image_to_string(image))
