import time

kartSifresi = "9147"
bakiye = 1000
denemeHakki = 3
kart_islem_durumu = True

print("X Bankasına Hoş Geldiniz")

islemDurumu = True
while islemDurumu:
    girilenSifre = input("Kart Şifrenizi girin : ")

    if girilenSifre != kartSifresi:
        print("Şifre Yanlış. Tekrar deneyin")
        denemeHakki -= 1
        print("Deneme hakkınız", denemeHakki)

        if denemeHakki == 0:
            print("Kartınız Bloklandı. Banka ile en kısa zamanda görüşünüz.")
            islemDurumu = False
    else:
        while kart_islem_durumu:
            print("----------------------")
            print("Giriş Yapıldı")
            print("----------------------")
            time.sleep(3)
            print("""
            Yapılacak işlemi seçiniz
            ----------------------------
            1-) Para Çekme
            2-) Para Yatırma
            3-) Bakiye Sorgulama
            4-) Çıkış

            """)
            while kart_islem_durumu:
                print("----------------------------------")
                islemNo = input("İşlem numarasını giriniz : ")

                if islemNo == "4":
                    print("Çıkış yapıldı")
                    islemDurumu = False
                    kart_islem_durumu = False

                elif islemNo == "3":
                    print(f"Toplam Bakiye {bakiye}₺")

                elif islemNo == "2":
                    yatirilacakMiktar = int(input("Yatırılacak Para Girin : "))
                    bakiye += yatirilacakMiktar
                    print("Lütfen Bekleyin..")
                    time.sleep(2)
                    print(f"{yatirilacakMiktar}₺ Yüklendi. Toplam Bakiye{bakiye}₺")

                elif islemNo == "1":
                    cekilecekMiktar = int(input("Çekilecek Para : "))
                    
                    if cekilecekMiktar > bakiye:
                        print(f"Yetersiz Bakiye. Toplam Bakiye : {bakiye}₺")
                    
                    else:
                        bakiye -= cekilecekMiktar
                        print("Para Çekiliyor. Lütfen Bekleyin..")
                        print("")
                        print("----------------------")
                        print("")
                        time.sleep(3)
                        print(f"İşlem Gerçekleşti. Kalan Bakiye : {bakiye}")
                        