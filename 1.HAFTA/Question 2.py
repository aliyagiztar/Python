
sayi1 = float(input("Lütfen birinci sayıyı giriniz: "))
sayi2 = float(input("Lütfen ikinci sayıyı giriniz: "))


sonuc = sayi1 - sayi2


if sonuc < 0:
    
    sayi1, sayi2 = sayi2, sayi1
    sonuc = sayi1 - sayi2
    print(f"Sayıların yerleri değiştirildi. Yeni sonuç: {sonuc}")
else:
    print(f"Çıkarma sonucu: {sonuc}")
