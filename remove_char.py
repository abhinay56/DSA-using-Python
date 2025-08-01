def delchar(s,c):
    if(len(c)>1):
        return s
    am=''
    for i in range(len(s)):
        if(s[i]!=c):
            am=am+s[i]
    return (am)
s=input("enter str:")
c=input("char=")
print(delchar(s,c))