from bs4 import BeautifulSoup
import requests
import lxml
import os

url = "https://www.amazon.com/FINIS-Underwater-Bone-Conduction-Player/dp/B0169RSNPG/ref=sr_1_4?keywords=waterproof+headphones+for+swimming+fins&qid=1637240574&qsid=130-2276365-0611149&sr=8-4&sres=B07CRRY7D6%2CB0169RSNPG%2CB08NCHYNW3%2CB097BCBLHL%2CB07J2Z5DBM%2CB088LW4JKR%2CB0957WVRD7%2CB0931284PS%2CB08ML44WHV%2CB07ZDMJ75K%2CB08ZYK8945%2CB00OY8G3NC%2CB082YQ3ZQ7%2CB085VX9JY7%2CB07RGZ5NKS%2CB0876349QT&srpt=HEADPHONES"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,he-IL;q=0.8,he;q=0.7"
}

response = requests.get(url=url, headers=header)
web_page = response.text
soup = BeautifulSoup(web_page, "lxml")
# print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
price = float(price.split("$")[1])
# print(type(price))
print(price)
