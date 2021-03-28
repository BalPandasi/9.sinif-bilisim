sayi=0
sayi2=0
for i in range(1,101):
    sayi+=i
    sayi2+=pow(i,2)
print("İlk 100 doğal sayının kareleri toplamı ile toplamlarının kareleri arasındaki farkı==>",pow(sayi,2)-sayi2)