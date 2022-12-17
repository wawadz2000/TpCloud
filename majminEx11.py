while True:
    print("text: ")
    txt=str(input())
    maj=0
    min=0
    for i in range(0,len(txt)):
        if txt[i].islower() :
            min=min+1
        elif txt[i].isupper() :
            maj=maj+1    
    print("MAJUSCULE ",maj)
    print("MINUSCULE ",min)
        