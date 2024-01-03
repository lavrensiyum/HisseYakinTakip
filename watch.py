import pull, time, os

clear = lambda: os.system('cls')

def main():
    clear()
    print("İzleme ekranına hoşgeldiniz!")
    print("Listedeki hisselerin fiyatları her dakika güncellenecektir.")
    print("Unutmayın buradaki veriler BIST kuralları gereği 15 dakika gecikmelidir.\n")

    with open("hisse.txt", "r", encoding="utf-8") as file:
        hisse_list = file.readlines()
        hisse_list = [hisse.strip() for hisse in hisse_list]
        file.close()
    
    print("Toplamda " + str(len(hisse_list)) + " adet hisse bulundu.")
    
    while True:
        print("### Hisse Listesi ###")
        for i in hisse_list:
            print(i + " : " + pull.PullPrice(i))
        print("#####################")
        print("Çıkış yapmak için 'ctrl+c' tuşuna basınız.")
        print("Veriler 1 dakika sonra tekrar güncellenecektir.")
        time.sleep(60)
        clear()