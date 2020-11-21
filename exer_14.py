carpim=list()
fark=list()
for i in range(2,60607):
    if 121212%i==0:
        carpim.append(i)
        if len(carpim)%2==0:
            a=int(len(carpim)/2)
print(carpim[a] , "ve" , carpim[a-1])

