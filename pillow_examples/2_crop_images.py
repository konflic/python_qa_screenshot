from PIL import Image

image = Image.open('../images/example_product.png')
cropped = image.crop((0, 80, 200, 400))
cropped.save('../images/example_product_cropped.png')
