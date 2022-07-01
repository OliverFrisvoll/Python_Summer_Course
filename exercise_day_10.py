# Created by ocfri at 30/06/2022
import numpy as np


def birthday_paradox(trials: int = 100000):
    people = 23
    double_birthdays = 0
    random_num = np.random.randint(1, 365 + 1, (trials, people))
    for row in random_num:
        if len(set(row)) < people:
            double_birthdays += 1
    print(f"Answer {double_birthdays / trials: .4f}")


def generate_number(digits=4):
    return str(np.random.randint(10 ** (digits - 1), 10 ** digits))


def no_duplicated_digits(number):
    return len(set(number)) == len(number)


def game(rounds: int = 10):
    while True:
        secret = generate_number()
        if no_duplicated_digits(secret):
            break

    for x in range(10):
        guess = input(f"Attempt: {x + 1} Guess number: ")
        if guess == secret:
            print("You won!")
            return 0

        bulls = [g_digit for g_digit, s_digit in zip(guess, secret) if g_digit == s_digit]
        bulls_amount = len(bulls)
        cows = [digit for digit in guess if digit in secret and digit not in bulls]
        cows_amount = len(cows)
        print(f" Bulls: {bulls_amount}, Cows: {cows_amount}")

    print(f"You failed, the secret was: {secret}")


def main():
    birthday_paradox()
    game()


if __name__ == "__main__":
    main()
