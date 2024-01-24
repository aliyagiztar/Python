# Kullanıcıdan bir not değeri alıyoruz.
# We're asking for a grade from the user.
not_degeri = float(input("Lütfen notunuzu giriniz: "))

# Girilen not 49'dan büyükse geçti, değilse kaldı yazdırıyoruz.
# If the entered grade is greater than 49, we print 'passed', otherwise 'failed'.
if not_degeri > 49:
    print("Geçti")
else:
    print("Kaldı")

# Kullanıcıdan bir sayı alıyoruz ve bu sayıyı float türüne dönüştürüyoruz.
# We are asking for a number from the user and converting this number to float type.
sayi = float(input("Lütfen bir sayı giriniz (0 ile 100 arasında): "))

# Eğer sayı 0'dan küçükse veya 100'den büyükse, uygun aralıkta bir değer girilmesi gerektiğini söyleyen bir mesaj yazdırıyoruz.
# If the number is less than 0 or greater than 100, we print a message stating that a value within the appropriate range must be entered.
if sayi < 0 or sayi > 100:
    print("Girdiğiniz sayı 0 ile 100 arasında olmalıdır.")
else:
    print("Girdiğiniz sayı uygun aralıktadır.")

    # Kullanıcıdan çocuk sayısını alıyoruz.
    # We are asking for the number of children from the user.
    cocuk_sayisi = int(input("Lütfen çocuk sayısını giriniz: "))

    # Çocuk sayısının negatif olup olmadığını kontrol ediyoruz.
    # We check if the number of children is negative.
    if cocuk_sayisi < 0:
        print("Çocuk sayısı için negatif sayı girilemez.")
    else:
        # Eğer çocuk sayısı 3 veya daha az ise her biri için 200 TL hesaplıyoruz.
        # If the number of children is 3 or less, we calculate 200 TL for each.
        if cocuk_sayisi <= 3:
            ek_odeme = cocuk_sayisi * 200
        # Eğer çocuk sayısı 3'ten fazla ise her biri için 400 TL hesaplıyoruz.
        # If the number of children is more than 3, we calculate 400 TL for each.
        else:
            ek_odeme = cocuk_sayisi * 400

        # Toplam ek ödemeyi yazdırıyoruz.
        # We print the total additional payment.
        print("Toplam ek ödeme: {} TL".format(ek_odeme))

