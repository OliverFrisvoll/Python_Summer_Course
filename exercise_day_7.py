# Created by ocfri at 28/06/2022
from collections import Counter

TEXT_FILE = "data/shakespeare_sonnets.txt"


def clean(text):
    text = text.lower().split()
    return [x.strip("?,.'!;:") for x in text]


class Exercise2:
    def __init__(self, file):
        self._file = file

    def _read_file(self):
        with open(self._file, "r") as f:
            return f.read()

    def count_words(self):
        return len(self._read_file().split())

    def uniques(self):
        return len(set(clean(self._read_file())))

    def frequency(self):
        return Counter(clean(self._read_file())).most_common()


def main():
    sp = Exercise2(TEXT_FILE)
    print(f"{sp.count_words() = }")
    print(f"{sp.uniques() = }")
    print(f"{sp.frequency()[0][0] = }")
    print(f"{sp.frequency()[0:3] = }")


if __name__ == "__main__":
    main()
