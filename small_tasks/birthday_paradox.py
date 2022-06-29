# Created by ocfri at 29/06/2022
import numpy as np


def main():
    trials = 100000
    random_array = np.random.default_rng().uniform(1, 365, (23, trials))
    random_array = random_array.astype(int)
    double_birthday = 0
    for trial in range(trials):
        if len(set(random_array[:, trial])) != len((random_array[:, trial])):
            double_birthday += 1
    print(f"Answer: {double_birthday / trials}")


if __name__ == '__main__':
    main()
