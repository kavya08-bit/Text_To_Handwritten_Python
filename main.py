from PIL import Image ,ImageDraw,ImageFont,ImageFilter

img = Image.new("RGB", (3000, 500), color="white")

draw = ImageDraw.Draw(img)

font = ImageFont.truetype("fonts/QEDavidReidCAP.ttf", 40)
draw.text((50, 50), "Hello World", fill="black", font=font)

font = ImageFont.truetype("fonts/QEHerbertCooper.ttf", 40)
draw.text((2000, 50), "Hello World", fill="black", font=font)

img.save("output.png")

img.show()