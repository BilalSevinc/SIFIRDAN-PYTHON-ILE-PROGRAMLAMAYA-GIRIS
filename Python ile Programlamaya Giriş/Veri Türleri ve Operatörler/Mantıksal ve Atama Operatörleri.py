# Mantıksal Operatörler

x = 5                                   # x değişkenine 5 değeri atanır.
print(x > 3 and x < 10)                 # and: VE operatörü; iki koşul da True ise sonuç True olur.
                                        # x > 3 → 5 > 3 → True
                                        # x < 10 → 5 < 10 → True
                                        # True and True → True

x = 15                                  # x'in değeri 15 olarak güncellenir.
print(x > 3 and x < 10)                 # 15 > 3 → True, 15 < 10 → False → True and False → False
print(not(x > 3 and x < 10))            # not: değerin tersini alır. False → True

print(not(False))                       # not(False) → True
print(not(True))                        # not(True) → False

yas = 18                                # yas değişkeni 18 değerini tutar.
mezuniyet = "lise"                      # mezuniyet değişkeni bir metin değeridir (str).
print(yas > 18 or mezuniyet == "lise")  # or: VEYA operatörü; koşullardan en az biri True ise sonuç True.
                                        # yas > 18 → 18 > 18 → False
                                        # mezuniyet == "lise" → True
                                        # False or True → True

# Atama Operatörleri

x = 5                                   # x = 5
print(x)                                # x'in değeri ekrana yazdırılır → 5

x = x + 3                               # x'in önceki değerine 3 eklenir → 5 + 3 = 8
y = 5                                   # y = 5
y += 3                                  # y = y + 3 ile aynı anlamdadır → 5 + 3 = 8 (kısa yazım)
                                        # += artırma atama operatörüdür.

print(x)                                # x = 8
print(y)                                # y = 8
print(x == y)                           # == eşitlik karşılaştırması → 8 == 8 → True

x = 2                                   # x = 2
print(x ** 5)                           # ** üs alma operatörü → 2^5 = 32
x = x ** 5                              # x artık 32 değerini alır.
print(x)                                # ekrana 32 yazdırılır.

sayi1 = 10                              # sayi1 = 10
sayi2 = sayi1                           # sayi2, sayi1'in mevcut değerini kopyalar → sayi2 = 10

sayi1 = sayi1 + 2                       # sayi1 = 10 + 2 = 12
sayi2 += 2                              # sayi2 = sayi2 + 2 şeklinde çalışır → sayi2 = 10 + 2 = 12

print(sayi1 == sayi2)                   # 12 == 12 → True (ikisi de aynı sonuca ulaştı)

"""

--- OUTPUT ---

True
False
True
True
False
True

5
8
8
True
32
32
True

"""