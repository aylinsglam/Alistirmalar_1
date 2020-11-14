x=input("Lütfen 3 veya 4 basamkalı bir sayı giriniz: ")
while len(x)!=3 and len(x)!=4:
    x=input("Lütfen 3 veya 4 basamaklı bir sayı giriniz: ")
else:
    if x==x[::-1]:
        print("Bu bir palindromik sayıdır.")
    else:
        print("Bu bir palindromik sayı değildir.")
