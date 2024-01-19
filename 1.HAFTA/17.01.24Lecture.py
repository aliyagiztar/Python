# Tek satır yorum eklemek için '#' işareti kullanılır. IDE tarafından yorum olarak algılanır ve kodun parçası değildir.
# 'Single line comments' are used with '#' symbol. IDE recognizes them as comments, not as a part of the code.

"""
Çok satırlı yorumlar için üç tırnak işareti kullanılır. Bu, genellikle kodun genel açıklaması için kullanılır.
Multi-line comments are denoted with triple quotes. This is commonly used for providing a general description of the code.
"""

print('MERHABA')  # Bu, ekrana 'MERHABA' yazdırır. Çoğu geliştirici bu yöntemi tercih eder.
print('BENİM ADIM         TARIK')  # Ekrana 'BENİM ADIM         TARIK' yazar.
print("MERHABA" 
      "BEN İSTEDİĞİM "
      "ŞEKİLDE YAZI      YAZDIRMAK"
      " İSTİYORUM")  # Birden fazla satırda string birleştirme. Sonuç tek bir satırda görüntülenir.

print(""" IAU 
   COMPUTER 
                                  ENGINEERING   """)  # Çok satırlı string. Format, girintilerle korunur.

"""
ALGORITMA
Bir işlemi sonlandırmak için takip edilen mantıklı adımlar bütünü.
Algorithm is a set of logical steps followed to conclude a process.
"""

"""
Bu algoritma, kullanıcıdan bir sayı alıp bu sayının çift olup olmadığını kontrol eder.
This algorithm takes a number from the user and checks if it is even or not.
"""

"""
Bu algoritma, kullanıcıdan iki sayı alır ve çıkarma işlemi sonucunun negatif olmamasını sağlar.
This algorithm takes two numbers from the user and ensures the subtraction result is not negative.
"""

"""
DEĞİŞKEN KAVRAMI
Variables are fundamental structures that store data coming from the user or resulting from a calculation.
"""

"""
Veri Tipleri: Metinsel, Sayısal ve Mantıksal.
Data Types: Textual, Numerical, and Boolean.
"""

# Değişkenlerin veri tipini öğrenmek için 'type()' fonksiyonu kullanılır.
# To find out the data type of variables, 'type()' function is used.

# PRINT İLE EKRANA YAZDIRMA TİPLERİ
# Different ways to print to the console.

# 1. Yöntem: Değişkenleri virgülle ayırarak yazdırma.
# Method 1: Printing variables by separating them with commas.

# 2. Yöntem: F-string kullanarak değişkenleri yazdırma.
# Method 2: Using f-string to print variables.

### String KAÇIŞ (ESCAPE) İFADELERİ
# Escape sequences in strings

# \n: Bir sonraki karakteri alt satıra geçirir.
# \n: Moves the next character to the next line.

# \t: Kendinden sonraki karakterle arasında tab kadar boşluk bırakır.
# \t: Leaves a tab space after itself.

# End: Print ifadesindeki varsayılan son karakteri (\n) değiştirmek için kullanılır.
# End: Used to change the default end character (\n) in print statements.

# Sep: Print ifadesindeki argümanlar arasındaki ayırıcıyı değiştirmek için kullanılır.
# Sep: Used to change the separator between arguments in a print statement.
print("Merhaba Dünya", "Burası mecidiyeköy", "Burdan çıkış yok", sep="\n")
