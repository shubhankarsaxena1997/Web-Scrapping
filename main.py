import requests
from bs4 import BeautifulSoup
import smtplib

EMAIL = "shubh.python.test@gmail.com"
PASSWORD = "yzkdciszgiwgfdum"
PORT = 587

URL = "https://www.amazon.com/OnePlus-Unlocked-Android-Smartphone-Version/dp/" \
      "B09RG132Q5/ref=sr_1_2?keywords=nord+ce2&qid=1663602644&sprefix=Nord+ce%2Caps%2C442&sr=8-2"
# URL = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"

header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/105.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,hi;q=0.8"
}
response = requests.get(URL, headers=header)
web_page_content = response.text
soup = BeautifulSoup(web_page_content, 'html.parser')
prod_name = soup.find(name="span", class_="product-title-word-break").text
price = int(soup.find(name='span', class_="a-offscreen").text.split("$")[1].split(".")[0])
if price < 280:
    with smtplib.SMTP("smtp.gmail.com", PORT) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        message = f"Subject: Amazon Price tracker\n\n The product{prod_name}that you wished for, is now in your budget i.e {price}, you can buy it now. {URL}"
        message = message.encode('utf-8')
        connection.sendmail(from_addr=EMAIL, to_addrs="mickeyjoshdecember@gmail.com",
                            msg=message)
