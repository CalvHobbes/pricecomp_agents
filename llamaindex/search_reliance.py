import requests
import json
from bs4 import BeautifulSoup

# Function to fetch prices from Reliance Digital
def fetch_prices_from_reliance(product):
    """Searches for the product on Reliance Digital and returns the name, url and price of the product."""
    url = f"https://www.reliancedigital.in/search?q={product}:relevance"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        "origin": "https://www.reliancedigital.in",
        "referer": "https://www.reliancedigital.in/"
    }
    response = requests.get(url, headers=headers, timeout=300, verify=True)# set to False when using proxy like Charles
    response.raise_for_status()
    data = response.text
    
    # Parse the HTML content
    soup = BeautifulSoup(data, 'html.parser')
    
    # Extract product details
    products = soup.select('.sp.grid')
    product_list = [
        {
            'name': product.select_one('.sp__name').get_text(strip=True),
            'url': 'https://www.reliancedigital.in' + product.select_one('a[attr-tag="anchor"]')['href'],
            'price': product.select_one('.StyledPriceBoxM__PriceWrapper-sc-1l9ms6f-0 span > span:nth-of-type(2)').get_text(strip=True)
        }
        for product in products
    ]
    return product_list

# Example usage
# query = "sony bravia"
# prices = fetch_prices_from_reliance(query)
# print(json.dumps(prices, indent=4))
