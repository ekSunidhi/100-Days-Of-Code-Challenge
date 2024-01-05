# Import all the necessary packages
import requests
from bs4 import BeautifulSoup
import json

# Set the URL that is to be scrapped
url='https://www.cdkeys.com/pc'

# Make a response and parse the response as HTML
response=requests.get(url)
soup=BeautifulSoup(response.content, 'html.parser')

# Select the data that you are interested in extracting from the page
oldPrices=soup.select('span[data-price-type="oldPrice"] span')
products=soup.select('li.product-item')

# Loop through each of the products and extract the data that we need
for i in range(len(products)):
    # Convert the data in the html attributes to json
    prod=json.loads(products[i]['data-impression'])
    
    # Print the product information
    print(f"{prod['name']} - ${prod['price']} - {oldPrices[i].text}")
