import requests

def get_exchange_rates(base_currency="USD"):
    """Fetch live exchange rates from the European Central Bank (no API key needed)."""
    url = f"https://api.exchangerate.host/latest?base={base_currency}"
    response = requests.get(url)
    data = response.json()
    return data["rates"]

def convert_currency(amount, from_currency, to_currency):
    """Convert an amount from one currency to another."""
    rates = get_exchange_rates(from_currency.upper())
    if to_currency.upper() not in rates:
        raise ValueError("Invalid target currency.")
    converted_amount = amount * rates[to_currency.upper()]
    return round(converted_amount, 2)

if __name__ == "__main__":
    print("💱 Simple Currency Converter")
    try:
        amount = float(input("Enter amount: "))
        from_currency = input("From currency (e.g., USD): ").upper()
        to_currency = input("To currency (e.g., EUR): ").upper()

        result = convert_currency(amount, from_currency, to_currency)
        print(f"{amount} {from_currency} = {result} {to_currency}")

    except Exception as e:
        print("Error:", e)
