sum=0
n=int(input("Enter n number"))
while(n>0):
  r=n%10
  sum=sum+r*r
  n=n//10
print(sum)
  
