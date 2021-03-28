import random
sayi=random.randint(1,100)
sayac=0
while True:
    tahmin=int(input("0 ve 100 arasında bir sayı giriniz,0 girerseniz oyununuz iptal edilir:"))
    sayac+=1
    if tahmin==0:
        print("oyunu iptal ettiniz")
        break
    elif sayi<tahmin:
        print("daha küçük bir sayı giriniz")
        continue
    elif sayi>tahmin:
        print("daha büyük bir sayı giriniz:")
        continue
    elif sayi>99 or sayi<0:
        print("lütfen 0 ve 100 arasında bir sayı giriniz")
        continue
    else:
        print("tebrikler bildiniz,sayınız",sayi)
        print(sayac,"seferde buldunuz")
        break
a=int(input("sayıyı giriniz:"))
b=int(0)
for i in range(1,int(a+1)):
    b+=i**i
print(b)