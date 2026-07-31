"""""
Kullanıcıdan vize notu ve final notu alalım
- Ortalama hesaplaması
- harf notu belirleme
- sonucu ekrana yazdırma
"""

vize = int(input("Vize notunuzu giriniz: "))
final = int(input("Final notunuzu giriniz: "))

def ortalama():
    ortalama = vize * 40 / 100 + final * 60 / 100
    print(f"Ortalamaniz: {ortalama}")
    return ortalama

def harf_notu_belirle(ortalama: float) -> str:
    if ortalama >= 88:
        return "A"
    elif ortalama >= 80:
        return "B"
    elif ortalama >= 60:
        return "C"
    else:
        return "F"

ortalama_degeri = ortalama()
harf_notu = harf_notu_belirle(ortalama_degeri)

print("Ortalama değer: ",ortalama_degeri)
print("Harf Notunuz:", harf_notu)
    
    
    

    
