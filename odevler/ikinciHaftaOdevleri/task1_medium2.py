# Kullanıcıdan virgüllerle ayrılmış sayılar isteyin  örn: 24,67,98,23

# Girilen sayıları liste haline getirip büyükten küçüğe sıralayın ve ekrana yazdırın örn: 98 67 24 23

# Ekrana en büyük ve en küçük sayının farkını şu şekilde yazdırın: [maks - min = result] örn: 98 - 23 = 75

# Girilen sayıların ortalamasını ekrana yazdırın

myList = input("Virgüllerle ayırarak sayılar giriniz -->> ").split(",")

intList = list(map(int, myList))
intList.sort()
min = intList[0]
intList.sort(reverse=True)
max = intList[0]
toplam = 0

print(intList)

print(f"Girdiğiniz en büyük sayı ile en küçük sayı farkı -->> {max} - {min} = {max - min}")

for x in range(len(intList)):
    toplam += intList[x]
    x += 1
print(f"Girdiğiniz sayıların ortalaması -->> {(toplam / len(intList)):.2f}")
