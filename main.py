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
text = """Batman[b] is a superhero who appears in American comic books published by DC Comics. Batman was created by writer Bill Finger and artist Bob Kane, and debuted in the 27th issue of the comic book Detective Comics on March 30, 1939. In the DC Universe, Batman is the alias of Bruce Wayne, a wealthy American playboy, philanthropist, and industrialist who resides in the fictional Gotham City. His origin story features him swearing vengeance against criminals after witnessing the murder of his parents, Thomas and Martha, as a child, a vendetta tempered by the ideal of justice. He trains himself physically and intellectually, crafts a bat-inspired persona, and monitors the Gotham streets at night. Kane, Finger, and other creators accompanied Batman with supporting characters, including his sidekicks Robin and Batgirl; allies Alfred Pennyworth and James Gordon; love interest and occasional adversary Catwoman; as well as foes such as the Penguin, the Riddler, Two-Face, and his archenemy, the Joker.

Kane conceived Batman in early 1939 to capitalize on the popularity of Superman; although Kane frequently claimed sole creation credit, Finger substantially developed the concept from a generic superhero into something more bat-like. They drew inspiration from pulp fiction characters like the Shadow, Sherlock Holmes, and the Green Hornet. Batman received a spin-off publication, Batman, in 1940. Kane and Finger introduced Batman as a ruthless vigilante who frequently killed or maimed criminals, but he evolved into a just, tempered superhero with a stringent moral code that prohibits killing during the 1940s. Unlike most superheroes, Batman does not possess any superpowers, instead relying on his intellect, fighting skills, and wealth. The 1960s Batman television series used a camp aesthetic, which continued to be associated with Batman for years after it ended. Various creators worked to return Batman to his darker roots in the 1970s and 1980s, culminating with the 1986 miniseries The Dark Knight Returns by Frank Miller.

DC has featured Batman in many comic books, including comics published under its imprints such as Vertigo and Black Label; he has been considered DC's flagship character[4][5]since the 1990s. The longest-running Batman comic, Detective Comics, is the longest-running comic book in the United States. Batman is frequently depicted alongside other DC superheroes, such as Superman and Wonder Woman, as a member of organizations such as the Justice League and the Outsiders. In addition to Bruce Wayne, other characters used the Batman persona, such as Jean-Paul Valley / Azrael in the 1993–1994 "Knightfall" story arc; Dick Grayson, the first Robin, from 2009 to 2011; and Jace Fox, the son of Wayne's ally Lucius, since 2021.[6] DC has also published comics featuring alternate versions of Batman, including the incarnation seen in The Dark Knight Returns and its successors, the incarnation from the Flashpoint (2011) event, and numerous interpretations in comics published under the Elseworlds label."""
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

# pages.append(paper)            save multiple pages

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


background.show()