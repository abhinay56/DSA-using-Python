a=int(input("a="))
b=int(input("b="))
temp=a
a=b
b=temp
print(f"a={a} and b={b}")
# without using temp variable
x=int(input("x="))
y=int(input("y="))
x=x+y
y=x-y
x=x-y
print(f"a={x} and b={y}")
