x=int(input("Tabani giriniz:"))
y=int(input("Üssü giriniz:"))
a=pow(x,y)
sayi=0
sayi2=len(str(a))
for i in range(sayi):
    sayi=str(a)[i]
    sayi2+=int(d)
print("Girdiğiniz Uslu sayı",a,"olup rakamları toplamı==>",sayi2)