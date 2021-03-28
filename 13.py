girilen=int(input("bir sayı değeri girin:"))
toplam=0
for i in range(1,girilen+1):
    sonuç=i**i
    toplam+=sonuç
print(toplam)