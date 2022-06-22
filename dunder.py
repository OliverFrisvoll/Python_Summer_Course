# Created by ocfri at 20/06/2022
import logging
import numpy as np
import itertools

logging.basicConfig(
    format="%(levelname)s %(asctime)s - %(message)s",
    datefmt="%d-%m-%Y %H:%M:%S",
    level=logging.DEBUG,
)


def closest_pair(points):
    combinations = list(itertools.combinations(points, 2))

    def distance(pair):
        x, y = pair
        return np.linalg.norm(np.array(x) - np.array(y))

    lengths = [distance(pair) for pair in combinations]
    min_index = lengths.index(min(lengths))

    return combinations[min_index]


def mix(s1, s2):
    def split(string):
        return [char for char in string if char.islower()]

    def counter(word_list):
        counts = dict()
        for char in word_list:
            counts[char] = counts.get(char, 0) + 1
        return counts

    s1, s2 = split(s1), split(s2)

    unique = list(set(s1 + s2))

    s1_count, s2_count = counter(s1), counter(s2)

    highest_amount = {}

    for key in unique:
        if key in s1_count and key in s2_count:
            highest_amount[key] = max(s1_count[key], s2_count[key])

    letter_multiples = [highest_amount[key] * key for key in highest_amount if highest_amount[key] > 1]
    letter_multiples.sort()
    letter_multiples.sort(reverse=True, key=len)

    def key_picker(l_string):
        key = l_string[0]
        s1, s2 = s1_count[key], s2_count[key]

        if s1 == s2:
            return f"=:{l_string}"

        elif s1 > s2:
            return f"1:{l_string}"

        else:
            return f"2:{l_string}"

    lst, last_run, answer = [], 0, []

    sort_order = {"2": 0, "1": 1, "=": 2}

    for letters in letter_multiples:
        if len(letters) == last_run:
            lst.append(key_picker(letters))

        elif not lst:
            lst.append(key_picker(letters))

        else:
            answer += lst.sort(reverse=False, key=lambda val: sort_order[val.split(':')[0]])
            lst = [key_picker(letters)]

        last_run = len(letters)

    answer += lst.sort(key=lambda val: sort_order[val.split(':')[0]])

    return '/'.join(answer)


def solution(digits):
    digits = str(digits)
    lst = []
    for n in range(len(digits) - 4):
        lst.append(digits[n:n + 5])

    return max(lst)


def main():
    print(solution(3234242242))


if __name__ == "__main__":
    main()
