import requests

def get_exchange_rate(source_currency, target_currency):
    api_key = "7741c2f0d3c5e08091979ad3"  # Replace with your API key
    url = f"https://open.er-api.com/v6/latest/{source_currency}"
    response = requests.get(url)
    
    if response.status_code == 200:
        rates = response.json()["rates"]
        exchange_rate = rates.get(target_currency)
        return exchange_rate
    else:
        print(f"Error: {response.status_code}")
        return None

def convert_currency():
    source_currency = input("Enter source currency: ").upper()
    target_currency = input("Enter target currency: ").upper()
    amount = float(input("Enter amount to convert: "))

    exchange_rate = get_exchange_rate(source_currency, target_currency)

    if exchange_rate is not None:
        converted_amount = amount * exchange_rate
        print(f"{amount} {source_currency} is equal to {converted_amount:.2f} {target_currency}")

def main():
    print("\nCurrency Converter")
    convert_currency()

if __name__ == "__main__":
    main()
