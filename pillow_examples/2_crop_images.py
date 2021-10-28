from PIL import Image

image = Image.open('../images/example_product.png')
cropped = image.crop((0, 100, 200, 400))

cropped.save('example_product_cropped.png')
