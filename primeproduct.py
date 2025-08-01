def factor(n):
    fac=[]
    for i in range(1,n+1):
        if(n%i==0):
            fac=fac+[i]
    return (fac)

def prime(n):
    if(factor(n)==[1,n]):
        return True
    else:
        return False
    
def  primeproduct(n):
    if n <= 0:
        return False
    for i in range(2, n):  
        if n % i == 0:
            j = n // i
            if prime(i) and prime(j):
                return True
            else:
                return False
n=int(input())
print(primeproduct(n))
    