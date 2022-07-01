# Created by ocfri at 01/07/2022
import logging


def birth_day_paradox(people: int, trials: int = 100000):
    random_array = np.random.randint(1, 365 + 1, (trials, people))
    double_birthday = 0
    for row in random_array:
        if len(set(row)) != people:
            double_birthday += 1
    print(f"Answer: {(double_birthday / trials) * 100: .2f}%")


def main():
    pass


if __name__ == '__main__':
    main()
