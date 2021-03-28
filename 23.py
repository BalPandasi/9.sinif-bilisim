def f(a):
	if(a<0):
		print("HATA LÜTFEN İLK SAYININ İKİNCİ SAYIDAN BÜYÜK YA DA EŞİT OLDUĞUNA EMİN OLUN")
		exit(1)
	c=1
	for b in range(1,a+1):
		c=c*b
	return c
y2=int(input("Kombünasyonu Hesaplanacak Sayıyı Giriniz"))
x2=int(input("Kombinasyonu Hesaplanacak Sayıyı Giriniz"))
print("Sonuç",f(y2)/(f(y2-x2)*f(x2)))