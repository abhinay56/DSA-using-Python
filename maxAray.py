a=list(map(int,input("enter an array= ").split()))
print(a)
print(max(a))
sum=0
print(len(a))
for i in range(0,len(a)):
    sum=sum+a[i]
print(sum)