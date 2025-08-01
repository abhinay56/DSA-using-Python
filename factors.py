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
    
def prime_n(n):
    primelist=[]
    for i in range(1,n+1):
        if(prime(i)):
            primelist=primelist+[i]
    return (primelist)

def  primeproduct(n):
    if n <= 0:
        return False
    for i in range(2, n):  # no sqrt, check all from 2 to m-1
        if n % i == 0:
            j = n // i
            if prime(i) and prime(j):
                return True
            else:
                return False
n=int(input("enter num:"))
print(factor(n))
print(prime(n))
print(prime_n(n))
print(primeproduct(n))

