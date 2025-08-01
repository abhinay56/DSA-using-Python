num1=int(input("Enter the num1 value:"))
num2=int(input("Enter the num2 value:"))
operator=input("Enter the operation to perform:")
if(operator=="+"):
    print(f"Addition of {num1} and {num2} is",num1+num2)
elif(operator=="-"):
    print(f"Substraction of {num1} and {num2} is",num1-num2)
elif(operator=="*"):
    print(f"Multiplication of {num1} and {num2} is",num1*num2)
elif(operator=="/"):
    print(f"Division of {num1} and {num2} is",num1/num2)
else:
    print("Enter correct Operator")