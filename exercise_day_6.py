# Created by ocfri at 27/06/2022


def exercise_1(number: int):
    return sum(int(x) for x in str(number))


def main():
    # Exercise 1
    print(exercise_1(12))


if __name__ == '__main__':
    main()
