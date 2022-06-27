import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def fibonacci_nth_step(steps):
    if steps == 0:
        return 0
    elif steps == 1:
        return 1
    else:
        return fibonacci_nth_step(steps - 1) + fibonacci_nth_step(steps - 2)


def main():
    logging.info(f"{fibonacci_nth_step(10) = }")


if __name__ == "__main__":
    main()
