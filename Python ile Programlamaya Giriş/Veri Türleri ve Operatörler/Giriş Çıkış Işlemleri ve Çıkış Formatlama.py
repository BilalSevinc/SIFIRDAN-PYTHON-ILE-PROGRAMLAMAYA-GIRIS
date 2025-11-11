# Giriş Çıkış İşlemleri

isim = input("Lütfen isminizi giriniz: ")       # input(): kullanıcıdan klavyeden veri alır ve her zaman metin (str) veri döndürür.
                                                # "Lütfen isminizi giriniz: " ekranda kullanıcıya gösterilen açıklama mesajıdır.
                                                # isim: kullanıcının girdiği metni tutan değişkendir.

print("Merhaba, " + isim + ".")                 # + operatörü burada metin birleştirme (string concatenation) işlemi yapar.
                                                # "Merhaba, " + isim + "." → örnek çıktı: Merhaba, Ali.

print(type(isim))                               # type(): bir değişkenin veri türünü ekrana yazdırır.
                                                # isim, input() ile alındığı için türü her zaman str olur.

sayi = int(input("Lütfen bir sayı giriniz: "))  # input(): kullanıcıdan metin alır → int(): bu metni tam sayıya dönüştürür.
                                                # Kullanıcı harf girerse hata oluşur (ValueError).
print(sayi + 100)                               # sayısal toplama işlemi yapılır; sayıya 100 eklenerek ekrana yazdırılır.

# # # # #

help(print)                                     # help(): belirtilen komutun/donanımın nasıl kullanılacağıyla ilgili yardım bilgisi gösterir.
                                                # print fonksiyonunun kullanım açıklamasını terminalde gösterir.

print("Ocak", "Şubat", "Mart", end = "...")     # print(): birden fazla değeri aralarına varsayılan olarak boşluk koyarak yazar.
                                                # end="...": satır sonunda normalde '\n' (yeni satır) yerine '...' yazılmasını sağlar.

print(isim, sayi, sayi + 1, sayi + 2, sep=" - ")# sep=" - " parametresi, print içindeki öğelerin arasına koyulacak karakteri belirler.
                                                # Varsayılan boşluk yerine burada " - " kullanılmıştır.

# Çıkış Formatlama

urun = "Kalem"                                  # urun değişkenine bir metin atanır (str).
fiyat = 15.5                                    # fiyat değişkeni ondalıklı sayıdır (float).

print("Ürün: " + urun + " Fiyatı:", fiyat)      # Metin + metin birleştirme + virgülle yazma karışık kullanılmış.
                                                # Virgülden sonra otomatik boşluk gelir.

print("Ürün: {} Fiyatı: {}".format(urun, fiyat))  
                                                # .format(): metin içinde {} bırakılan yerlere sırasıyla değer yerleştirir.

print(f"Ürün: {urun} Fiyatı: {fiyat:.2f}")      # f-string: Metin içinde değişkenleri {} kullanarak doğrudan yazmayı sağlar.
                                                # {fiyat:.2f}: fiyat değerini virgülden sonra 2 basamak olacak şekilde biçimlendirir.
"""

--- OUTPUT ---

Lütfen isminizi giriniz: bilal
Merhaba, bilal.

<class 'str'>

Lütfen bir sayı giriniz: 10
110

Help on built-in function print in module builtins:

print(*args, sep=' ', end='\n', file=None, flush=False)
    Prints the values to a stream, or to sys.stdout by default.

    sep
      string inserted between values, default a space.
    end
      string appended after the last value, default a newline.
    file
      a file-like object (stream); defaults to the current sys.stdout.
    flush
      whether to forcibly flush the stream.

Ocak Şubat Mart...bilal - 10 - 11 - 12

Ürün: Kalem Fiyatı: 15.5
Ürün: Kalem Fiyatı: 15.5
Ürün: Kalem Fiyatı: 15.50

"""