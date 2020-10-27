x=list()
y=list()
for i in range(2,125):
    a=125%i
    if 125%i==200%i and 125%i==350%i:
        y.append(i)
        x.append(a)
b=max(x)
c=x.index(b)
print("{} sayısı, bu sayılara bölündüğünde en çok kalanı veren sayıdır".format(y[c]))

        
        
        
        
