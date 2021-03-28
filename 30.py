sayi=0
def asal(i):
    sayi=0
    for a in range(2,i):
        if (i%a==0):
            sayi+=1
    if sayi!=0:
        return 0
    if sayi==0:
        return i
toplam=0
sayi2=0
sayac=1
for i in range(1,1001):
    sayi2=asal(i)
    if (sayi2!=0):
        print(sayac,".asal sayı===",sayi2)
        toplam+=sayi2
        sayac+=1
print("1000 ile 1 arasında",sayac," kadar asal sayı vardır toplamları :",toplam)