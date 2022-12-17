while True :
    print("add list (1,2,3...) : ")
    nbr=input()
    nbrlist=[]
    nbrimair=[]
    x=''
    nbrlist.append(nbr[0])
    i=2
    for j in range(0,len(nbr)):
        if j==i :
            nbrlist.append(nbr[i])
            i=i+2

    for k in range(0,len(nbrlist)):
        if int(nbrlist[k]) % 2 != 0 or int(nbrlist[k])==1:
            nbrimair.append(nbrlist[k])

    for w in range(0,len(nbrimair)):
        x=str(x+nbrimair[w]+',')

    print(x.rstrip(x[-1]))



    

