# Amaç, halka arzı olan şirketlerin kağıt fiyatlarının her dakika güncellenmesi
# ve taban bozması durumunda kullanıcıyı bilgilendirmesi


# Gerekli kütüphanelerin import edilmesi
import requests
from bs4 import BeautifulSoup
import time
import os

import pull, add, watch


def Main():
    # hisse.txt dosyasından kağıt isimlerinin okunması
    with open("hisse.txt", "r", encoding="utf-8") as file:
        hisse_list = file.readlines()
        hisse_list = [hisse.strip() for hisse in hisse_list]
        file.close()

    # konsola hisse.txt dosyasındaki kağıt isimlerinin yazdırılması
    print("### Hisse Listesi ###")
    for i in hisse_list:
        print(i)
    print("#####################")

    # kullanıcıdan input alınması
    print("Lütfen yapacağınız işlemi seçiniz: ")
    print("1- Hisse Ekle")
    print("2- Hisseleri İzlemeye Al")
    print("q- Programı Kapat")

    # kullanıcıdan input alınması
    islem = input("Seçiminiz: ")

    if islem == "1":
        add.main()
    elif islem == "2":
        watch.main()
    elif islem == "q":
        quit()

if __name__ == "__main__":
    Main()