# Created by ocfri at 22/06/2022
import logging


exchange_rates = {
    "NOK/EUR": 1 / 10.40,
    "NOK/USD": 1 / 9.91,
}


def currency_swap():
    des: int = 2
    temp_dict = {}
    for key in exchange_rates:
        currencies = key.split("/")
        currencies.reverse()
        temp_dict["/".join(currencies)] = round(1 / exchange_rates[key], des)

    exchange_rates.update(temp_dict)
    rate: str = ""
    while rate not in list(exchange_rates):
        rate = input(f"Available rates: {' '.join(list(exchange_rates))}\nWhich exchange rate? ")
        if rate not in list(exchange_rates):
            print(f" --- We currently do not support {rate}, please try a rate from the list --- ")

    amount = round(float(input(f"Amount of money to exchange: ")), des)
    print(f"{amount} {rate.split('/')[0]} equals {round(exchange_rates[rate] * amount, des)} {rate.split('/')[1]}")

    if input("Try another? (Y/N): ") == "Y":
        currency_swap()


def main():
    currency_swap()


if __name__ == '__main__':
    main()
