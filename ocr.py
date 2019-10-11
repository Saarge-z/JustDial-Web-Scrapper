import pytesseract
from PIL import Image

img = Image.open('screenshot.png')
print (pytesseract.image_to_string(img))