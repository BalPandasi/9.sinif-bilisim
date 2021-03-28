a=int(input("sayıyı giriniz:"))
b=int(0)
for i in range(1,int(a+1)):
    b+=i**i
print(b)