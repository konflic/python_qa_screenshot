from PIL import Image
from PIL import ImageChops

# https://stackoverflow.com/questions/35176639/compare-images-python-pil/56280735
production = Image.open("../images/16d1c_prog.png").convert('RGB')
staging = Image.open("../images/16d1c_stag.png").convert('RGB')

# Find difference between images
difference = ImageChops.difference(production, staging)

if difference.getbbox():
    print("Different!")
else:
    print("Not different!")

difference.save("difference.png")
