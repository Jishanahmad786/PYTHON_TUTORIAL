i=1
c=0
n=int(input("Enter number"))
while(i<=n):
    if(n%i==0):
        c=c+1
    i=i+1
if(c==2):
    print("Prime")
else:
    print("Not Prime")
