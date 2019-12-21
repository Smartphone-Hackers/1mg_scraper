import requests
import re
from bs4 import BeautifulSoup

url = input("Enter Medicine URL : ")
user_agent = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"}
r = requests.get(url, headers=user_agent).text
soup = BeautifulSoup(r, "lxml")
product_name = soup.find("h1", {"class":"ProductTitle__product-title___3QMYH"})
product_price = soup.find("div", {"class":"PriceDetails__discount-div___nb724"})
no_product = soup.find("div", {"class":"Dropdown__display-text___15dWa"})
piece_product = soup.find("div", {"class":"PackSizeLabel__single-packsize___3KEr_"})
product_manufactured = soup.find("div", {"class":"OtcPage__manufacturer-address___3ugdE"})
medicine_info = soup.find("div", {"class":"ProductDescription__description-content___A_qCZ"})
medicine_desc = ""

if product_name is None:
    product_name = ""
else:
    product_name = "Product Name :\n" + "-"*len("Product Name :")+ "\n" + "\t" + str(product_name.text) + "\n"

if product_price is None:
    product_price = ""
else:
    product_price = "Product Price :\n" + "-"*len("Product Price :")+ "\n" + "\t" + str(product_price.text) + "\n"

if no_product is None and piece_product is None:
    no_product, piece_product = "", ""
    product_quantity = "Product Quantity :\n" + "-"*len("Product Quantity :")+ "\n" + "\n"
elif no_product is not None and piece_product is not None:
    product_quantity = "Product Quantity :\n" + "-"*len("Product Quantity :") + "\n" +  "\t" + str(no_product.text) + str(piece_product.text) + "\n"
elif no_product is None:
    product_quantity = "Product Quantity :\n" + "-"*len("Product Quantity :") + "\n" +  "\t" + str(piece_product.text) + "\n"
elif piece_product is None:
    product_quantity = "Product Quantity :\n" + "-"*len("Product Quantity :") + "\n" +  "\t" + str(no_product.text) + "\n"

if product_manufactured is None:
    product_manufactured = ""
else:
    product_manufactured = "Product Manufactured :\n" + "-"*len("Product Manufactured :") + "\n" + product_manufactured.text + "\n"

for medicine in medicine_info:
    if re.findall("'.+'", str(type(medicine)))[0].strip('"').strip("'") == "bs4.element.Tag":
        medicine_desc = medicine_desc + medicine.text + "\n"
    else:
        medicine_desc = medicine_desc + medicine + "\n"

file = open("medicine.txt", "w", encoding="utf-8")
file.write(product_name)
file.write(product_quantity)
file.write(product_price)
file.write(product_manufactured)
file.write(medicine_desc)
