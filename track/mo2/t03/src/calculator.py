from ast import operator
num1=int(input("enter the num1:"))
num2=int(input("enter the num2:"))
operator=input("enter the operator:")
if(operator=="+"):
    print(num1+num2)
elif(operator=="-"):
    print(num1-num2)
elif(operator=="*"):
    print(num1*num2)
elif(operator=="/"):
    print(num1/num2)
else:
    print("invalid operator")