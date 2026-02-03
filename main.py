from PIL import Image ,ImageDraw,ImageFont,ImageFilter

background = Image.open("background/background.jpeg").convert("RGB")

background = background.resize((1200, 1600))

draw = ImageDraw.Draw(background)


font = ImageFont.truetype("fonts/QEDavidReidCAP.ttf", 40)

# Text input
text = """Hello World
This text is aligned
with notebook lines
and looks natural"""

lines = text.split("\n")

# Starting position (margin)

x, y = 10, 150 # the x and y where written line is start
line_gap = 95  # the margin between lines


for line in lines:    # how the text input is printing 
    draw.text((x, y), line, fill=(0, 0, 0), font=font)
    y += line_gap

background.save("output.png")  # the output img is saved 

background.show()