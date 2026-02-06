# Text to Handwriting Converter (Python)

Convert typed text into realistic handwritten notes on notebook paper using Python. This project generates handwritten-style images and combines them into a multi‑page PDF automatically.

---

## ✨ Features

*  Converts text into handwritten style 
*  Uses notebook paper background
*  Proper line alignment with notebook lines
*  Human‑like randomness (per‑word variation)
*  Automatic word wrapping
*  Multi‑page support
*  Export all pages into a single PDF
*  Reads input from `.txt` file

---

## 📂 Project Structure

```
text_to_handwriting/
│
├── background/
│   └── background.jpeg
│
├── fonts/
│   └── QEDavidReidCAP.ttf
│
├── input/
│   └── input.txt
│
├── handwritten_notes.pdf
│
├── main.py
└── README.md
```

---

## ⚙️ Requirements

* Python 3.8 or newer
* Pillow library

Install dependency:

```bash
pip install pillow
```

---

## ▶️ How to Use

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/text-to-handwriting.git
cd text-to-handwriting
```

### 2. Activate virtual environment (optional but recommended)

Linux / Mac:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Add your text

Edit:

```
input/input.txt
```

Example:

```
Hello World
This is my handwritten notes project.
It converts text into realistic handwriting.
```

---

### 4. Run the program

```bash
python main.py
```

---

## 📤 Output

The program generates:

* Handwritten page images:

  ```
  output_page_1.png
  output_page_2.png
  ```

* Combined PDF:

  ```
  handwritten_notes.pdf
  ```

---

## 🧠 How It Works

1. Reads text from input file
2. Splits text into lines and words
3. Places words with slight randomness
4. Wraps text within page margins
5. Creates new pages automatically
6. Saves images and exports PDF

---

## 🎓 Learning Outcomes

This project demonstrates:

* Python file handling
* Image processing with Pillow
* Text rendering and layout
* Multi‑page document generation
* PDF export automation

##
