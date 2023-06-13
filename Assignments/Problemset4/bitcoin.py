import requests
import sys

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

res_ = response.json()

try:
    n = int(sys.argv[1])
    rate = res_["bpi"]["USD"]["rate_float"]
    print(rate)
except(requests.RequestException):
    sys.exit("Cannot be a Float")

cost = n * rate
print(f"Cost: {cost:,}")