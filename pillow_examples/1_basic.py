from PIL import Image

production = Image.open("../images/example_product.png")
staging = Image.open("../images/example_staging.png")

production.show()
staging.show()
