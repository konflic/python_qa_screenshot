from PIL import Image, ImageDraw, ImageFont

image_object = Image.open("../images/example_product.png").convert("RGB")

idraw = ImageDraw.Draw(image_object)
text = "Эта надпись раньше тут не была"

font = ImageFont.truetype("arial.ttf", size=60)

idraw.text((100, 100), text, font=font)
idraw.rectangle((300, 300, 600, 600), fill="red")

image_object.save('example_product_tag.png')
