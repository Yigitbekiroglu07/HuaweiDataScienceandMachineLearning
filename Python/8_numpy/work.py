import numpy as np


# SORU 1
# 1) NumPy kullanarak 1’den 20’ye kadar sayılardan oluşan bir dizi oluşturun.
# 2) Dizinin kaç eleman içerdiğini ekrana yazdırın.

## 1. yol

np_array1 = np.arange(1, 21)
print("Dizi:", np_array1)
print("Eleman sayısı:", np_array1.size)

## 2.yol

dizi_2 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
print(f"Dizinin eleman sayısı: {len(dizi_2)}")


# SORU 2
# 1) [5, 10, 15, 20, 25] değerlerinden oluşan bir NumPy dizisi oluşturun.
# 2) Dizideki tüm elemanları 3 ile çarpın.
# 3) Sonucu ekrana yazdırın.

np_array2 = np.array([5, 10, 15, 20, 25])
result_2 = np_array2 * 3
print(f"Çarpım işlemi sonucu: {result_2}")


# SORU 3
# 1) 0’dan 30’a kadar sayılar içeren bir dizi oluşturun.
# 2) Bu diziden sadece 10 ile 20 arasındaki elemanları slicing kullanarak seçin.

np_array3 = np.arange(0,31)
result_3 = np_array3[10:21]
print(f"Slicing işlemi: {result_3}")


# SORU 4
# 1) [1,2,3] ve [4,5,6] dizilerini oluşturun.
# 2) Bu iki diziyi NumPy kullanarak birleştirin.

array_40 = np.array([1,2,3])
array_41 = np.array([4,5,6])
result_4 = np.concatenate((array_40,array_41))
print(f"Kümelerin birleşimi: {result_4}")


# SORU 5
# 1) 1’den 12’ye kadar sayılar içeren bir dizi oluşturun.
# 2) Bu diziyi reshape kullanarak 3x4 boyutunda bir matrise dönüştürün.
# 3) Matrisin shape değerini yazdırın.

array_5 = np.arange(1,13)
result_5 = array_5.reshape(3,4)

print(result_5)
print("Shape:", result_5.shape)


# SORU 6
# 1) Aşağıdaki matrisi oluşturun
# [[1,2,3],
#  [4,5,6],
#  [7,8,9]]
# 2) İkinci satırı ekrana yazdırın.
# 3) İkinci sütunu ekrana yazdırın.

array_6 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(f"İkinci satır: {array_6[1]}")
print(f"İkinci sütun: {array_6[:,1]}")

# SORU 7
# 1) 3x3 boyutunda rastgele sayılardan oluşan bir matris oluşturun.
# 2) Matrisin ortalamasını hesaplayın.
# 3) Matrisin maksimum değerini yazdırın.


array_7 = np.random.rand(3,3)

print("Matris:\n", array_7)
print("Ortalama:", np.mean(array_7))
print("Max:", np.max(array_7))

# SORU 8
# 1) [2,4,6,8] ve [1,3,5,7] dizilerini oluşturun.
# 2) Dizileri eleman bazlı çarpın.
# 3) Sonucu ekrana yazdırın.

array_8 = np.array([2,4,6,8])
array_8_1 = np.array([1,3,5,7])

sonuc = array_8 * array_8_1

print("Sonuç: ", sonuc)


# SORU 9
# 1) 1’den 9’a kadar sayılar içeren bir dizi oluşturun.
# 2) Bu diziyi 3x3 matrise dönüştürün.
# 3) Matrisin transpose’unu hesaplayın.

array_9 = np.arange(1,10)
reshape_9 = array_9.reshape(3,3)
print("3x3 Matris: ",reshape_9)
result = reshape_9.T
print("Transpose: ",result)


# SORU 10
# 1) 1 ile 50 arasında rastgele 10 tam sayı üretin.
# 2) Bu sayılardan oluşan dizinin toplamını hesaplayın.
# 3) Dizinin ortalamasını yazdırın.

array_10 = np.random.randint(1,51,10) # [17  2 10 29 46 10 16 21 50 23]

total = np.sum(array_10)

mean = np.mean(array_10)

print("Matris Dizisi: ", array_10)

print("Dizinin toplamı: ", total)

print("Dizinin ortalaması", mean)


