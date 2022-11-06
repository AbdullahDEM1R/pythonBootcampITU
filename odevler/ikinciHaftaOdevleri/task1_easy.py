mtn = "IEEE İTÜ öğrenci kolu RAS ve CS komiteleri tarafından düzenlenen Python Bootcamp eğitimine hoş geldiniz!"

# Verilen metni tüm harfleri büyük şekilde yazdırın

buyukMetin = mtn.upper()
print (buyukMetin)

# Verilen metnin her kelimesinin sadece ilk harfi büyük şekilde yazdırın

baslıkMetin = mtn.title()
print (baslıkMetin)

# Verilen metni indexleyerek 'RAS ve CS komiteleri' kısmını yazdırın

print (mtn[22:43])

# Verilen metni tamamen tersten yazdırın: "Python" ---> "nohtyP"

print(mtn[::-1])

# Verilen metinde 'İstanbul' kelimesinin olup olmadığını kontrol edin

if mtn.count("İstanbul") == 0:
    print("Metin değerinde hiç istanbul değeri geçmemektedir.")
else:
    print("Metin değerinde İstanbul değeri geçmektedir.")

# Verilen metinde 'Bootcamp' kelimesinin kaçıncı indexte olduğunu bulun

print(mtn.index("Bootcamp"))

# Verilen metni boşluklardan ayırarak liste haline çevirin

liste = mtn.split()
print (liste)

# Verilen metnin her kelimesini alfabe sırasına göre sıralayın

siraliListe = liste.sort()
print(siraliListe)

# Verilen metindeki 'a' ve 'e' karakterlerini silin

mtnYeni = mtn.replace("a", "")
mtnYeni = mtn.replace("e", "")
print(mtnYeni)

# Verilen metindeki her bir kelimeyi alt alta yazdırın

x = 0
while x < len(liste):
    print(liste[x])
    x += 1

#------------------------------------------------------

# Kullanıcıdan isim, soyisim, yaş ve okul bilgisi alarak şu formatta ekrana yazdırın:
# Merhaba ben [isim] [soyisim]. [yaş] yaşındayım ve [okul]'da okuyorum.

isim = input("İsminizi giriniz -> ")
soyisim = input("Soyisminizi giriniz -> ")
yas = input("Yaşınızı giriniz -> ")
okul = input("Okulunuzu giriniz -> ")

print (f"Merhaba ben {isim} {soyisim}. {yas} yaşındayım ve {okul}'da okuyorum.")


# Kullanıcıdan aldığınız bilgileri name, surname, age, school bilgilerinden oluşan bir dictionary (sözlük) halinde ekrana yazdırın

dict = {"name" : isim, "surname" : soyisim, "age" : yas, "school" : okul}

#------------------------------------------------------
li1 = [16, 25, 432, 23, 12, 452, 998, 278]
li2 = [98, 32, 52, 23, 54, 78, 111]

# Verilen listeleri küçükten büyüğe doğru sıralayın

li1.sort()
li2.sort()

# Verilen iki listeyi birleştirin

buyukListe = li1 + li2  #sıralamasız direkt birleştirdim.
print(buyukListe)

# Verilen iki listenin kesişen elemanlarını bulun
kesisenElemanlar = []
for x in range(len(li1)):
    for y in range(len(li2)):
        if li1[x] == li2[y]:
            kesisenElemanlar.append(li1[x])
        else:
            continue
        y += 1
    x += 1

print (kesisenElemanlar)

# Verilen iki listenin ortalamasını ayrı ayrı bulun ve şu formatta ekrana yazdırın:
# 1. Listenin ortalaması: [birinci_listenin_ortalamas]
# 2. Listenin ortalaması: [ikinci_listenin_ortalaması]

ortalama1 = 0
toplam1 = 0
ortalama2 = 0
toplam2 = 0
for x in range(len(li1)):
    toplam1 += li1[x]
    ortalama1 = toplam1 / (x+1)
for y in range (len(li2)):
    toplam2 += li2[y]
    ortalama2 += toplam2 / (y + 1)

print(f"Listenin ortalaması : {ortalama1}")
print(f"listenin ortalaması : {ortalama2:.2f}")

#------------------------------------------------------

# Kullanıcıdan iki sayı isteyin ve bu sayılara dört işlem uygulayarak sonuçları ekrana yazdırın

sayi1 = int(input ("Birinci sayıyı girin -> "))
sayi2 = int(input ("İkinci sayıyu girin -> "))
if sayi1 > sayi2:
    print(f"Toplam - {sayi1 + sayi2}\nÇıkarma - {sayi1 - sayi2}\nÇarpma - {sayi1 * sayi2}\nBölme - {(sayi1 / sayi2):.2f}")
elif sayi2 > sayi1:
    print(f"Toplam - {sayi1 + sayi2}\nÇıkarma - {sayi2 - sayi1}\nÇarpma - {sayi1 * sayi2}\nBölme - {(sayi2 / sayi1):.2f}")

# Kullanıcıdan 4 sayı isteyin ve bu sayıların en küçüğünü ekrana yazdırın

sayi1 = int(input ("Birinci sayıyı girin -> "))
sayi2 = int(input ("İkinci sayıyı girin -> "))
sayi3 = int(input ("Üçüncü sayıyı girin -> "))
sayi4 = int(input ("Dördüncü sayıyı girin -> "))
sayilar = [sayi1, sayi2, sayi3 ,sayi4]
sayilar.sort()
print(f"En küçük sayı -->> {sayilar[0]}")

# Kullanıcıdan 2 sayı isteyin ve bu sayıları birbirine bölün, çıkan sonucu noktadan sonra iki basamak olacak şekilde ekrana yazdırın

sayi1 = int(input ("Birinci sayıyı girin -> "))
sayi2 = int(input ("İkinci sayıyı girin -> "))
print (f"Bölüm işleminin sonucu -->> {(sayi1 / sayi2):.2f}")

# Kullanıcıdan 3 sayı isteyin ve en büyük sayıdan diğer iki sayıyı çıkarın

sayi1 = int(input ("Birinci sayıyı girin -> "))
sayi2 = int(input ("İkinci sayıyı girin -> "))
sayi3 = int(input ("Üçüncü sayıyı girin -> "))
sayilar = [sayi1, sayi2, sayi3]
sayilar.sort()
print(f"En büyük sayıdan diğer iki sayının çıkarılması işlemi sonucu -->> {sayilar[2] - (sayilar[0] + sayilar[1])}")
