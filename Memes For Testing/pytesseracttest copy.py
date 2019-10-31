import pytesseract
from PIL import Image
import sys

input = 'Screen Shot 2019-10-26 at 11.36.35 PM.png'
output = pytesseract.image_to_string(Image.open(input))
print(output)

image_file = Image.open(input) # open colour image
image_file = image_file.convert('1') # convert image to black and white
image_file.save('result.png')

print("2nd Try")

input = 'result.png'
output = pytesseract.image_to_string(Image.open(input))
print(output)
