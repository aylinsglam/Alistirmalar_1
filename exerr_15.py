asallar=list()
for i in range(10001,100000,2):
    #işlem kolaylığı için sadece tek sayıları kontrol ediyorum.
    a=int((i/2)+1)
    bolenler=list()
    for j in range(3,a,2):
        #sadece tek sayıları kontrol ettiğim için bölenlerde de sadece tek sayıları dahil ediyorum.
        if i%j==0:
            bolenler.append(j)
    if len(bolenler)==0:
        asallar.append(i)
print(asallar)
    
    
