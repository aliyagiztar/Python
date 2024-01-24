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
