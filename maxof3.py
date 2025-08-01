a=input("enter the numbers: ")
x,y,z=a.split(" ")
if(x > y and x > z):
    print(f"max element is {x}")
elif(y > x and y > z):
    print(f"max element is {y}")
else:
    print(f"max element is {z}")