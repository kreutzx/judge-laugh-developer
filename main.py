import os

LINE = "It works on my machine. It also works on Kevin's machine. Kevin quit in March — we now deploy exclusively to Kevin's machine."


def main():
    # One-line developer excuse, written to the entry file for judging.
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    text = LINE + "\n"
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
