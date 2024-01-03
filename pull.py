# fonksiyona göre borsa.doviz.com'dan işlem yapılması
# bütün kağıtlar BIST borsası baz alındı

import requests, bs4
from bs4 import BeautifulSoup


def PullPrice(symbol):
    url = "https://borsa.doviz.com/hisseler/" + symbol  # Burasi algolab ile tekrar yazılacak, 15 dk gecikmeli
    response = requests.get(url)
    html_icerigi = response.content
    soup = bs4.BeautifulSoup(html_icerigi, "html.parser")

    try:
        baslik = soup.find("div", {"class": "text-xl font-semibold text-white"}).text
    except AttributeError:
        print("Bir hata oluştu.")
    return baslik

def PullChange(symbol):
    url = "https://borsa.doviz.com/hisseler/" + symbol
    response = requests.get(url)
    html_icerigi = response.content
    soup = bs4.BeautifulSoup(html_icerigi, "html.parser")
    baslik = soup.find("div", {"class": "down"}).text
    return baslik