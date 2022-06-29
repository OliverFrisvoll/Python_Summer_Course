# Created by ocfri at 29/06/2022
import random


def value_checker(guess, answer):
    fermi = [x == z for x, z in zip(guess, answer)]
    pico = [x in answer and fermi[i] is False for i, x in enumerate(guess)]

    if guess == answer:
        return "Correct Answer"
    text = "Fermi " * sum(fermi) + "Pico " * sum(pico)
    if text == "":
        return "Bagels"
    else:
        return text


def play_game(rounds=10):
    answer = str(random.randint(100, 1000))

    for attempt in range(rounds + 1):
        guess = input(f"Guess #{attempt + 1}: ")
        result = value_checker(guess, answer)
        if result == "Correct Answer!":
            print(result)
            break
        else:
            print(result)

    print(f"You failed, the correct answer was: {answer}")

    if input("Play again? (Y/N)") == "Y":
        play_game()


def main():
    play_game()


if __name__ == '__main__':
    main()
