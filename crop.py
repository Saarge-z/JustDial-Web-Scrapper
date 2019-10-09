from PIL import Image
def crop(png_image_name):
    img = Image.open(png_image_name)
    area = (160, 220, 400, 300)
    cropped_img = img.crop(area)
    cropped_img.save(png_image_name)
    cropped_img.show()
crop('screenshot.png')
# for f in listdir('.'):
#     if f.endswith('.png'):
#         crop(f)