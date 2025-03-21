import requests

def get_mexc_listings():
    url = "https://www.mexc.com/open/api/v2/market/coin/list"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return [coin['symbol'] for coin in data['data']]
    return []

if __name__ == "__main__":
    listings = get_mexc_listings()
    print("MEXC New Listings:", listings)
