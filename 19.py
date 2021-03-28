a=1
b=0
f=int(input("Ucgensel sayi olup olmadığını sorgulayacağın sayıyı gir:"))
for i in range(1,f+1):
    b+=i
    if(b==f):
        a=0
        print("Girdiğiniz ",f," sayısı üçgensel sayı olup\n",i,".üçgensel sayıdır",b)
if(a):
    print("Üçgensel Sayı değildir")