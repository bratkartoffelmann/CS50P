import requests
import sys

# Check command line argument
if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")
elif len(sys.argv) != 2:
    sys.exit("Invalid command-line argument")


def main(value = sys.argv[1]):
    # Cast argument into int
    try:
        value = float(value)
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # Get request
    try:
        data = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = data.json()
    except requests.RequestException:
        sys.exit("Error in fetching request")

    rate_USD = data["bpi"]["USD"]["rate_float"]
    amount = value * rate_USD
    print(f"${amount:,.4f}")

main()