a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=int(input("Enter third number"))
if(a>b and a<c) or (a>c and a<b):
    print(a,"is middle")
elif(b>a and b<c) or (b>c and b<a):
    print(b,"is middle")
else:
    print(c,"is middle")
