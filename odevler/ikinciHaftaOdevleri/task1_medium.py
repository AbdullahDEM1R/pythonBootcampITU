"""
Kullanıcıdan iki sayı ve bir karakter isteyin. 
Kullanıcıdan alınan sayıların genişliği ve uzunluğunda alınan karakterlerden oluşan bir dikdörtgen çizdirin.
!! Bu programı döngüler kullanmadan yapınız

EX:
s1 -> 5
s2 -> 7
c1 -> *

[OUTPUT]

*****
*****
*****
*****
*****
*****
*****
""" # task1_medium.pdf dosyasında görselli açıklama bulunuyor

satir = int(input("Oluşturmak istediğiniz dörtgenin satır sayısını giriniz -->> "))
sutun = int(input("Oluşturmak istediğiniz dörtgenin sutun sayısını giriniz -->> "))
karakter = input("Oluşturmak istediğiniz dörtgenin hangi karakterden oluşmasını istediğinizi giriniz -->> ")


liste = []
liste.append((("\t" + karakter * sutun) + "\n") * (satir -1))
liste.append(("\t" + karakter * sutun))

print(*liste)
