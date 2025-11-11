# Değişken Tanımlama 

number1 = float(input("1. sayı: "))   # input(): kullanıcıdan klavyeden veri alır ve her zaman metin (str) döndürür.
                                      # "1. sayı: " ekranda kullanıcıya gösterilen bilgilendirme yazısıdır.
                                      # float(): str olarak gelen değeri ondalıklı sayıya (float türüne) dönüştürür.
                                      # = operatörü: sağdaki değeri soldaki değişkene atar, yani bellekte saklar.
                                      # number1: değişken adı; kullanıcının girdiği sayıyı tutar.

number2 = float(input("2. sayı: "))   # İkinci sayıyı da aynı yöntemle kullanıcıdan alır ve float türüne çevirir.

total = number1 + number2             # + operatörü toplama işlemi yapar.
                                      # number1 ve number2 sayısal türde olduğundan sonuç da sayı olur.
                                      # total değişkeni toplam sonucu saklar.

average = total / 2                   # / operatörü bölme yapar ve her zaman float sonuç üretir.
                                      # total'i 2'ye bölerek ortalama hesaplanır.
                                      # average değişkeni ortalama sonucu saklar.

print("Ortalama:", average)           # print(): ekrana çıktı yazdırır.
                                      # Birden fazla ifade virgülle yazıldığında araya otomatik boşluk koyar.

a = 3                                 # a değişkenine 3 tam sayısı atanır.
b = 5                                 # b değişkenine 5 tam sayısı atanır.

print(a)                              # a değişkeninin değerini ekrana yazar.
print(b)                              # b değişkeninin değerini ekrana yazar.
print(a, b)                           # Birden fazla değeri aynı anda ekrana yazar (aralarında boşluk ile).

a = 7                                 # a değişkeninin değeri güncellenir. Önceki 3 unutulur, yerine 7 kaydedilir.

print(a)                              # Güncel a değerini ekrana yazar (7).

c = 2 * a + b                         # * çarpma, + toplama işlemidir.
                                      # İşlem önceliğine göre önce çarpma, sonra toplama yapılır.
                                      # c değişkeni bu matematiksel işlemin sonucunu saklar.

print(c)                               

"""
1a = 10   - Geçersiz: Değişken isimleri sayı ile başlayamaz.
a1 = 10   - Geçerli: Harfle başlar, sonra sayı olabilir.
a_1 = 10  - Geçerli: Alt çizgi (_) kullanılabilir.
a-1 = 10  - Geçersiz: Tire (-) değişken isminde kullanılamaz.
a 1 = 10  - Geçersiz: Değişken isimlerinde boşluk olamaz.
_1a = 10  - Geçerli: Alt çizgi ile başlamak serbesttir.
yaş = 25  - Geçerli: Türkçe karakter kullanılabilir ama genelde İngilizce karakter kullanmak tercih edilir (yas).
if = 10   - Geçersiz: 'if' Python'da özel bir anahtar kelimedir, değişken adı olamaz.
"""

# Veri Türleri

var1 = 5                              # int: tam sayı veri türü.
var2 = 5.0                            # float: ondalıklı sayı veri türü.
var3 = "5"                            # str: metin veri türü (tırnak içi yazılan her şey metindir).
var4 = (5 == 5)                       # == karşılaştırma operatörüdür; True veya False döndürür. Sonuç: True → bool türü.

print(var1)                           # var1'in değerini yazar.
print(var2)                           # var2'nin değerini yazar.
print(var3)                           # var3'ün değerini yazar.
print(var4)                           # var4'ün değerini yazar.

print(type(var1))                     # type(): Bir değişkenin türünü ekrana yazdırır. (int)
print(type(var2))                     # (float)
print(type(var3))                     # (str)
print(type(var4))                     # (bool)

print(var1 * 2)                       # 5 * 2 = 10 → sayı ile sayı çarpılır.
print(var2 * 2)                       # 5.0 * 2 = 10.0 → ondalıklı işlem sonucu float döner.
print(var3 * 2)                       # "5" * 2 = "55" → metin tekrar edilir (string çarpma özelliği).
print(var4 * 2)                       # True * 2 → 1 * 2 = 2 → bool sayısal olarak işlem görebilir (True=1, False=0).

print(type(var4 * 2))                 # Sonucun türü int olur.

sayi = 10                             # sayi değişkeni int türünde bir değer tutar.
pi = 3.14                             # pi float türünde bir değer tutar.
isim = "Bilal"                        # isim str türünde (yazı/metin) bir değer tutar.
kontrol = True                        # kontrol bool türünde bir değer tutar.

print(sayi)                           # Değerleri ekrana yazdırma
print(pi)
print(isim)
print(kontrol)

print(2 * pi * 5)                     # Matematiksel işlem: 2 * pi * yarıçap (örnek daire çevresi formülü gibi)

print(type(sayi))                     # Türlerini tekrar gösterme
print(type(pi))
print(type(isim))
print(type(kontrol))

"""

--- OUTPUT ---

1. sayı: 10
2. sayı: 5
Ortalama: 7.5

3
5
3 5
7
19

5
5.0
5
True

<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>

10
10.0
55
2

<class 'int'>

10
3.14
Bilal
True

31.400000000000002

<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>

"""