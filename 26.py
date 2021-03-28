def mukemmel(sayi):
    toplam=0
    for i in range(1,sayi):
        if(sayi%i == 0):
            toplam += i
    if(sayi==toplam):
        return True

mukemmelSayilar=[]
for i in range(1,1000):
    if(mukemmel(i)):
        mukemmelSayilar.append(i) 

print("Mükemmel sayılar",mukemmelSayilar)