import requests
from lxml import html 


asin = 'B00737M29A'

amazon_url  = 'http://www.amazon.in/dp/'+asin
	# Add some recent user agent to prevent amazon from blocking the request 
	# Find some chrome user agent strings  here https://udger.com/resources/ua-list/browser-detail?browser=Chrome
headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19'}
page = requests.get(amazon_url,headers = headers,verify=False)
page_response = page.text

parser = html.fromstring(page_response)
XPATH_PRODUCT_NAME = '//h1//span[@id="productTitle"]//text()'
XPATH_PRODUCT_PRICE  = '//span[@id="priceblock_ourprice"]/text()'

raw_product_price = parser.xpath(XPATH_PRODUCT_PRICE)
product_price = ''.join(raw_product_price).replace(',','')

raw_product_name = parser.xpath(XPATH_PRODUCT_NAME)
product_name = ''.join(raw_product_name).strip()

print(product_price, product_name)