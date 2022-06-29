# Created by ocfri at 28/06/2022
import re

FILE_NAME = "data/words.txt"


def read_file(file):
    with open(file, "r") as f:
        return f.read()


def repeated_words(text):
    words = re.findall(r"\w+", text.lower())
    prev_word = ""
    for word in words:
        if prev_word == word:
            return True
        prev_word = word
    return False


def main():
    text = read_file(FILE_NAME).split()
    text_set = set(text)
    palindromes = [word for word in text if word == word[::-1]]
    anadromes = [word for word in text if word[::-1] in text_set]
    anadromes = [word for word in anadromes if word not in palindromes]
    print(f"{palindromes = }")
    print(f"{anadromes = }")

    vowel = len(re.findall("[aeiouy]", read_file(FILE_NAME)))
    consonant = len([letter for word in text for letter in word if letter not in "aeiouy"])
    print(f"{vowel = }")
    print(f"{consonant = }")

    print(repeated_words("Test test string string test what is a test"))



if __name__ == '__main__':
    main()
