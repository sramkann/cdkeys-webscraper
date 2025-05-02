from urls import URLS_TO_BE_SCRAPED
from bs4 import BeautifulSoup
import requests
import pandas

columns = ["Item Name", "CDKeys Price (SG$)", "Recommended Sale Price (SG$)",  "Stock Status"]

df = pandas.DataFrame(columns=columns)

for url in URLS_TO_BE_SCRAPED:
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    product_name = soup.find('div', class_ = "page-title-wrapper product").text.strip()
    product_price = soup.find('span', class_ = "price").text.strip()
    stock_status = soup.find('div', class_ = "product-usps-text").text.strip()
    recommended_sale_price = "$" + str(round(float(product_price.strip("$")) + float(product_price.strip("$")) * 0.30, 2))
    product_data = [product_name, product_price, recommended_sale_price, stock_status]
    length = len(df)
    df.loc[length] = product_data

df.to_csv(r'cdkey_product_price_catalogue.csv', index=False)

