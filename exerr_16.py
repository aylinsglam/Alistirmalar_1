#kullanıcı tarafından girilen bir sayının asal olup olmadığını kontrol edelim
x=int(input("bir sayı giriniz: "))
bolenler=list()
a=int((x/2)+1)
for i in range(2,a):
    if x%i==0:
        bolenler.append(i)
if x!=1 and len(bolenler)==0:
    print(x, "bir asal sayıdır.")
else:
    print(x, "Bir asal sayı değildir.")


      
