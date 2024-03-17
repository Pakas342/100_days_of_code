from bs4 import BeautifulSoup
import requests
import re


def scrapper(url):
    """Goes to the specified url and retrieves a list of  dictionaries per property with address price and link"""

    # Obtains the info about the website and create a beautiful soup
    website = requests.get(url).text
    soup = BeautifulSoup(website, "html.parser")

    # Create lists for links, prices and address using list comprehension
    links = [link.get("href") for link in soup.find_all(name="a", class_="property-card-link")]

    # For prices, we need to do some data transformation with a regex
    # This part creates a pattern that only picks anything that's not (^ symbol) a digit (\d symbol)
    pattern = re.compile(r'[^\d]+')
    prices_class_html = "PropertyCardWrapper__StyledPriceLine"
    raw_prices = [price.getText() for price in soup.find_all(name="span", class_=prices_class_html)]
    prices = [int(re.sub(pattern, "", price)) for price in raw_prices]

    addresses = [address.getText().strip() for address in soup.find_all(name="address")]

    # We use list comprehension for the final data
    final_data = [{"address": address, "price": price, "link": link} for address, price, link in
                  zip(addresses, prices, links)]

    return final_data
