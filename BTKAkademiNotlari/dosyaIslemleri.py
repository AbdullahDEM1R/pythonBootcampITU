# Dosya açmak için open() fonksiyonu kullanılır.
# Örnek -> open(dosyaAdi, dosyaErismeModu)
# dosyaErismeModu -> dosyayı hangi amaçla açtığımızı belirtir.

# "w" --> (write) yazma modu. Dosyayı konumda oluşturur.
# "a" --> (append) ekleme modu. Dosya konumda yoksa oluşturulur
# "x" --> (Create) oluşturma modu. Dosya zaten varsa hata verir.
# "r" --> (Read) okuma modu. VARSAYILAN MOD. Dosya konumda yoksa hata verir.

file  = open("/Users/demir/Desktop/Yazılım/pythonBootcampOdevleri/BTKAkademiNotlari/yeniDosya.txt", "w", encoding="utf-8") # daha sonrasında açtığımız dosyayla ilgili işlem yapmamız gerekebileceğinden dolayı dosyayı açarkenki parametreyi bir değişkende tutmamızda fayda vardır.
# file.close() #dosyayla işimiz bittiğinde dosyayı kapatmamız gerekir. Encoding'i UTF-8 demezsek bazen türkçe karakterleri algılayamayabiliyor.

file.write("Muhammed Abdullah DEMİR") # Eğer "w" metoduyla açarsak önceki bilgiler gider ve file.write() şeklinde içine bilgi yazabiliriz.
file.close()

file  = open("/Users/demir/Desktop/Yazılım/pythonBootcampOdevleri/BTKAkademiNotlari/yeniDosya.txt", "a")
file.write("\nİstanbul Gelişim Üniversitesi\n210403353")
file.close()

file  = open("/Users/demir/Desktop/Yazılım/pythonBootcampOdevleri/BTKAkademiNotlari/yeniDosya.txt", "r")

for x in file:
    print(x, end="") #bir değişkeni yazdırdıktan sonra alt satıra geçtikten sonra boşluk bırakma demek oluyor. Gereksiz bir boş satır eklemez aralarına.
file.close()

file  = open("/Users/demir/Desktop/Yazılım/pythonBootcampOdevleri/BTKAkademiNotlari/yeniDosya.txt", "r") # yukarıdaki işlemle birebir aynı fakat biz elle döngü açmak yerine read isimli metot ile otomatik bir şekilde değerler çekilir.
icerikler = file.read()
print(icerikler)
file.close()

file  = open("/Users/demir/Desktop/Yazılım/pythonBootcampOdevleri/BTKAkademiNotlari/yeniDosya.txt", "r")

icerik1 = file.read() # read metodu dosyanın en sonuna kadar okur ve tekrar read metodu kullanmak istediğimizde imleç kaldığı yerden okumaya çalışır fakat bu örnekte en son imleç dosyanın sonunda kaldığından read metodunun okuyabileceği bir değer kalmamaktadır.
icerik2 = file.read()
icerik3 = file.read()
print("***************************")
print(icerik1)
print("***************************")
print(icerik2)
print("***************************")
print(icerik3)
file.close()

# file.read(5) demek imleçten sonra 5 karakterlik değer oku demektir. Metodun içine verdiğimiz sayı aslında byte demektir yani 5 bytlık bir değer oku diyoruz.

file  = open("/Users/demir/Desktop/Yazılım/pythonBootcampOdevleri/BTKAkademiNotlari/yeniDosya.txt", "r")

print(file.readline(), end="") # readline komutu sadece bir satır okumaya yarar.
print(file.readline(), end="")
print(file.readline(), end="")
print("\n")
file.close()

file  = open("/Users/demir/Desktop/Yazılım/pythonBootcampOdevleri/BTKAkademiNotlari/yeniDosya.txt", "r")

liste = file.readlines() # readlines() bütün satırları okur ve bunları liste olarak tutar fakat her satırdan sonra \n olduğundan son eleman haricindeki bütün elemanların sonuna \n ekler.
print(liste)
file.close()

        ###############################################################
#     *****    DOSYA OKURKEN KULLANILAN FONKSIYONLAR    *****

with open("/Users/demir/Desktop/Yazılım/pythonBootcampOdevleri/BTKAkademiNotlari/yeniDosya.txt", "r") as file:  # bir blok oluşturulur ve artık kapatmaya gerek kalmaz. En son satıra gelince direkt kapatır.
    icerik = file.read()
    print(icerik)
    print(file.tell())
    file.seek(0) # imlecin nereye gideceğini söyler.
    print(file.tell()) #file.tell() komutu bize imleçin o dosyadaki yerini verir örneğin burada imleç 67. konumdadır.
    icerik2 = file.read()
    print(icerik2)


        ###############################################################
#                   *****    DOSYA GUNCELLEME    *****

with open("/Users/demir/Desktop/Yazılım/pythonBootcampOdevleri/BTKAkademiNotlari/yeniDosya.txt", "r+") as file: # burada hem okuma hem yazma şeklinde açmak için r+ kullandık.
    print(file.read())

# with open("/Users/demir/Desktop/Yazılım/pythonBootcampOdevleri/BTKAkademiNotlari/yeniDosya.txt", "r+") as file:
    # file.write("Bilgisayar Mühendisliği") # buradaki write() komutu 0. indexten başlayarak bizim verdiğimiz değeri üstüne yazar.

#SAYFA SONUNU GUNCELLEME

with open("/Users/demir/Desktop/Yazılım/pythonBootcampOdevleri/BTKAkademiNotlari/yeniDosya.txt", "a") as file:
    file.write("\nBilgisayar Mühendisliği") # append şeklinde açarsak eğer önce imleci en sona götürür ve o şekilde yazar.

#SAYFA BASINI GUNCELLEME

with open("/Users/demir/Desktop/Yazılım/pythonBootcampOdevleri/BTKAkademiNotlari/yeniDosya.txt", "r+") as file:
    icerik = file.read()
    icerik = "2. sınıf\n" + icerik
    file.seek(0)
    file.write(icerik)

#SAYFA ORTASINI GUNCELLEME

with open("/Users/demir/Desktop/Yazılım/pythonBootcampOdevleri/BTKAkademiNotlari/yeniDosya.txt", "r+") as file:
    liste = file.readlines()
    liste.insert(2, "Ortalama -> 3.48\n")
    file.seek(0)
    # for x in liste:
    #     file.write(x)
    file.writelines(liste)