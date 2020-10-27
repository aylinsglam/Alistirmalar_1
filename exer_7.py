t=0
x=list()
for i in range(100,1000):
    if int((str(i))[0])+int((str(i))[1])==int((str(i))[2]):
        t=t+1
        x.append(i)
print(x)
print("bu sayılardan ", t , "tane vardır.")
        
