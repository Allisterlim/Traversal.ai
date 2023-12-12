from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = (
    r"c:\Program Files\Tesseract-OCR\tesseract.exe"
)

image = Image.open("screenshot_2.jpg")
print(pytesseract.image_to_string(image))
