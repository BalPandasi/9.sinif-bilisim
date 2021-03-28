def f(a):
	if(a<0):
		print("HATA LÜTFEN İLK SAYININ İKİNCİ SAYIDAN BÜYÜK YA DA EŞİT OLDUĞUNA EMİN OLUN")
		exit(1)
	c=1
	for b in range(1,a+1):
		c=c*b
	return c
y=int(input("Permütasyonu Hesaplanacak Sayıyı Giriniz:"))
x=int(input("Kaçlı Permütasyonları Hesaplanacak Sayıyı Giriniz:"))
print("Sonuç",f(y)/f(y-x))
