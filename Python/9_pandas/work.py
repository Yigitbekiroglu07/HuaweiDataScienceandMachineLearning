import pandas as pd

# ÖRNEK VERİ SETİ
# Aşağıdaki veri seti tüm sorular için kullanılacaktır.

veri = {
    "isim": ["Ali", "Ayşe", "Mehmet", "Zeynep", "Ahmet", "Elif"],
    "yas": [25, 30, 28, 35, 22, 27],
    "sehir": ["Ankara", "İstanbul", "Ankara", "İzmir", "Bursa", "İstanbul"],
    "maas": [5000, 7000, 6000, 8000, 4500, 6500]
}

df = pd.DataFrame(veri)

print("VERİ SETİ")
print(df)
print("-" * 50)

# SORU 1
# DataFrame'in ilk 3 satırını gösterin.

print(df.head(3))
print("-" * 50)

# SORU 2
# DataFrame'deki sütun isimlerini ekrana yazdırın.

print(df.columns)
print("-" * 50)

# SORU 3
# Sadece "isim" sütununu seçin.

print(df["isim"])
print("-" * 50)

# SORU 4
# Sadece "isim" ve "maas" sütunlarını birlikte gösterin.

print(df[["isim","maas"]])
print("-" * 50)

# SORU 5
# Yaşı 28'den büyük olan kişileri filtreleyin.

print(df[df["yas"] > 28])
print("-" * 50)

# SORU 6
# Maaşı 6000'den büyük olan kişilerin sadece isim ve maaş bilgilerini gösterin.

print(df[df["maas"] > 6000 ][["isim","maas"]])
print("-" * 50)

# SORU 7
# Maaşa göre küçükten büyüğe sıralayın.

### Tüm dataframe'e getirme
print(df.sort_values("maas"))
print("-" * 50)


### Sadece maaş sütununu getirme
print(df["maas"].sort_values(ascending=False))
print("-" * 50)

# SORU 8
# Maaşa göre büyükten küçüğe sıralayın.

print(df.sort_values("maas", ascending=False))
print("-" * 50)

# SORU 9
# Şehirlere göre gruplama yapın ve her şehir için ortalama maaşı hesaplayın.

print(df.groupby("sehir")["maas"].mean())
print("-" * 50)

# SORU 10
# "yillik_maas" adında yeni bir sütun oluşturun.
# Bu sütun maaşın 12 ile çarpılması ile oluşturulacaktır.

df["yillik_maas"] = df["maas"] * 12
print(df)
print("-" * 50)