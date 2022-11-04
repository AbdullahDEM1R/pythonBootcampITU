metin = "abdullah demir"
yas = 19
print (metin [::-1]) #burada bütün her şeyi tersten yazdırır.
print (metin [2::3]) #burada 2. indexten sona kadar üçer üçer arta arta yazdırır.
print (metin [:6]) #burada ilk indexten 6. indexe kadar yazdırır fakatt 6. index dahil değil.
print (metin [12:1:-1]) #burada 12. indexten 2. indexe kadar ters yazdırır. 12. index dahil değil.

print (metin.upper()) #bütün harfleri büyütür
print (metin.lower()) #bütün harfleri küçültür
print (metin.capitalize()) #sadece başharfi büyültür
print (metin.title()) #bütün kelimelerin başharfi büyütülür
print (metin.replace('a', '-')) #bütün a harflerini - ile değiştirir. sadece tek bir harf olmasına gerek yok birden fazla harfi aynı anda değiştirebiliriz. yanyana olmalılar
print (metin.strip()) #sağdaki ve soldaki boşlukları siler. eğer lstrip dersek soldaki rstrip dersek sağdakini siler. komutun içine değer koyarsak o değerler sondaysa onları siler.
print (metin.count('a')) #belirtilen karakterden kaç tane geçtiği gösterilir.
print (metin.split()) #boşluk karakterinden sonra ayırır veya eğer içine değer atarsak o değer gördüğünde ayırır.

                                                                                ###FORMATLAMA###

print ("Merhaba benim adım {}. {} yaşındayım".format(metin, yas)) #burada formatın içine yazılan değişkenler süslü parantez ile belirtilen yere sırasıyla gelir. eğer süslü parantezlerin içine 0 1 2 gibi sayılar yazarsak önce soldan başlayarak koymak yerine sayıya göre koyar -> {1}{0}{0}, yas, metin --->> abdullah demir 19 19 yazar.
print ("Merhaba benim adım {m}. {y} . {y} yıldır yaşıyorum".format(m = metin, y = yas)) #m gördüğü yere metini y gödüğü yere yas değişkenini atar. Bu işleme geçici değişken atama diyebiliriz.
print(f"Merhaba benim adım {metin.upper()}. {yas + 10} yaşındayım")

sonuc = 95/13
print(f"Sonuc = {sonuc:1.6}") #virgülden sonra 6. basamağa göre yuvarlama yapılır yani 1.43567 şeklinde bir değer çıkartır

sayilar = [1, 54, 6, 0, 1231313, 123123]
liste = [1, 1231, 1234123, "abdullah", 123122, "demir"]
sayilar.sort() # burada sayilar listesini sıraladık
print(sayilar)
sayilar.reverse() # burada sayilar listesini tersten sıraladk.
print (liste.index("abdullah")) # abdullah değişkeninin indexini bize gösterir.
