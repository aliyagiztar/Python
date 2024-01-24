# Kullanıcıdan bir not değeri alıyoruz.
# We're asking for a grade from the user.
not_degeri = float(input("Lütfen notunuzu giriniz: "))

# Girilen not 49'dan büyükse geçti, değilse kaldı yazdırıyoruz.
# If the entered grade is greater than 49, we print 'passed', otherwise 'failed'.
if not_degeri > 49:
    print("Geçti")
else:
    print("Kaldı")
