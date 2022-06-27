# Created by ocfri at 27/06/2022
import logging


class RomanNumerals:
    dict_roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    dict_numerals = {v: k for k, v in dict_roman.items()}

    # Convert an integer to a roman numeral using dict_roman
    def to_roman(self, number) -> str:
        answer_int: int = 0
        answer_str: str = ""
        answer_int = min(self.dict_numerals, key=lambda k: abs(k - number))
        answer_str = self.dict_numerals[answer_int]

        while answer_int != number:
            num = min(self.dict_numerals, key=lambda k: abs(k - abs(number - answer_int)))
            if answer_int > number:
                answer_str = self.dict_numerals[num] + answer_str
                answer_int -= num
            else:
                answer_str = answer_str + self.dict_numerals[num]
                answer_int += num

        print(f"{answer_int = } {answer_str = }")
        return answer_str

    def from_roman(self, roman_num):
        roman_num = [self.dict_roman[num] for num in list(roman_num)]
        roman_index = roman_num.index(max(roman_num))
        if roman_index == 0:
            return roman_num[0] + sum(roman_num[roman_index + 1:])
        else:
            return roman_num[-1] - sum(roman_num[:roman_index])


def main():
    RomanNumerals().to_roman(1990)
    print(RomanNumerals().from_roman("VII"))


if __name__ == '__main__':
    main()
