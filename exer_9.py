for i in range(1,1000):
    if i<9:
        print(i, end=" ")
    elif len(str(i))==2:
        if int(str(i)[0])+int(str(i)[1])<9:
            print(i, end=" ")
    elif len(str(i))==3:
        if int(str(i)[0]) + int(str(i)[1])+int(str(i)[2])<9:
            print(i, end=" ")
