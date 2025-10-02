import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import string


###  Constants

### Window size
WINDOW_HEIGHT = 350
WINDOW_WIDTH = 500

### Padding
PAD_X = 10
PAD_Y = 10

### Title label size
TITLE_LABEL_HEIGHT = 2
TITLE_LABEL_WIDTH = 20

### Input label size
INPUT_LABEL_HEIGHT = 1
INPUT_LABEL_WIDTH = 30

### Input entry size
INPUT_ENTRY_WIDTH = 30
INPUT_ENTRY_HEIGHT = 2

### Generate button size
GENERATE_BUTTON_WIDTH = 20
GENERATE_BUTTON_HEIGHT = 2

### Output entry size
OUTPUT_ENTRY_WIDTH = 30
OUTPUT_ENTRY_HEIGHT = 2


###  Functions

def check_input_string():
    input_value = input_entry.get()  ### Get text from input Entry

    if len(input_value) != 6:
        messagebox.showerror("Invalid Input", "Please enter exactly 6 digits.")
        return

    if not input_value.isdigit():
        messagebox.showerror("Invalid Input", "Input must contain only digits (0-9).")
        return

    generate_key(input_value)


def generate_block_5(digits_part):
    ### Takes 3 digits, adds 2 random letters and returns 5-character block
    letters = ''.join(random.choices(string.ascii_uppercase, k=2))
    return digits_part + letters


def generate_key(input_value):
    ### Create blocks and add them to each other
    digits_part1 = ''.join(random.sample(input_value[3:6], 3))
    digits_part2 = ''.join(random.sample(input_value[0:3], 3))

    block1 = generate_block_5(digits_part1)
    block2 = generate_block_5(digits_part2)

    sum_numeric = int(digits_part1) + int(digits_part2)
    block3 = str(sum_numeric).zfill(4)[-4:]

    final_key = f"{block1}-{block2} {block3}"

    key_entry.config(state="normal")
    key_entry.delete(0, tk.END)
    key_entry.insert(0, final_key)
    key_entry.config(state="readonly")


###  GUI
root = tk.Tk()
root.title("Key Generator")
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

### Load background image
background_image = Image.open("DarkestDungeon2Image.png")  ### Nicely seen in full window mode
background_photo = ImageTk.PhotoImage(background_image)

### Create background label
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
background_label.image = background_photo  ### Keep reference

### Create main frame over the background
main_frame = tk.Frame(root)
main_frame.place(relx=0.5, rely=0.5, anchor="center")

### Title label
title_label = tk.Label(
    main_frame,
    text="KeyGenerator",
    height=TITLE_LABEL_HEIGHT,
    width=TITLE_LABEL_WIDTH,
    font=("Segoe UI", 16, "bold")
)
title_label.pack(side=tk.TOP, pady=PAD_Y)

### Input label
input_label = tk.Label(
    main_frame,
    text="Enter 6-digit InputPart:",
    height=INPUT_LABEL_HEIGHT,
    width=INPUT_LABEL_WIDTH
)
input_label.pack(side=tk.TOP, anchor="w", padx=PAD_X, pady=PAD_Y)

### Input field
input_frame = tk.Frame(main_frame)
input_frame.pack(side=tk.TOP, fill=tk.X, padx=PAD_X, pady=PAD_Y)

input_entry = tk.Entry(input_frame, width=INPUT_ENTRY_WIDTH, font=("Arial", 12))
input_entry.pack(side=tk.LEFT, padx=PAD_X, ipady=INPUT_ENTRY_HEIGHT)

### Button
generate_button = tk.Button(
    input_frame,
    text="Generate new key",
    width=GENERATE_BUTTON_WIDTH,
    height=GENERATE_BUTTON_HEIGHT,
    command=check_input_string
)
generate_button.pack(side=tk.RIGHT, padx=PAD_X)

### Output field for generated key
key_entry = tk.Entry(
    main_frame,
    width=OUTPUT_ENTRY_WIDTH,
    font=("Arial", 12),
    state="readonly"
)
key_entry.pack(side=tk.TOP, padx=PAD_X, pady=PAD_Y, ipady=OUTPUT_ENTRY_HEIGHT)


### Mainloop
root.mainloop()
