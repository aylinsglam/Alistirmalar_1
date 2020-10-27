x=list()
for i in range(1000,10000):
    if (str(i))[0]>(str(i))[-1]:
        x.append(i)
print(len(x))
