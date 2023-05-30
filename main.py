import requests
from bs4 import BeautifulSoup
import smtplib

MY_EMAIL = "ongoingpython@gmail.com"
MY_PASSWORD = "cqzmoivhyfjtfkrc"
URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url=URL, headers=headers)
response.raise_for_status()
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
price = float(soup.find(name="span", class_="a-offscreen").getText().strip("$"))
title = soup.find(name="span", id="productTitle").getText().strip()

if price < 100:
    message = f"Subject:Low Price!!!\n\nThe {title} is current at the price of ${price}!\nGrab it at {URL}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="sakina903@gmail.com",
                            msg=message.encode("utf-8"))
