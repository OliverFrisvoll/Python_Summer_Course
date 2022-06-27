# Created by ocfri at 27/06/2022
import logging


def hamming(n):
    result = [1]
    ind2 = ind3 = ind5 = 0
    count = 1
    while n > count:
        add = min(result[ind2] * 2, result[ind3] * 3, result[ind5] * 5)
        if add == result[ind2] * 2:
            ind2 += 1
        if add == result[ind3] * 3:
            ind3 += 1
        if add == result[ind5] * 5:
            ind5 += 1
        count += 1
        result.append(add)
    return result[-1]


def main():
    print(hamming(323))


if __name__ == '__main__':
    main()
