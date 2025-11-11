# Aritmetik Operatörler

print(5 + 3)                      # + toplama operatörüdür; 5 ile 3'ü toplar ve sonucu ekrana yazar (8).
print(10 - 4)                     # - çıkarma operatörüdür; 10'dan 4'ü çıkarır (6).
print((7 - 2) * 5 + 10)           # Parantez önceliği: önce (7-2)=5, sonra 5*5=25, ardından 25+10=35.

print(5 / 2)                      # / gerçek bölme operatörüdür; sonucu her zaman float döndürür (2.5).
print(5 // 2)                     # // tam bölme (taban bölme) operatörüdür; sonucu küsuratsız verir (2).
print(10 // 3)                    # 10 // 3 = 3 (küsurat atılır).

print(5 % 2)                      # % mod operatörü; bölümden kalan sonucu verir. 5 % 2 = 1.
print(10 % 2)                     # 10 % 2 = 0 (çünkü 10 sayısı 2'ye tam bölünür).
print(12 % 10)                    # 12 % 10 = 2 (12'nin 10 ile bölümünden kalan).

print(2 ** 3)                     # ** üs alma operatörü; 2 üzeri 3 = 8.
print(2 ** 5)                     # 2 üzeri 5 = 32.

a = 10                            # a değişkenine 10 değeri atanır.
b = 3                             # b değişkenine 3 değeri atanır.

print("a / b =", a / b)           # / float bölme: 10 / 3 = 3.333...
print("a // b =", a // b)         # // tam bölme: 10 // 3 = 3 (küsurat atılır).
print("a + b =", a + b)           # + toplama: 10 + 3 = 13.
print("a - b =", a - b)           # - çıkarma: 10 - 3 = 7.

# Karşılaştırma Operatörleri

print(3 < 5)                      # < küçüktür karşılaştırma operatörü; 3 < 5 → True.
print(7 < 2)                      # 7 < 2 → False.
print(5 < 5)                      # 5 < 5 → False (çünkü eşitler).
print(5 <= 5)                     # <= küçük-eşit; 5 <= 5 → True.
print(2 + 2 == 4 - 0)             # == eşitlik karşılaştırması; iki taraf eşitse True döner → True.
print(5 - 2 != 10 * 2)            # != eşit değildir; 3 != 20 → True.

x = 7                             # x'e 7 atanır.
y = 5                             # y'ye 5 atanır.

print("x > y:", x > y)            # > büyüktür operatörü; 7 > 5 → True.
print("x < y:", x < y)            # < küçüktür operatörü; 7 < 5 → False.
print("x = y:", x == y)           # == eşitlik kontrolü; 7 == 5 → False.
print("x >= y:", x >= y)          # >= büyük eşit; 7 >= 5 → True.
print("x != y:", x != y)          # != eşit değil; 7 != 5 → True.

"""

--- OUTPUT ---

8
6
35
2.5
2
3
1
0
2
8
32

a / b = 3.3333333333333335
a // b = 3
a + b = 13
a - b = 7

True
False
False
True
True
True

x > y: True
x < y: False
x = y: False
x >= y: True
x != y: True

"""