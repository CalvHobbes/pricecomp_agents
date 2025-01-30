import requests
import json

# Function to fetch prices from Croma
def fetch_prices_from_croma(product):
    """Searches for the product on Croma and returns the name, url and price of the product.
  """
    url = f"https://api.croma.com/searchservices/v1/search?query={product}:relevance&channel=WEB"
    headers = {
        "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"macOS\"",
        "dnt": "1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "sec-fetch-site": "none",
        "sec-fetch-mode": "navigate",
        "sec-fetch-user": "?1",
        "sec-fetch-dest": "document",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-GB,en;q=0.9",
        "priority": "u=0, i",
        "origin": "https://www.croma.com",
        "referer": "https://www.croma.com/"
    }
    response = requests.get(url, headers=headers, timeout=300, verify=True) # set to False when using proxy like Charles
    response.raise_for_status()
    data = response.json()
    
    products = data.get('products', [])
    product_list = [
        {
            'name': product['name'],
            'url': 'https://www.croma.com' + product['url'],
            'price': product['price']['value']
        }
        for product in products
    ]
    return product_list

# Example usage
query = "sony bravia"
prices = fetch_prices_from_croma(query)
print(json.dumps(prices, indent=4))
