import math
sayı=int(input("bir sayı giriniz:"))
b=math.factorial(sayı)
print(b)

n=b
tot=0
while(n>0):
    dig=n%10
    tot=tot+dig
    n=n//10
print("Sonucun basamakları toplamı:",tot)