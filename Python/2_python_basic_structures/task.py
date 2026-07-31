# ============================================================
# SORU 1
# Bir değişken tanımlayalım: ad = "Kaan", yas = 25, ortalama = 3.45
# Bu değişkenlerin tiplerini type() ile yazdıralım.
# ============================================================

ad = "Kaan"
yas = 25
ortalama = 3.45
print(type(ad))
print(type(yas))
print(type(ortalama))

# ============================================================
# SORU 2
# Kullanıcıdan yaş bilgisini input() ile alalım.
# Bu yaşın tipini ekrana basalım ve 5 yıl ekleyip sonucu yazdıralım.
# Not: input() her zaman string döndürür, int'e çevirmeyi unutmayalım.
# ============================================================


# yas = input("Yasinizi girin: ")
# print(f"Gelen veri tipi : {type(yas)}") # <class 'str'>
# yeni_yas = int(yas) + 5
# print(f"Yeni yaş: {yeni_yas}")

# ============================================================
# SORU 3
# Bir ürün fiyatı (float) alalım. %18 KDV hesaplayalım.
# Toplam fiyatı 2 basamak olacak şekilde yazdıralım.
# ============================================================

# urun_fiyati = float(input("Ürün fiyati : "))
# toplam_fiyat = urun_fiyati + urun_fiyati*18/100
# print(f"Toplam fiyat: {round(toplam_fiyat,2)}")


# ============================================================
# SORU 4
# Bir liste oluşturalım: sayilar = [10, 20, 30, 40, 50]
# - İlk elemanı yazdıralım
# - Son elemanı yazdıralım
# - 2. indexten sona kadar olan parçayı yazdıralım
# - Listeye 60 ekleyelim
# - Listedeki 20 değerini silelim
# ============================================================

my_list = [10,20,30,40,50]
print(my_list[0])
print(my_list[-1])
print(my_list[2:5])
my_list.append(60)
print(my_list)
my_list.remove(20)
print(my_list)


# ============================================================
# SORU 5
# Bir tuple oluşturalım: koordinat = (12, 34)
# - Tuple içindeki değerleri unpacking ile x ve y değişkenlerine alalım
# - x ve y'yi yazdıralım
# - Tuple'ın değiştirilemediğini göstermek için (yorum satırıyla) örnek verelim
# ============================================================

coordinates = (12,34)

x,y = coordinates

print(f"{x}")
print(f"{y}")

## coordinates [0] = 48 # Bu satır hata verir çünkü tuple immutable (değiştirilemez)

# SORU 6
# Bir sözlük (dictionary) oluşturalım:
# ogrenci = {"isim": "Ayşe", "yas": 22, "bolum": "Yazılım"}
# - Öğrencinin ismini yazdıralım
# - "not" anahtarı ile 90 ekleyelim
# - "yas" değerini 23 yaparak güncelleyelim
# - Tüm anahtarları ve tüm değerleri yazdıralım
# ============================================================

## Bir sözlük (dictionary) oluşturalım:
ogrenci = {"isim": "Ayşe", 
           "yas": 22, 
           "bolum": "Yazilim"}

## Öğrencinin ismini yazdıralım
print(ogrenci["isim"])


#"not" anahtarı ile 90 ekleyelim
ogrenci["Not"] = 90
print(ogrenci)

# "yas" değerini 23 yaparak güncelleyelim
ogrenci["yas"] = 23
print(ogrenci)

# Tüm anahtarları ve tüm değerleri yazdıralım
print(ogrenci.keys())
print(ogrenci.values())
print(ogrenci.items())


# ============================================================
# SORU 7
# Set oluşturalım ve tekrar edenleri temizleyelim:
# liste = ["Ali", "Ayşe", "Ali", "Mehmet", "Ayşe"]
# - listeyi set'e çevirip benzersiz isimleri yazdıralım
# - benzersiz isim sayısını yazdıralım
# ============================================================

my_list = ["Ali", "Ayşe", "Ali", "Mehmet", "Ayşe"]

my_set = set(my_list)

print(my_set)

print(len(my_set))