# Created by ocfri at 28/06/2022
from collections import Counter

TEXT_FILE = "data/shakespeare_sonnets.txt"


def read_file(file):
    with open(file, "r") as f:
        return f.read()


def clean(text):
    text = text.lower().split()
    return [x.strip("?,.'!;:") for x in text]


def count_words(file):
    return len(read_file(file).split())


def uniques(file):
    return len(set(clean(read_file(file))))


def frequency(file):
    return Counter(clean(read_file(file))).most_common()


def main():
    print(f"{count_words(TEXT_FILE) = }")
    print(f"{uniques(TEXT_FILE) = }")
    print(f"{frequency(TEXT_FILE)[0][0] = }")
    print(f"{frequency(TEXT_FILE)[0:3] = }")


if __name__ == "__main__":
    main()
