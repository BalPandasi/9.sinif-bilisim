def asal(sayi):
    sonuc=True
    for i in range(2,sayi):
        if(sayi%i == 0):
            sonuc=False
    return sonuc
for a in range(2,10001):
    if (asal(a)==1) and asal(a+2)==1:
        print(a,"bir chen sayisidir")