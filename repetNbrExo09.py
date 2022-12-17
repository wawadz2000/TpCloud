list1=[5,6,8,6,4,5,5,1,3,5,9]
i=0
ln=len(list1)
while i < ln :
    if list1.count(list1[i]) > 1 :
        list1.remove(list1[i])
    ln=len(list1)    
    i=i+1
print(list1)