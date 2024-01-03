#konsolun temizlenmesi
import os, requests, bs4, sys
import time
from bs4 import BeautifulSoup

import pull, main

import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
import numpy as np

print("Hisseler yükleniyor...")
with open("hisse.txt", "r", encoding="utf-8") as file:
    hisse_list = file.readlines()
    hisse_list = [hisse.strip() for hisse in hisse_list]
    file.close()

clear = lambda: os.system('cls')
clear()

# kağıt kodunun notebook da kontrolü, True=var, False=yok
def notebookCheck(hisse):
    if hisse in hisse_list:
        return True
    elif hisse:
        if pull.PullPrice(hisse) == True:
            return True
        else:
            return False

def symbolCheck(symbol): # sembol kontrolü, True=var, False=yok
    url = "https://borsa.doviz.com/hisseler/" + symbol
    response = requests.get(url)
    html_icerigi = response.content
    soup = bs4.BeautifulSoup(html_icerigi, "html.parser")

    try:
        baslik = soup.find("div", {"class": "text-xl font-semibold text-white"}).text
    except AttributeError:
        return True
    else:
        return False
    
def symbolAdd(symbol):
    with open("hisse.txt", "a", encoding="utf-8") as file:
        file.write("\n" + symbol)
        file.close()
    print("Hisse eklendi.")
    time.sleep(2)
    clear()


def main():
    clear()
    print("Hisse Listesi ekleme menüsüne hoşgeldiniz!")
    
    while True:
        print("Lütfen hissenin sembol ismini büyük harflerle giriniz. Örneğin TUPRS, ASELS ... ")
        print("Programdan çıkmak için 'q' tuşuna basınız.")
        isim = input("Hisse adı: ")

        if isim == "q":
            break

        if symbolCheck(isim) == True:
            print("Bu sembol ile ilgili veri bulunamadı.")
            time.sleep(2)
            clear()
        else:
            if notebookCheck(isim)==True:
                print("Bu sembol zaten mevcut.")
                time.sleep(2)
                clear()
            if notebookCheck(isim)==False:
                symbolAdd(isim)
                print("Hisse eklendi.")


    