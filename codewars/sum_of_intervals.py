# Created by ocfri at 21/06/2022
import itertools
import functools
import operator


def sum_of_intervals(intervals):
    comb = itertools.combinations(intervals, 2)
    pair = [x for x in comb if x[0][1] > x[1][0] > x[0][0]]
    flatten = functools.reduce(operator.iconcat, pair, [])
    print(flatten)
    # return max(flatten) - min(flatten)


def main():
    print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]))


if __name__ == '__main__':
    main()
