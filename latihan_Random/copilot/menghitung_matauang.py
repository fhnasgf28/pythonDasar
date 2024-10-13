import requests
import json

BASE_URL = 'https://api.exchangerate-api.com/v4/latest/USD'


def get_exchange_rates():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency != 'USD':
        amount = amount / rates['rates'][from_currency]
    return amount * rates['rates'][to_currency]


def main():
    rates = get_exchange_rates()
    if rates:
        amount = float(input("Enter amount in USD:"))
        currency = input("Enter target currency (e.g., EUR, JPY)")
        converted_amount = convert_currency(amount, 'USD', currency, rates)
        print(f"{amount} USD is equivalent to {converted_amount} {currency}")

        # Store results in JSON
        data = {'amount': amount, 'currency': currency, 'converted_amount': converted_amount}
        with open('finance_results.json', 'w') as json_file:
            json.dump(data, json_file)

        print("Results saved to finance_results.json")

if __name__ == "__main__":
    main()