import requests


def get_exchange_rate(base_currency, target_currency):
    url = (
        f"https://api.frankfurter.app/latest"
        f"?from={base_currency}&to={target_currency}"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()

    if target_currency not in data["rates"]:
        return None

    return data["rates"][target_currency]


def convert_currency(amount, exchange_rate):
    return amount * exchange_rate


def main():
    print("===== CURRENCY CONVERTER =====")

    try:
        amount = float(input("Enter amount: "))

        base_currency = input(
            "Enter source currency (e.g. USD): "
        ).upper()

        target_currency = input(
            "Enter target currency (e.g. INR): "
        ).upper()

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        if base_currency == target_currency:
            print("Source and target currencies cannot be the same.")
            return

        print("\nFetching exchange rate...")

        exchange_rate = get_exchange_rate(
            base_currency,
            target_currency
        )

        if exchange_rate is None:
            print("Unable to get the exchange rate.")
            print("Please check the currency codes or your internet connection.")
            return

        converted_amount = convert_currency(
            amount,
            exchange_rate
        )

        print("\n----- RESULT -----")
        print(
            f"{amount:.2f} {base_currency} = "
            f"{converted_amount:.2f} {target_currency}"
        )
        print(f"Exchange rate: 1 {base_currency} = "
              f"{exchange_rate:.4f} {target_currency}")

    except ValueError:
        print("Please enter a valid numeric amount.")

    except requests.exceptions.RequestException:
        print("Unable to connect to the exchange-rate API.")


if __name__ == "__main__":
    main()
