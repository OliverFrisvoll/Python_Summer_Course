# Created by ocfri at 27/06/2022
from collections import Counter


def exercise_1(number: int):
    return sum(int(x) for x in str(number))


class Exercise2:
    def __init__(self, file_location: str):
        self.file_location = file_location

    def _open_file(self):
        with open(self.file_location, 'r') as f:
            return f.read()

    def get_words(self):
        return len(self._open_file().split())

    def get_unique_words(self):
        return len(set(self._open_file().split()))

    def get_most_frequent_words(self, number: int = 1):
        return Counter(self._open_file().split()).most_common(number)


def main():
    # Exercise 1
    print(exercise_1(12))

    # Exercise 2
    shake_spear = Exercise2('data/shakespeare_sonnets.txt')
    print(f"Words in text: {shake_spear.get_words()}")
    print(f"Unique words in text: {shake_spear.get_unique_words()}")
    print(f"Most frequent word in the text: {shake_spear.get_most_frequent_words()[0][0]}")
    print(f"3 most frequent words in the text: {shake_spear.get_most_frequent_words(3)}")


if __name__ == '__main__':
    main()
