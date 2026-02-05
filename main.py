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
text = """Spider-Man is a superhero in American comic books published by Marvel Comics. Created by writer-editor Stan Lee and artist Steve Ditko, he first appeared in the anthology comic book Amazing Fantasy #15 (August 1962) in the Silver Age of Comic Books. Considered one of the most popular and commercially successful superheroes, he has been featured in comic books, television shows, films, video games, novels, and plays.

Spider-Man is the secret identity of Peter Benjamin Parker, who was raised by his Aunt May and Uncle Ben in Queens, New York City, after the death of his parents. Lee, Ditko, and later writers had the character deal with the struggles of adolescence and young adulthood. Readers identified with his self-doubt and loneliness. Unlike previous teen heroes, Spider-Man was not a sidekick nor did he have a mentor. He would be given many supporting characters, such as his Daily Bugle boss J. Jonah Jameson; friends like Harry Osborn and Flash Thompson; romantic interests like Gwen Stacy, Mary Jane Watson, and the Black Cat; and enemies such as Doctor Octopus, the Green Goblin, and Venom. In his origin story, Peter gets his superhuman spider-powers and abilities after he was bitten by a radioactive spider. These powers include superhuman strength, speed, agility, reflexes and durability; clinging to surfaces and ceilings; and detecting danger with his precognitive "spider-sense". He sews a spider-web patterned spandex costume that fully covers his body and builds wrist-mounted "web-shooter" devices that shoot artificial spider-webs of his own design, which he uses for both fighting and "web swinging" across the city. Peter initially used his powers for personal gain, but after his Uncle Ben was killed by a burglar that he could have stopped but did not, he learned that "with great power comes great responsibility", and began to use his powers to fight crime as Spider-Man.

Marvel has featured Spider-Man in several comic book series, the first and longest-lasting of which is The Amazing Spider-Man. Since his introduction, the main-continuity version of Peter has gone from a high school student to attending college to currently being somewhere in his late 20s. Peter has been a member of numerous superhero teams, most notably the Avengers and Fantastic Four. Doctor Octopus also took on the identity for a story arc spanning 2012–2014 following the "Dying Wish" storyline, where Peter appears to die after Doctor Octopus orchestrates a body swap with him and becomes the Superior Spider-Man. Marvel has also published comic books featuring alternate versions of Spider-Man, including Spider-Man 2099, which features the adventures of Miguel O'Hara, the Spider-Man of the future; Ultimate Spider-Man, which features the adventures of a teenage Peter Parker in the alternate universe; and Ultimate Comics: Spider-Man, which depicts a teenager named Miles Morales who takes up the mantle of Spider-Man after Ultimate Peter Parker's apparent death. Miles later became a superhero in his own right and was brought into mainstream continuity during the Secret Wars event, where he sometimes works alongside the mainline version of Peter.

Spider-Man has appeared in countless forms of media, including several animated TV series, a live-action television series, syndicated newspaper comic strips, and multiple series of films. In live-action films, Spider-Man has been portrayed by Tobey Maguire in Sam Raimi's Spider-Man trilogy, Andrew Garfield in The Amazing Spider-Man duology directed by Marc Webb, and Tom Holland in the Marvel Cinematic Universe. The Peter Parker version of Spider-Man was also voiced by Jake Johnson and Chris Pine in the animated film Spider-Man: Into the Spider-Verse, with the former reprising his role in the sequel, Spider-Man: Across the Spider-Verse."""
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


# background.show()