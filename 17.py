b=" "
a=int(input("binary kodu hesaplanacak sayıyı giriniz:"))
while a!=0:
    b=str(a%2)+b
    a//=2
print(b)