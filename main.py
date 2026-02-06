from PIL import Image ,ImageDraw,ImageFont,ImageFilter
import random

X_JITTER = 7    # left-right pixels
Y_JITTER = 7    # up-down pixels
WORD_SPACE = 12

# Starting position (margin)
x, y = 10, 150 # the x and y where written line is start
line_gap = 95  # the margin between lines

background = Image.open("background/background.jpeg").convert("RGB")
background = background.resize((1200, 1600))                

TOP_MARGIN = 140
BOTTOM_MARGIN = background.height - 30


PAGE_WIDTH = background.width
LEFT_MARGIN = x
RIGHT_MARGIN = PAGE_WIDTH - 70  


# draw = ImageDraw.Draw(background)
font = ImageFont.truetype("fonts/QEDavidReidCAP.ttf", 40)

pages = []          # store completed pages
page_count = 1

def new_page():
    img = Image.open("background/background.jpeg").convert("RGB")
    img = img.resize((1200, 1600))
    return img, ImageDraw.Draw(img)

paper , draw = new_page()  # make new page using func()
y = TOP_MARGIN

# Text input
# text = """"""     # for input in code
with open("input/input.txt", "r", encoding="utf-8") as file:
    text = file.read()

lines = text.split("\n")

# for line in lines:    # how the text input is printing 
#     draw.text((x, y), line, fill=(20, 20, 60), font=font)
#     y += line_gap


for line in lines:         # this for loop add human error while writing like writing under the line over the line etc
    current_x = x
    words = line.split(" ")

    for word in line.split(" "):
        x_offset = random.randint(-X_JITTER, X_JITTER)
        y_offset = random.randint(-Y_JITTER, Y_JITTER)
        word_width = draw.textlength(word, font=font)

        if current_x + word_width >= RIGHT_MARGIN:   # create new line
            y += line_gap
            current_x = LEFT_MARGIN

        if y + line_gap >= BOTTOM_MARGIN:  # create new page
            pages.append(paper)
            paper, draw = new_page()
            y = TOP_MARGIN

        draw.text(
            (current_x + x_offset, y + y_offset),
            word,
            fill=(20, 20, 60),
            font=font
        )


        current_x += word_width + WORD_SPACE

    y += line_gap


# background.save("output.png")  # the output img is saved 

pages.append(paper)      #      save multiple pages

# for i, page in enumerate(pages, start=1):
#     page.save(f"output_page_{i}.png")

# print(f"Saved {len(pages)} handwritten pages")

pages = [page.convert("RGB") for page in pages]

pages[0].save(                           # save output in pdf
    "handwritten_notes.pdf",
    save_all=True,
    append_images=pages[1:]
)

print(f"Saved {len(pages)} pages into handwritten_notes.pdf")


# background.show()