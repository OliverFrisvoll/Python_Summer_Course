# Created by ocfri at 27/06/2022
from collections import Counter


# Exercise 1
def stats(string: str):
    done_letters = []
    for letters in string:
        if letters not in done_letters:
            print(f"{letters} | {string.count(letters)} times(s)")
            done_letters.append(letters)


# Exercise 1: Extra challenge
def stats_adv(string: str):
    Counter(string).most_common()
    for letters, times in Counter(string).most_common():
        print(f"{letters} | {times} times(s)")


def main():
    print("\nExercise 1:")
    stats("banana")

    print("\nExercise 1: Extra challenge")
    stats_adv("banana")


if __name__ == '__main__':
    main()
