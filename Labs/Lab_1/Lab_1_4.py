import time


### Task 4
### Build percentage distribution of numbers from file sequence.txt

GREEN = "\033[42m \033[0m"  ### green block
RED = "\033[41m \033[0m"    ### red block


### Load numbers from file
def load_numbers(filename="sequence.txt"):
    with open(filename, "r", encoding="utf-8") as f:
        numbers = [float(line.strip()) for line in f if line.strip()]
    return numbers


### Static chart (2 categories: [-3;3] and others)
def print_static_chart(numbers):
    in_range = sum(1 for x in numbers if -3 <= x <= 3)
    out_range = len(numbers) - in_range
    total = len(numbers)

    in_percent = in_range / total * 100
    out_percent = out_range / total * 100

    max_blocks = 50
    in_blocks = int(round(in_percent / 100 * max_blocks))
    out_blocks = int(round(out_percent / 100 * max_blocks))

    print("Distribution of numbers (2 categories):\n")
    print("[-3; 3]      | " + GREEN * in_blocks + f" {in_percent:.2f}%")
    print("Out of range | " + RED * out_blocks + f" {out_percent:.2f}%")
    print()


### Animated chart (3 categories: < -3, [-3;3], > 3)
def print_animated_chart(numbers):
    less_range = sum(1 for x in numbers if x < -3)
    in_range = sum(1 for x in numbers if -3 <= x <= 3)
    greater_range = sum(1 for x in numbers if x > 3)
    total = len(numbers)

    less_percent = less_range / total * 100
    in_percent = in_range / total * 100
    greater_percent = greater_range / total * 100

    max_blocks = 100
    less_blocks = int(round(less_percent / 100 * max_blocks))
    in_blocks = int(round(in_percent / 100 * max_blocks))
    greater_blocks = max_blocks - less_blocks - in_blocks

    segments = [
        (RED, less_blocks, f"< -3 ({less_percent:.1f}%)"),
        (GREEN, in_blocks, f"[-3;3] ({in_percent:.1f}%)"),
        (RED, greater_blocks, f"> 3 ({greater_percent:.1f}%)")
    ]

    print("Distribution of numbers (3 categories):\n")

    line = ""
    for color, blocks, label in segments:
        for i in range(blocks):
            line += color
            print("\r" + line, end="", flush=True)
            time.sleep(0.1)  # animation speed

    print()  ### New line after animation

    labels_line = ""
    pos = 0
    for i, blocks, label in segments:
        labels_line += " " * (pos - len(labels_line)) + label
        pos += blocks
    print(labels_line)
    print()


### Main body of program
if __name__ == "__main__":
    numbers = load_numbers("sequence.txt")
    print_static_chart(numbers)
    print_animated_chart(numbers)

