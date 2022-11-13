#CLASS

class Person:        #genellikler büyük harfle başlar. Bir class tanımlandıktan sonra ya attribute ya da method tanımlanmalı fakat boş bir şekilde tanımlamak istersek pass kullanmalıyız.

    pass
    # CLASS ATTRIBUTES
   
    # Bir obje oluşturulduğunda mutlaka tanımlanması gereken bilgileri constructor (yapıcı metod)ların içine atıyoruz fakat sürekli kullanmmayacağımız bilgileri class attributelarının içine atıyoruz
    adress = "bilgi girilmedi"

    #CONSTRUCTOR (YAPICI METOD)
    def __init__(self, name, year): # burada yazılan self classtan türetilmiş objeleri ifade eder. Bu örnekte p1 ve p2 yerine geçer diyebiliriz. Selften sonra yazılan parametreler ise selfin yani objenin üzerine eklemek istediğimiz değerleri ifade eder. Self yerine farklı isimler de yazılabilir fakat genelde self yazılır.
        self.name = name
        self.year = year
        print("init metodu çalıştırıldı")
        # OBJECT ATTRIBUTES

    #INSTANCE METHODS
    def giris(self):
        print(f"Merhabalar, benim adım {self.name}") # Buradaki self objeyi temsil eder. Eğer p1 üzerinden giris'i çağırıyorsak p1.isim'i alır fakat p2 üzerinden giris'i çağırırsak burada p2.isim'i temsil eder.
    def yasHesapla(self):
        return 2019 - self.year

#OBJECT (INSTANCE)
p1 = Person(name = "abdullah", year = 2003)   #p1 objesi tanımlandı ve bu şekilde p1 objesi üzerinden Person classındaki methodlara ya da attributeslara erişilebilir. Değerleri atarken parametre isimlerirni girmemize gerek yoktur ancak okunulabilirliğini arttırmak için yapılması iyi olur.

p2 = Person(name = "konuralp", year = 1998)

# BİR OBJENİN ATTRIBUTELARINI GÜNCELLEME
p1.name = "ahmet"
p1.adress = "eskişehir"


    # BİR OBJENİN ATTRIBUTELARINA ERİŞİM
# print(f"\nisim -> {p1.name}, doğum tarihi -> {p1.year}, adres -> {p1.adress}")
# print(f"isim -> {p2.name}, doğum tarihi -> {p2.year}, adres -> {p2.adress}")

p1.giris()
print(f"Merhaba benim adım {p2.name} ve {p2.yasHesapla()} yaşındayım") # burada name derken parantez koymuyoruz çünkü direkt bir değer veriyor fakat yasHesapla'da parantez koymamızın sebebi bize bir işlem yapan metot çağırmamız. Toparlayacak olursam p1.name bir değeri fakat p1.yasHesapla bir metodu çağırır.

class Circle:
    #class object attribute
    pi = 3.14

    def __init__(self, yaricap = 1):
        self.yaricap = yaricap

    #methods
    def cevreHesap (self):
        return 2 * self.pi * self.yaricap
    def alanHesap (self):
        return self.pi * (self.yaricap**2)

c1 = Circle() # yaricap bire eşitlendi
c2 = Circle(5)

print(f"c1 için alan --> {c1.alanHesap()} --- cevre --> {c1.cevreHesap()}")
print(f"c2 için alan --> {c2.alanHesap()} --- cevre --> {c2.cevreHesap():.2f}")

                    ###########################################################################

#Inheritance (kalıtım) : Miras alma
# Person --> name, lastName, age, eat(), run(), drink()

# Student (Person), Teacher(Person)  kalıtım, oluşturduğumuz bir classın attributelarını daha sonrasında başka bir class ta da kullanmamıza yarar. Yani bu örnekte Person classının name lastName eat() gibi attributelarını ya da metotlarını direkt Student ya da Teacher classlarına da tanımlamamızı sağlar. Person özellikleri student ile Tachera gider fakat Student veya Teacher özellikleri Persona gitmez. Person bir temel sınıftır.

class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print("Person Created")

    def benKimim(self):
        print ("Ben bir insanım")

    def ye(self):
        print("Yiyorum")

class Student(Person):  # Student da bir person olduğundan gidip Person classını çalıştırır. 
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname)
        self.studentNumber = number
        print("Student Created") #Eğer studentın bir init metodu varsa personun init metodunu ezer. Bunun olmasını istemiyorsak eğer yukarıdaki Person.__init__(self) metodunu kullanırız. Bu durumda önce persondaki init sonra studenttaki init başlatılır.  
    def benKimim(self): #eğer bunu tanımlarsak ve s1 üzerinden çağırısak persondaki benKimimi ezer yani ben bir öğreniciym gösterir. Eğer tanımlamazsak ve s1.benKimim() dersek bu sefer ben bir insanım değerini gösterir. Bu ezme olayına OVERRIDE denir.
        print("Ben bir öğrenciyim")

class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname, lname)
        self.branch = branch

    def benKimim(self):
        print(f"Ben bir {self.branch} öğretmenim")


p1 = Person("Abdullah", "Onur")
s1 = Student("Mert", "Demir", 112)
t1 = Teacher("İrfan", "Altınok", "Sınıf Öğretmeni")

print(f"p1 için --> isim - {p1.firstName} | soyisim - {p1.lastName}")
print(f"s2 için --> isim - {s1.firstName} | soyisim - {s1.lastName} | numara - {s1.studentNumber}")
print(f"t1 için --> isim - {t1.firstName} | soyisim - {t1.lastName} | branş - {t1.branch}")

p1.benKimim()
s1.benKimim()
t1.benKimim()
s1.ye()

                    ###########################################################################

# OZEL METOTLAR
class Movie():
    def __init__(self, title, director, duration) -> None:
        self.title = title
        self.director = director
        self.duration = duration
    
    def __str__(self) -> str:
        return (f"{self.title} by {self.director}")
    
    def __len__(self):
        return self.duration

m1 = Movie("Film Adı", "Yönetmen Adı", 123)

print(m1)
print(len(m1)) #burada normalde lan metodu yoktur fakat biz yukarıda def ile tanımladığımızdan dolayı bize istediğimiz değeri döndürür.
