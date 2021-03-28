sayi = input("Sayi giriniz:")
kuvvet = len(sayi) 
sayi = int(sayi)
toplam = 0
rakam = 0
kontrol = sayi
for i in range(kuvvet):
    rakam = sayi % 10 
    toplam += rakam ** kuvvet 
    sayi = sayi // 10 

if(toplam == kontrol):
    print("Armstrong sayıdır")
else:
    print("Armstrong sayısı değildir")