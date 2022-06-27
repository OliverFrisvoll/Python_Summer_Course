# Created by ocfri at 22/06/2022
import logging


def currency_swap_1():
    NOK_EUR = 10.40
    amount = int(input("Amount of money to exchange (in NOK): "))
    print(f"{amount} NOK equals {amount / NOK_EUR} EUR")


def currency_swap_2_3():
    NOK_EUR = 10.40
    text = input("Amount of money to exchange (i.e. 100 NOK, 400 EUR...) ").upper()
    try:
        amount = int(text.split(" ")[0])
        if text.endswith("NOK"):
            print(f"{amount} NOK equals {amount / NOK_EUR:.2f} EUR")
        elif text.endswith("EUR"):
            print(f"{amount} EUR equals {amount * NOK_EUR:.2f} NOK")
        else:
            print(
                f" --- We currently do not support {text.split(' ')[1]}, please try NOK or EUR --- "
            )
    except ValueError:
        print(
            f' --- We currently do not support {text}, please try the format "amount currency" i.e: 200 NOK --- '
        )

    except IndexError:
        print(
            f' --- You need to supply a currency, (i.e. 100 NOK, 400 EUR...) --- '
        )

    if input("Try again? (Y/N): ") == "Y":
        currency_swap_2_3()


def currency_swap_4():
    exchange_rates = {
        "NOK/EUR": 1 / 10.40,
        "NOK/USD": 1 / 9.91,
    }

    temp_dict = {}
    for key in exchange_rates:
        currencies = key.split("/")
        currencies.reverse()
        temp_dict["/".join(currencies)] = 1 / exchange_rates[key]

    exchange_rates.update(temp_dict)
    rate: str = ""
    while rate not in list(exchange_rates):
        rate = input(
            f"Available rates: {' '.join(list(exchange_rates))}\nWhich exchange rate? "
        ).upper()
        if rate not in list(exchange_rates):
            print(
                f" --- We currently do not support {rate}, please try a rate from the list --- "
            )

    amount = float(input(f"Amount of money to exchange: "))
    print(
        f"{amount} {rate.split('/')[0]} equals {exchange_rates[rate] * amount:.2f} {rate.split('/')[1]}"
    )

    if input("Try another? (Y/N): ") == "Y":
        currency_swap_4()


def main():
    # currency_swap_1()
    currency_swap_2_3()
    # currency_swap_4()


if __name__ == "__main__":
    main()
