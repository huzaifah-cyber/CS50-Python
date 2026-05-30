import sys
import requests

if not len(sys.argv) == 2:
    sys.exit("Missing command-line argument")

try:
    multiplier  = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get(
        "https://rest.coincap.io/v3/assets/bitcoin?apiKey=93649dd31aac1b9526282b6107c0a8a48909b058fb2b85d49ad57b9ccd5160b9"
    ).json()

    bitcoin = float(response["data"]["priceUsd"])
    print(f"${bitcoin * multiplier :,.4f}")

except requests.RequestException:
    print("Request failed")