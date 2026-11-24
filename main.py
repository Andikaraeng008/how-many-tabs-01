import os

TEXT = "137"


def main():
    assert TEXT.isdigit() and 1 <= len(TEXT) <= 5
    assert TEXT.strip() == TEXT and TEXT == TEXT.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
