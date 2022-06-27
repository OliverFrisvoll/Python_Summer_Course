# Created by ocfri at 22/06/2022

# Exercise 1:
def dashes():
    name = input("Enter your name: ")
    print(f"HELLO, {'-'.join(name.upper())}!")


def main():
    dashes()


if __name__ == '__main__':
    main()
