def sumsquare(l):
    sq = []
    odds = 0
    evens = 0
    for i in range(len(l)):
        if(l[i]%2 != 0):
            odds += l[i]**2
        if(l[i]%2 == 0):
            evens += l[i]**2
    sq = [odds,evens]
    return (sq)
l = list(map(int,input("enter elements: ").split()))
print(sumsquare(l))

