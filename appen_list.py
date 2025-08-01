def shuffle(l1,l2):
    if(len(l1)==len(l2)):
        l3=l1+l2
        l3.sort()
        return (l3)
    elif(len(l1)>len(l2)):
        l3=l2+l1
        l3.sort()
        return (l3)
    elif(len(l1)<len(l2)):
        l3=l1+l2
        l3.sort()
        return (l3)
l1=list(map(int,input("enter element:").split()))
l2=list(map(int,input("enter element:").split()))
print(shuffle(l1,l2))