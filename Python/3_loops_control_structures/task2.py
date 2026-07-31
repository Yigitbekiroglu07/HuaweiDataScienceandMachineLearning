# ============================================================
# SORU 1 (IF)
# Kullanıcıdan bir sayı alın.
# Sayı pozitifse "Pozitif", negatifse "Negatif", sıfırsa "Sıfır" yazdırın.
# ============================================================

# sayi = int(input("Bir sayi girin : "))

# if sayi > 0:
#     print("Pozitif")
# elif sayi == 0:
#     print("Sifir")
# else:
#     print("Negatif")

# ============================================================
# SORU 2 (FOR)
# 1'den 10'a kadar (10 dahil) sayıları yazdırın.
# Ayrıca bu sayıların toplamını hesaplayıp ekrana yazdırın.
# ============================================================

for sayi in range(1, 11):
    print(sayi)

toplam = 0

for sayi in range(1, 11):
    toplam += sayi

print(toplam)


# ============================================================
# SORU 3 (WHILE)
# Kullanıcıdan "q" yazana kadar sürekli giriş alın.
# Kullanıcı her giriş yaptığında "Girdiniz: ..." şeklinde ekrana yazdırın.
# Kullanıcı "q" yazarsa döngü bitsin ve "Çıkış yapıldı" yazsın.
# ============================================================


# giris = ""

# while giris != "q":
#     giris = input("Bir şey yazın (çıkmak için q): ")
#     if giris != "q":
#         print(f"Girdiniz: {giris}")


# ============================================================
# SORU 4 (NESTED)
# 1'den 20'ye kadar sayıları dolaşın.
# Eğer sayı çiftse "Çift", tekse "Tek" yazdırın.
# Ayrıca sayı 10'dan büyükse yanına "Büyük", değilse "Küçük/Eşit" yazdırın.
# Örnek çıktı: 12 -> Çift - Büyük
# ============================================================

for sayi in range(1,21):
    if sayi % 2 == 0:
        if sayi > 10:
            print(f"{sayi} Cift - Büyük")
        else:
            print(f"{sayi} Çift Kucuk/Eşit")
        
    else:
        if sayi > 10:
            print(f"{sayi} Tek - Büyük ")
        else:
            print(f"{sayi} Tek - Küçük/Eşit")